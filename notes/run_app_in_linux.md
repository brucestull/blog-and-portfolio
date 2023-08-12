# Run Application in Linux (WSL Ubuntu)

## Resolve `psycopg2` Issue

1. `sudo apt-get update`
1. `sudo apt-get install libpq-dev`
1. `pipenv install psycopg2`

## Commands

1. `cp Pipfile.linux Pipfile`
1. `rm Pipfile.lock`
1. `pipenv install`
1. `pipenv shell`
1. `pip list`
1. `python manage.py makemigrations`
1. `python manage.py migrate`
1. `python manage.py createsuperuser --email FlynntKnapp@email.app --username FlynntKnapp`
1. `python manage.py runserver`
