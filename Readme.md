Without docker:

python manage.py runserver
celery -A timer_project beat -l INFO
celery -A timer_project worker -l INFO

