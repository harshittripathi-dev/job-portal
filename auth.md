# Authentication and Authorization

The known design uses PHP sessions and hashed passwords
(`password_hash()` / `password_verify()`).

  Action                      Intended access
  --------------------------- -----------------------------------------
  Browse public jobs          Public
  Register/login              Public
  Apply for a job             Authenticated student
  View own applications       Authenticated student, own records only
  Post a job                  Admin only under the current policy
  Change application status   Admin only under the current policy

Public registration should allow only `student` and `employer`. Never
trust a role submitted by the browser. Check authorization in each
protected PHP handler. Regenerate session ID after login, destroy
session on logout, and use secure cookie settings over HTTPS. Password
reset is not confirmed as implemented.
