# Database Reference

Local database name discussed: `job_in_india`. Production credentials
must be stored privately, never in Git or documentation.

## `users`

Known columns: `id`, `name`, `email` (unique), `password` (hash), `role`
(`student`/`employer`/`admin`), `phone`, `skills`, `education`,
`created_at`.

## `jobs`

Known columns: `id`, `title`, `company`, `location`, `description`,
`salary`, `employer_id`, `created_at`.

## `applications`

Known columns: `id`, `user_id`, `job_id`, `resume`, `status`
(`Applied`/`Shortlisted`/`Selected`/`Rejected`), `applied_at`.

Intended relationship: users and jobs each have many applications. A
unique constraint on `(user_id, job_id)` can prevent duplicate
applications. Confirm exact schema with `SHOW CREATE TABLE table_name;`
before changes and back up data first.
