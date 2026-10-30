# Architecture

``` text
Browser -> PHP pages/forms -> MySQL
                   |
                   +--> optional HTTP request -> Flask API -> TF-IDF/cosine similarity + skill overlap
```

-   **Presentation:** PHP-rendered HTML, CSS, JavaScript.
-   **Application:** registration, login, job discovery, upload,
    applications, status handling.
-   **Data:** MySQL tables for users, jobs, applications.
-   **Optional ML:** Python ranking service; separate process from PHP.

Application flow: student browses jobs -\> selects Apply -\> uploads
resume -\> PHP validates upload -\> application record is stored -\>
student views status.

Treat browser input, uploaded files, and API requests as untrusted. PHP
must enforce authorization server-side. Shared hosting may not support a
persistent Flask service.
