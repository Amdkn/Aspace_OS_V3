# 00_Blueprints (The Schematics)

**The Architectural Master Plans.**
This folder contains the `docker-compose.yml` templates and `Ansible` playbooks to replicate the TARDIS.

---

## ⚡ Role: The Matrix
*   **What lies here**: The "Idea" of the infrastructure.
*   **How to use**: Copy a blueprint, hydrate with `.env`, and deploy.

## 📂 Contents
*   `server_init.sh`: The first script to run on a fresh VPS.
*   `docker_base.yml`: The core stack (Portainer, Traefik, Watchtower).
*   `security_hardening.sh`: The shield generator (Fail2Ban, UFW).
