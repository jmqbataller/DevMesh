# Security Reference

## Secrets

Never commit or expose:

- API secret keys
- database service-role/admin keys
- private tokens
- webhook signing secrets
- OAuth client secrets

A variable being present in an environment file does not make it client-safe.

## Input boundaries

Treat as untrusted:

- form data
- query/path parameters
- cookies/tokens until verified
- webhook payloads until signature verification
- imported files
- external API data

## Authorization

Check authorization at the server/data boundary, not only by hiding UI controls.

## Logging

Avoid logging credentials, access tokens, raw payment information, sensitive personal data, or full private payloads unless explicitly required and safely handled.
