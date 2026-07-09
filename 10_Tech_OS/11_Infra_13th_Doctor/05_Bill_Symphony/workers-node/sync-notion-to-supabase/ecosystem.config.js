/* PM2 ecosystem — Symphony Phase 2 hourly worker
 * Cible : VPS Hostinger sous /home/amadeus/symphony-workers/sync-notion-to-supabase
 *
 * Lifecycle :
 *   pm2 start ecosystem.config.js   # registre + premier run
 *   pm2 save                          # persiste la liste
 *   pm2 startup                       # autostart au boot (génère cmd systemd)
 *   pm2 logs sync-notion-to-supabase  # tail
 *   pm2 trigger ... custom:run        # manuel
 *
 * Cron : '0 * * * *' = top de chaque heure (00:00, 01:00, 02:00, ...).
 */
module.exports = {
  apps: [
    {
      name: 'sync-notion-to-supabase',
      script: './sync-notion-to-supabase.js',
      cwd: '/home/amadeus/symphony-workers/sync-notion-to-supabase',
      instances: 1,
      exec_mode: 'fork',
      autorestart: false,          // run-once, exit, PM2 restart by cron
      cron_restart: '0 * * * *',   // every hour at minute 0
      max_restarts: 3,
      min_uptime: '5s',
      max_memory_restart: '300M',
      restart_delay: 5000,
      time: true,
      error_file: '/home/amadeus/symphony-workers/_logs/sync-notion-to-supabase-err.log',
      out_file: '/home/amadeus/symphony-workers/_logs/sync-notion-to-supabase-out.log',
      env: {
        NODE_ENV: 'production',
        NOTION_DATABASE_ID: '6b07315e-06ca-4652-9049-d72a1e79e906',
        PROJECT_SLUG: 'aspace_solaris',
        DLQ_DIR: '/home/amadeus/symphony-workers/_dlq',
        // SECRETS in .env on VPS (chmod 600, never committed):
        //   NOTION_TOKEN          (ntn_xxx Internal Integration Bearer)
        //   PG_CONNECTION_STRING  (postgres://user:pwd@host:port/db)
      },
    },
  ],
};
