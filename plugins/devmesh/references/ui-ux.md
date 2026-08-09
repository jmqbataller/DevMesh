# UI/UX Reference

## Fast audit order

1. Can the user identify the primary task?
2. Can they complete it on narrow mobile and desktop?
3. Are controls understandable and reachable?
4. Are system states visible?
5. Is typography readable?
6. Is motion useful rather than distracting?
7. Is visual styling internally consistent?

## Common regression traps

- `overflow: hidden` masking broken layout
- fixed card heights with dynamic content
- icon-only actions without accessible labels
- hover-only functionality
- low-contrast muted text
- sticky headers covering anchor targets
- animations that intercept clicks
- huge desktop spacing collapsing poorly on mobile
- z-index escalation instead of fixing stacking context
