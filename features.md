# Feature Inventory

## Core capabilities discussed

-   Student/employer registration and login/logout
-   Job listing and search/filtering
-   Job applications with resume upload
-   Personal application history
-   Admin job posting and application-status management under the
    intended policy

## Optional recommendation feature

Proposed approach: normalize skills, represent candidate/job text, use
TF-IDF and cosine similarity, calculate skill overlap, rank jobs, and
explain matched/missing skills. A previously discussed concept was 60%
semantic similarity + 40% skill overlap; verify `system.py` before
documenting that as implemented.

## Possible improvements

Pagination, saved jobs, email notifications, password reset, admin audit
trail, CSRF protection, rate limiting, automated tests, and
accessibility improvements. These are suggestions, not confirmed
features.
