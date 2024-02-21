migrate:
	python manage.py makemigrations
	python manage.py migrate
	DJANGO_SUPERUSER_USERNAME=admin DJANGO_SUPERUSER_EMAIL=admin@example.com DJANGO_SUPERUSER_PASSWORD=password python manage.py createsuperuser --noinput

celery:
	celery -A weops_lite worker -B --loglevel=info

win-celery-worker:
    celery -A weops_lite worker --loglevel=info

win-celery-beat:
    celery -A weops_lite beat --loglevel=info

celery-inspect:
    celery -A weops_lite inspect scheduled

celery-flower:
    celery -A weops_lite flower

run:
	daphne -b 0.0.0.0 -p 8000 weops_lite.asgi:application

test:
	pytest --cov --cov-report html

show_test_result:
	allure serve ./allure-results

collectstatic:
    python manage.py collectstatic --noinput

keycloak_init:
	python ./manage.py keycloak_init


bdd_test:
	DJANGO_SETTINGS_MODULE=weops_lite.settings  behave ./apps/system_mgmt/features