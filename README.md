# Sticky-Notes  DEMO

The Sticky-Notes web application provides a place for users to create and share notes. The web application uses the Django framework for its backend webserver, and Martor for markdown support.

## Environment Variables

To run this project, you will need to add the following environment variables to your .env file

`SECRET_KEY`

## Installation

Install sticky-notes webapp using the commands below:

```bash
  git clone https://github.com/Spencey818/sticky-notes-demo.git
  python -m venv .venv
  .venv\Scripts\activate
  python -m pip install -r requirements.txt
  cd stickyNotes
  python manage.py migrate
  python manage.py runserver
```
    
## Acknowledgements

 - [Martor](https://github.com/agusmakmun/django-markdown-editor)
 - [Django](https://www.djangoproject.com/)
