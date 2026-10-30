# Coding Agent Rules

-   Inspect the real repository before changing code; source code and
    schema are the source of truth.
-   Do not invent files, routes, columns, credentials, features, or test
    results.
-   Make small, scoped changes and preserve working PHP flows.
-   Use prepared SQL statements, escape output, validate inputs, and
    handle errors safely.
-   Use `password_hash()` and `password_verify()`; protect sessions and
    regenerate session IDs after login.
-   Public registration should allow only `student` and `employer`; do
    not let users self-register as admin.
-   Enforce admin-only job posting and application-status changes on the
    server, not merely by hiding buttons.
-   Validate uploaded file type, size, and generated filename.
-   Treat the Python ML API as optional unless verified in the repo; PHP
    browsing should work if it is offline.
-   Never commit secrets, passwords, tokens, `.env` files, or dependency
    folders.
-   Run syntax checks and describe how each change was tested.
-   If schema changes are needed, provide a migration/SQL and recommend
    a backup first.
