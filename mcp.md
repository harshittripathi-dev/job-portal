# MCP / External Tool Integrations

No specific MCP integration is confirmed as implemented. This document
is a future design note.

Possible controlled tools: search jobs, read a candidate's own
application status, create admin-approved job listings, or produce
aggregate reports.

Security requirements: - Authenticate and authorize every sensitive
tool. - Apply least privilege and validate arguments. - Never expose
credentials, password hashes, session tokens, or resumes by default. -
Require confirmation for destructive or externally visible actions. -
Add rate limits, timeouts, and audit logging without secrets. - Keep
business rules in a reusable service layer instead of duplicating SQL
inside each tool.

Before implementation, document server runtime, transport,
authentication, tool schemas, permissions, and tests.
