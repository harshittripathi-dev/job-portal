# Testing Plan

## Accounts

-   [ ] Student registration and employer registration work if
    supported.
-   [ ] Public registration cannot create admin.
-   [ ] Duplicate email and incorrect password are rejected.
-   [ ] Logout ends the session and protected pages require login.

## Jobs

-   [ ] Listing loads with and without filters.
-   [ ] Search, sort, and filter parameters are validated.
-   [ ] Empty results and invalid job IDs are handled.
-   [ ] All job links point to valid routes.

## Applications

-   [ ] Student can apply to a valid job.
-   [ ] Invalid job IDs and duplicate applications are handled.
-   [ ] Invalid/oversized resumes are rejected.
-   [ ] Students can see only their own applications.
-   [ ] Only authorized admins can change application status.

## Optional API

-   [ ] Health endpoint works if implemented.
-   [ ] Valid, empty, and malformed requests are handled.
-   [ ] Response keys match the frontend contract.
-   [ ] PHP still works when the API is unavailable.

## Static checks

``` bash
php -l login.php
php -l register.php
php -l jobs.php
php -l upload.php
python -m py_compile system.py api.py
```

Run checks only for files present. Record environment, date, result, and
defects. Never mark untested cases as passed.
