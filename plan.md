# Development Plan

## Phase 1 --- Stabilize

-   [ ] Confirm repository root and Git remote.
-   [ ] Verify PHP syntax, routes, and database connection.
-   [ ] Test register, login/logout, browse, apply, and status display.
-   [ ] Verify server-side admin restrictions.

## Phase 2 --- Security

-   [ ] Review prepared statements and output escaping.
-   [ ] Review session handling and upload validation.
-   [ ] Add CSRF protection and safe error handling.
-   [ ] Keep secrets out of Git and back up database before schema
    changes.

## Phase 3 --- UI

-   [ ] Standardize navigation, buttons, forms, cards, and spacing.
-   [ ] Test mobile and desktop layouts.
-   [ ] Verify all links and accessibility basics.

## Phase 4 --- Recommendation engine

-   [ ] Confirm `system.py` input/output and score formula.
-   [ ] Test skill normalization and ranking.
-   [ ] Connect PHP to Flask with timeout and fallback.
-   [ ] Evaluate results using representative profiles.

## Phase 5 --- Release

-   [ ] Verify hosting supports each runtime.
-   [ ] Configure production DB privately.
-   [ ] Test HTTPS, uploads, authorization, and rollback plan.
