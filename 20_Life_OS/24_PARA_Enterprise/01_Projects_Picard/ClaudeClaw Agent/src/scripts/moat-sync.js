import fs from 'fs/promises';
import path from 'path';

/**
 * Moat Sync Script — Bridges Drawbridge and the AI Agent
 * Usage: node moat-sync.js --id <id> --status <status>
 */

const MOAT_DIR = path.join(process.cwd(), '.moat');
const DETAIL_FILE = path.join(MOAT_DIR, 'moat-tasks-detail.json');
const MD_FILE = path.join(MOAT_DIR, 'moat-tasks.md');

async function syncMoatStatus() {
  const args = process.argv.slice(2);
  const idArg = args.indexOf('--id');
  const statusArg = args.indexOf('--status');

  if (idArg === -1 || statusArg === -1) {
    console.error('Usage: node moat-sync.js --id <id> --status <status>');
    process.exit(1);
  }

  const taskId = args[idArg + 1];
  const targetStatus = args[statusArg + 1];

  try {
    const detailData = await fs.readFile(DETAIL_FILE, 'utf8');
    const tasks = JSON.parse(detailData);

    const taskIndex = tasks.findIndex(t => t.id === taskId);
    if (taskIndex === -1) {
      console.error(`Task with ID ${taskId} not found.`);
      process.exit(1);
    }

    // Update status
    tasks[taskIndex].status = targetStatus;
    console.log(`✓ Synchronizing task ${taskId} to status: ${targetStatus}`);

    // Save JSON
    await fs.writeFile(DETAIL_FILE, JSON.stringify(tasks, null, 2));

    // Regenerate Markdown
    let mdContent = `# Moat Tasks - Connected to ${path.basename(process.cwd())}\n\n`;
    tasks.forEach((t, i) => {
      const statusIcon = t.status === 'done' ? '✅' : t.status === 'doing' ? '⏳' : '⭕';
      mdContent += `### ${i + 1}. ${t.title || 'Untitled Task'} [${t.status.toUpperCase()}] ${statusIcon}\n`;
      mdContent += `- **ID**: \`${t.id}\`\n`;
      mdContent += `- **Comment**: ${t.comment}\n`;
      if (t.selector) mdContent += `- **Selector**: \`${t.selector}\`\n`;
      mdContent += `\n---\n\n`;
    });

    await fs.writeFile(MD_FILE, mdContent);
    console.log(`✓ Successfully updated Drawbridge task lists.`);

  } catch (error) {
    console.error(`Status sync failed: ${error.message}`);
    process.exit(1);
  }
}

syncMoatStatus();
