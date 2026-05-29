# linear-diffs-trial

Throwaway repo to test **Linear Diffs** against the N2O workflow's real risks.
Dummy Python content; the point is the PR/branch shapes, not the code.

## What's set up

- **CI** (`.github/workflows/ci.yml`) — runs `pytest` on every PR and on `main` after merge. Job name `test` (the required status check).
- **Branch protection on `main`** — PR required, `test` check required, no direct pushes. (No required *approval* — a solo account can't approve its own PR; see gate #2.)
- **Chained branches** mirroring the workflow:
  - `feature/widget` off `main`
  - `sub1` off `feature/widget` → PR into `feature/widget`
  - `sub2` off `sub1` (stacked) → PR into `feature/widget`
  - `feature/widget` → `main` PR
- **`ci-fail-demo`** branch + PR into `main` with a deliberately failing test (for the red-CI test).
- **All three merge methods left enabled** so we can observe what Linear's merge does (gate #1).

## Test protocol (run from Linear)

1. **Merge method (gate #1 — critical):** merge **`sub1` → `feature/widget`** *from Linear*. Inspect the new commit on `feature/widget`: **merge commit or squash?** Did Linear let you *choose*?
2. **Stacked display (your original question):** while `sub1` and `sub2` are both open, do both show correctly in the Reviews tab? After `sub1` merges and GitHub retargets `sub2`, does `sub2`'s diff refresh to show only its own changes?
3. **CI gate / sync (gate #3):** open the **`ci-fail-demo`** PR in Linear — does it show CI **red**, and does it block merge? Then on a green PR, confirm status syncs both ways after merge.
4. **Approval sync (gate #2, partial):** approve a PR *from Linear* and check GitHub — does the approval appear as a **real GitHub review** by your account? (Whether it *satisfies* a required-review rule needs a second reviewer account to test fully.)
5. **Merge a protected branch:** merge **`feature/widget` → `main`** from Linear once CI is green — does it go through, and what merge commit results?

Record what you see next to each. Delete the repo when done.
