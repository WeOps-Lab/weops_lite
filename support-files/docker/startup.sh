python manage.py migrate
python manage.py createsuperuser --noinput
daphne -b 0.0.0.0 -p 8000 weops_lite.asgi:application