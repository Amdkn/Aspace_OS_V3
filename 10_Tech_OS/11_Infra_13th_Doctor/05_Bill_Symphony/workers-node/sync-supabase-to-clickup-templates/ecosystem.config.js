/* PM2 ecosystem — Symphony Phase 2 worker 2
 * Cron: 5 min après l'heure pile (laisse Stage 1 finir Notion→Supabase)
 */
module.exports = {
  apps: [{
    name: 'sync-supabase-to-clickup-templates',
    script: './sync-supabase-to-clickup-templates.js',
    cwd: '/home/amadeus/symphony-workers/sync-supabase-to-clickup-templates',
    instances: 1,
    exec_mode: 'fork',
    autorestart: false,
    cron_restart: '5 * * * *',  // every hour at xx:05
    max_restarts: 3,
    min_uptime: '5s',
    max_memory_restart: '300M',
    restart_delay: 5000,
    time: true,
    error_file: '/home/amadeus/symphony-workers/_logs/sync-supabase-to-clickup-templates-err.log',
    out_file: '/home/amadeus/symphony-workers/_logs/sync-supabase-to-clickup-templates-out.log',
    env: {
      NODE_ENV: 'production',
      PROJECT_SLUG: 'aspace_solaris',
      CLICKUP_TARGET_LIST_ID: '901416812179',
      DLQ_DIR: '/home/amadeus/symphony-workers/_dlq',
      // SECRETS in .env (chmod 600):
      //   PG_CONNECTION_STRING
      //   CLICKUP_TOKEN  (pk_xxxxx — get from ClickUp Settings > Apps > API Token)
    },
  }],
};
