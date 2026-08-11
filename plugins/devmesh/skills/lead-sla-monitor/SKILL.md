---
name: lead-sla-monitor
description: Use to measure and monitor real-estate lead journey latency and failures from website form/IDX inquiry through webhook/email/CRM receipt, assignment, and downstream processing where observable.
---

# Lead SLA Monitor

## Core rule

**A submitted form is not a delivered lead. Measure each observable handoff independently and never invent downstream receipt or assignment timestamps.**

Possible checkpoints: browser submit, application acceptance, queued job, webhook/API response, SMTP acceptance, CRM creation, deduplication, routing/assignment, agent notification, and acknowledgement.

Use synthetic test leads where allowed. Capture correlation ID/test marker, timestamps, latency per hop, final destination, duplicates, retries, failures, and SLA source.

Route underlying delivery bugs to `wordpress-lead-flow-qa`, `email-deliverability-doctor`, or `real-estate-crm-integration-specialist`.

Protect consumer PII; do not use real customer records for routine testing when synthetic data is sufficient.