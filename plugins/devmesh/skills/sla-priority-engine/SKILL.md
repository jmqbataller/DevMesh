---
name: sla-priority-engine
description: Use to assign evidence-based website operations severity and response priority from business impact, user scope, revenue/lead loss, security, compliance, availability, and client SLA rules.
---

# SLA Priority Engine

## Core rule

**Use the client's actual SLA when available. Default priority labels are operational guidance, not a contractual promise.**

Suggested fallback model:
- `P1`: site unavailable, severe security incident, critical data loss, or confirmed lead/revenue path outage
- `P2`: major feature/IDX/CRM degradation with significant business impact and workaround limited
- `P3`: partial functional, performance, SEO, accessibility, or quality issue with workable service
- `P4`: low-risk content, cosmetic, routine maintenance, or planned enhancement

Consider scope, duration, affected users, business hours, campaign/event timing, workaround, recurrence, and safety/compliance risk.

Output priority, rationale, SLA source/version, response/resolution target only when defined, escalation path, and evidence. Re-evaluate when impact changes.