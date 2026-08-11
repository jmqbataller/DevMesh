# Project Memory Reference

Persistent DevMesh memory is opt-in and lives in the target repository under `.devmesh/`.

## Recommended `project.json`

```json
{
  "schemaVersion": 1,
  "projectType": "nextjs",
  "packageManager": "npm",
  "commands": {
    "install": "npm ci",
    "dev": "npm run dev",
    "build": "npm run build",
    "test": "npm test",
    "lint": "npm run lint",
    "typecheck": "npm run typecheck"
  },
  "paths": {
    "source": ["src"],
    "tests": ["tests"]
  },
  "browserFacing": true,
  "database": "supabase",
  "deployment": "vercel"
}
```

Only include fields that are actually proven by the repository. Omit unknown values instead of guessing.

## `decisions.md`

Keep decisions short and durable. Suggested format:

```markdown
# DevMesh Decisions

## 2026-08-11 — Keep contact submission server-side

- Client submits to the existing server endpoint.
- Supabase secret credentials remain server-only.
- Reason: preserve the current security boundary and deployment model.
```

## `qa-baseline.json`

```json
{
  "schemaVersion": 1,
  "commands": [
    "npm test",
    "npm run build"
  ],
  "browser": {
    "routes": ["/", "/settings"],
    "viewports": [
      {"name": "desktop", "width": 1440, "height": 900},
      {"name": "phone", "width": 390, "height": 844}
    ]
  },
  "acceptedWarnings": []
}
```

Do not copy volatile logs into the baseline.

## Forbidden content

Never persist:

- API keys/tokens
- passwords
- cookies/session tokens
- private keys
- `.env` file contents
- customer/user personal data
- authorization headers

If a useful fact contains a secret value, store only the structural fact, for example `emailProvider: resend`, not the API key.
