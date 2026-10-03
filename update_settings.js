const fs = require('fs');

const file = '90_cubefarm_fork_integration/client/src/ui/ManagerConsole.tsx';
let content = fs.readFileSync(file, 'utf8');

const themeSelector = `
      <div className="card">
        <h3>🎨 Theme</h3>
        <label className="field">
          <span>Active Theme</span>
          <select value={settings.theme || 'aurora'} onChange={(e) => set({ theme: e.target.value })}>
            <option value="aurora">Aurora</option>
            <option value="glassmorphism">Glassmorphism</option>
            <option value="terminal">Terminal</option>
            <option value="brutalism">Brutalism</option>
            <option value="dark-oled">Dark OLED</option>
            <option value="warm-paper">Warm Paper</option>
          </select>
        </label>
      </div>`;

content = content.replace(
  '<div className="card">\n        <h3>🧠 Agents</h3>',
  themeSelector + '\n      <div className="card">\n        <h3>🧠 Agents</h3>'
);

fs.writeFileSync(file, content);
