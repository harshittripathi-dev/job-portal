# Setup Guide

## Requirements

PHP with MySQLi, MySQL/MariaDB, Git, browser. Optional Python 3 and pip
for the ML service. XAMPP is one local option on Windows.

## Database

1.  Start MySQL.
2.  Create `job_in_india`.
3.  Import the project's SQL schema.
4.  Configure `config/database.php` for local credentials. Typical XAMPP
    defaults may be `localhost`, `root`, empty password, database
    `job_in_india`; adjust to your installation.

## Start PHP

From the project root:

``` bash
php -v
php -S localhost:8000
```

Open `http://localhost:8000`.

## Optional Python API

If `api.py` and `system.py` exist:

``` bash
python -m venv .venv
.venv\Scripts\activate
pip install flask flask-cors scikit-learn
python api.py
```

Run PHP and Python in separate terminals.

## Git

``` bash
git status
```

If this is genuinely a new repository, use `git init`. Check existing
GitHub history and configure the correct remote before pushing; avoid
blind force-pushes.
