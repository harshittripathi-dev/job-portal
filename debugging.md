# Debugging

## PHP server

``` bash
php -v
php -S localhost:8000
```

If `php` is not recognized, install PHP or fix PATH. If port 8000 is
busy, use another port.

## Git says "not a git repository"

Run `pwd` and `ls -la`. Move to the actual repo root or run `git init`
only if this folder is intended to become a new repository. Check the
remote and existing history before pushing.

## Database errors

Check MySQL is running and verify host, database, username, and
password. Never expose production credentials in screenshots or commits.

## Upload errors

Check `uploads/resumes/` exists and is writable, PHP upload limits,
allowed file types, and `$_FILES` error code. Do not trust original
filenames.

## Checks

``` bash
php -l jobs.php
php -l login.php
php -l register.php
python -m py_compile system.py api.py
```

Run only checks for files that exist. If `get_result()` fails on
hosting, verify mysqlnd availability before switching to
`store_result()` / `bind_result()`.
