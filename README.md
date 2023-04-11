# Sticky-Notes

The Sticky-Notes web application is intentionally vulnerable and provides a place for users to create and share notes. The web application uses the Django framework for its backend webserver, and Martor for markdown support.

## Installation

Install sticky-notes webapp using the commands below:

```bash
  git clone https://github.com/Spencey818/sticky-notes-demo.git
  python -m venv .venv
  .venv\Scripts\activate
  python -m pip install -r requirements.txt
  cd stickyNotes
  python manage.py collectstatic (Errors are ok)
  python manage.py runserver 0.0.0.0:8000
```
    
## Acknowledgements

 - [Martor](https://github.com/agusmakmun/django-markdown-editor) - Martor is an open-source Markdown plugin for the Django framework
 - [Django](https://www.djangoproject.com/) - Django is an open-source Python web framework
 - [Jinja2](https://palletsprojects.com/p/jinja/) - Jinja2 is an open-source templating engine for Python

