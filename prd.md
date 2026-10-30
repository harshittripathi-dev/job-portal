# Product Requirements Document

## Product

Job In India is a job portal intended to help candidates discover jobs
and apply, while supporting controlled management of job listings and
application statuses.

## Users

-   Student/job seeker: browse jobs, apply, track applications.
-   Employer: use employer features supported by the current code.
-   Admin: manage jobs and application statuses according to policy.

## Functional requirements

1.  Users can register with permitted public roles.
2.  Users can sign in and sign out.
3.  Candidates can browse job listings.
4.  Candidates can submit an application with a resume.
5.  Candidates can view their own applications.
6.  Admins can post jobs and manage application statuses.
7.  Optional recommendation service can rank jobs based on profile/job
    relevance.

## Non-functional requirements

Security, responsive UI, data integrity, maintainability, clear errors,
and privacy-preserving data transfer.

## Success measures

Track application-flow completion, error rate, page responsiveness,
duplicate prevention, and user feedback on recommendation relevance.
Establish a baseline before setting numerical targets.

## Open questions

Verify employer permissions, exact filters, recommendation contract, and
where the optional Python API will run. Do not claim unimplemented
email, payment, password-reset, or resume-parsing features.
