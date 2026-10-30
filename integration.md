# PHP + Python Integration

PHP is the primary website. A Flask service can optionally provide job
recommendations.

## Local terminals

PHP:

``` bash
cd "C:/Users/Harshit Tripathi/Desktop/Job In India"
php -S localhost:8000
```

Python, only if `api.py` exists:

``` bash
pip install flask flask-cors scikit-learn
python api.py
```

Previously discussed addresses: PHP `http://localhost:8000`; API
`http://127.0.0.1:5000`.

Flow: PHP obtains relevant candidate/job fields -\> sends minimum
required JSON to Flask -\> Python ranks jobs -\> PHP validates and
displays results. Never send passwords, session IDs, or unnecessary
personal data.

Use timeouts and graceful fallback: users should still browse all jobs
if the API is offline. Verify the hosting platform supports a persistent
Python service before deploying.
