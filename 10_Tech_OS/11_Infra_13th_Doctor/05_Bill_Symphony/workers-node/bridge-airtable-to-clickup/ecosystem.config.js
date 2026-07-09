/* PM2 ecosystem — Symphony Phase 2 bridge
 * Cron: 10 min après l'heure pile (chain: 00 sync-notion / 05 sync-supabase / 10 bridge-airtable)
 */
module.exports = {
  apps: [{
    name: 'bridge-airtable-to-clickup',
    script: './bridge-airtable-to-clickup.js',
    cwd: '/home/amadeus/symphony-workers/bridge-airtable-to-clickup',
    instances: 1,
    exec_mode: 'fork',
    autorestart: false,
    cron_restart: '10 * * * *',
    max_restarts: 3,
    min_uptime: '5s',
    max_memory_restart: '300M',
    restart_delay: 5000,
    time: true,
    error_file: '/home/amadeus/symphony-workers/_logs/bridge-airtable-to-clickup-err.log',
    out_file: '/home/amadeus/symphony-workers/_logs/bridge-airtable-to-clickup-out.log',
    env: {
      NODE_ENV: 'production',
      AIRTABLE_BASE_ID: 'appmWf5Xm7w9Ae0ky',
      AIRTABLE_BRIEFS_TABLE_ID: 'tblqo7cjdpImMoaVq',
      CLICKUP_FASTTRACK_LIST_ID: '901416200299',
      CLICKUP_FORGE_TEXT_LIST_ID: '901416785045',    // Posts LinkedIn/X (default text)
      CLICKUP_FORGE_VISUAL_LIST_ID: '901416785054',  // Visuels Statiques (default visual)
      DLQ_DIR: '/home/amadeus/symphony-workers/_dlq',
      // SECRETS in .env (chmod 600):
      //   AIRTABLE_BEARER_AUTH  (patXXX...)
      //   CLICKUP_TOKEN         (pk_xxxxx)
    },
  }],
};
