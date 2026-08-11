---
name: client-access-inventory
description: Use to inventory which operational systems and roles are available for a client/site without storing secret values, so DevMesh can separate actual access from blocked verification.
---

# Client Access Inventory

## Core rule

**Inventory capability and ownership, not credentials. Never record passwords, API keys, session cookies, private keys, backup codes, or raw tokens.**

Track systems such as WordPress admin, hosting, DNS/registrar, CDN/WAF, SSH/SFTP, WP-CLI, database, Search Console, GA4/GTM, SMTP/email, CRM, backups, IDX/MLS portal/API, GitHub, deployment platform, and domain ownership.

For each: `AVAILABLE`, `MISSING`, `PENDING`, `EXPIRED`, `UNKNOWN`, role/permission level when known, owner, recovery/escalation contact, and last verified date.

Before promising a task, compare required capabilities against this inventory. Missing access becomes `BLOCKED`, with the smallest specific access request needed.