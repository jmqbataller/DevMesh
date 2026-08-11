---
name: backup-restore-drill
description: Use to verify website/WordPress backup completeness, retention, readability, restore instructions, and staging restore readiness instead of assuming an existing backup is recoverable.
---

# Backup Restore Drill

## Core rule

**A backup that has never been inspected or restored is not proven recovery.**

Verify where authorized:
- backup timestamp and retention
- database included
- uploads/media included
- themes/plugins/custom code included as required
- config/secrets handled separately and safely
- archive/object readability and expected size signals
- off-site or provider independence where appropriate
- documented restore procedure
- restore permissions/credentials availability without exposing them

Preferred proof is a non-production restore drill:
`select recovery point → restore to staging/isolation → database/app boot → representative pages/login/media/forms/integrations → Browser QA → record duration/findings`

Never overwrite production merely to test a restore. Use `risk-engine` before destructive restoration. Never place credentials or private customer data in reports.

Completion distinguishes `backup exists` from `restore verified` and records last verified restore, recovery gaps, and `BLOCKED` evidence.
