---
name: deploy
description: Containerizes a codebase with Docker and makes it production-ready. Use when the user asks to deploy, dockerize, containerize, stage, or prepare for production.
---
# Deploy

## Steps
1. Detect stack, entrypoint, ports, env vars, and external services (DB, cache, queue).
2. **Dockerfile** per service:
   - Multi-stage build, slim pinned base image (never `latest`).
   - Copy dependency files first for layer caching.
   - Non-root `USER`, `HEALTHCHECK`, `EXPOSE`, exec-form `CMD`.
   - Prod dependencies only in the final stage.
3. **.dockerignore**: .git, node_modules, venv, tests, .env, docs.
4. **docker-compose.yml** + `docker-compose.prod.yml` override: app + backing services, named volumes for data, internal network, `restart: unless-stopped`, resource limits, `depends_on` with healthchecks, env from `.env`.
5. **Config**: `.env.example` listing every var. Never bake secrets into images or compose files.
6. **Prod readiness**: logs to stdout/stderr, `/health` endpoint, graceful SIGTERM shutdown, debug off, stateless app (scales horizontally).
7. **Verify**: `docker compose build` → `up -d` → healthchecks green → smoke-test main endpoint → image scan (trivy / docker scout) if available.
8. **DEPLOY.md** (short): run, env vars, scaling (`--scale app=N`), logs, rollback.

## Output
Files created, verify results, run command. List remaining prod gaps (secrets manager, TLS/reverse proxy, backups, CI/CD) as one-liners; don't build them unless asked.
