.PHONY: test celery win-celery-worker win-celery-beat celery-inspect celery-flower generate-swagger

test:
	rm -Rf ./htmlcov && DEBUG=False pytest --cov-config=.coveragerc --cov --cov-report html -s 
	# -n auto 

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

show_test_result:
	allure serve ./allure-results

collectstatic:
	python manage.py collectstatic --noinput

keycloak_init:
	python ./manage.py keycloak_init


bdd_test:
	DJANGO_SETTINGS_MODULE=weops_lite.settings behavex --parallel-processes 4

migrate:
	python manage.py makemigrations
	python manage.py migrate
	DJANGO_SUPERUSER_USERNAME=admin DJANGO_SUPERUSER_EMAIL=admin@example.com DJANGO_SUPERUSER_PASSWORD=password python manage.py createsuperuser --noinput

generate-swagger:
	python manage.py generate_swagger -f yaml swagger.yml
