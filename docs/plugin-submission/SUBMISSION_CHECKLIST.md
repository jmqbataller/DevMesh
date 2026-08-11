# DevMesh OpenAI Plugin Directory Submission Checklist

This checklist is for the **skills-only** DevMesh submission.

## Already prepared in the repository

- [x] Public DevMesh GitHub repository
- [x] Production logo
- [x] Portable ChatGPT skill bundle source
- [x] GitHub Release asset: `devmesh-chatgpt-v0.6.0.zip`
- [x] Listing name, category, short description, and long description
- [x] Website URL
- [x] Support URL
- [x] Privacy policy
- [x] Terms of use
- [x] Starter prompts
- [x] Five positive reviewer test cases
- [x] Three negative reviewer test cases
- [x] Initial release notes
- [x] Skills-only submission path; no MCP server or reviewer credentials required

## Publisher-only steps in OpenAI Platform

These steps must be completed from the OpenAI organization that will own the public listing.

1. Sign in to the OpenAI Platform.
2. Select the organization that will publish DevMesh.
3. Confirm the submitter has **Apps Management: Write** permission. Organization owners already have the required submission permission.
4. Complete **individual verification** if publishing under your own verified name, or **business verification** if publishing under a company/business identity.
5. Make sure the identity selected for the submission matches the public publisher identity, website, support details, privacy policy, and terms.
6. Open the Plugin Submission Portal.
7. Select **Create plugin**.
8. Select **Skills only**.
9. Fill the public Info fields using `LISTING.md`.
10. Upload the final `devmesh-chatgpt-v0.6.0.zip` skill bundle from the GitHub Release.
11. Review and resolve any automated skill scan findings. Do not bypass security/policy findings merely to make the scan pass.
12. Add the starter prompts from `LISTING.md`.
13. Add all reviewer cases from `TEST_CASES.md`: five positive and three negative.
14. Select only countries/regions where the publisher is ready to support the plugin and comply with applicable terms.
15. Paste `RELEASE_NOTES.md` into the release-notes field.
16. Review the listing, skill bundle, prompts, tests, availability, and policy attestations.
17. Select **Submit for Review**.
18. Wait for OpenAI review. Submission does not immediately publish the plugin.
19. If approved, return to the portal and choose when to **Publish**.
20. After publication, verify that DevMesh appears in the universal Plugins Directory in ChatGPT and Codex and run the smoke prompts below.

## Smoke prompts after publication

```text
Use DevMesh.
Build a working quotation website.
```

```text
DevMesh Quick: fix this small UI bug with the minimum safe change.
```

```text
DevMesh Deep: review this application for production readiness.
```

## Files to copy from

- Public listing: `docs/plugin-submission/LISTING.md`
- Privacy: `docs/plugin-submission/PRIVACY.md`
- Terms: `docs/plugin-submission/TERMS.md`
- Reviewer tests: `docs/plugin-submission/TEST_CASES.md`
- Release notes: `docs/plugin-submission/RELEASE_NOTES.md`
- Upload bundle: GitHub Release `v0.6.0` → `devmesh-chatgpt-v0.6.0.zip`
