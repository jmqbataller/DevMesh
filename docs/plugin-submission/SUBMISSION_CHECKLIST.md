# DevMesh OpenAI Plugin Directory Submission Checklist

This checklist is for the **skills-only** DevMesh v0.8.0 submission.

## Already prepared

- [x] Public GitHub repository
- [x] Production logo
- [x] ChatGPT Agent Skill source with 49 bundled playbooks
- [x] Automated GitHub Release asset: `devmesh-chatgpt-v0.8.0.zip`
- [x] Listing copy, website, support, privacy, terms, starter prompts
- [x] Five positive + three negative reviewer test cases
- [x] v0.8 release notes
- [x] CI validation of plugin/adapter/submission contracts
- [x] Real-estate IDX/MLS, RESO Web API, listing-sync/search, and IDX compliance playbooks included in the portable bundle

## Publisher-only OpenAI Platform steps

1. Sign in to the OpenAI Platform organization that will publish DevMesh.
2. Confirm the submitter has **Apps Management: Write** permission.
3. Complete **individual verification** or **business verification** for the publisher identity.
4. Open the Plugin Submission Portal → Create plugin → **Skills only**.
5. Fill public Info using `LISTING.md`.
6. Upload the GitHub Release `devmesh-chatgpt-v0.8.0.zip`.
7. Resolve automated skill-scan findings without weakening security/policy behavior.
8. Add starter prompts from `LISTING.md`.
9. Add all cases from `TEST_CASES.md` (five positive, three negative).
10. Select supported countries/regions.
11. Paste `RELEASE_NOTES.md`.
12. Review policy attestations and choose **Submit for Review**.
13. Wait for OpenAI review; submission does not immediately publish.
14. If approved, choose **Publish**.
15. Verify DevMesh in the Plugins Directory and run Mission Control, full-stack, IDX/MLS, Quick, Deep, and negative-boundary smoke tests.

## Files

- Listing: `docs/plugin-submission/LISTING.md`
- Privacy: `docs/plugin-submission/PRIVACY.md`
- Terms: `docs/plugin-submission/TERMS.md`
- Reviewer tests: `docs/plugin-submission/TEST_CASES.md`
- Release notes: `docs/plugin-submission/RELEASE_NOTES.md`
- Upload bundle: GitHub Release `v0.8.0` → `devmesh-chatgpt-v0.8.0.zip`
