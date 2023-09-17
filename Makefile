manage_py := docker compose exec -it backend python app/manage.py

run:
	$(manage_py) runserver 0.0.0.0:8000

migrate:
	$(manage_py) migrate

makemigrations:
	$(manage_py) makemigrations

shell:
	$(manage_py) shell_plus --print-sql

createsuperuser:
	$(manage_py) createsuperuser

collectstatic:
	$(manage_py) collectstatic --no-input && \
	docker cp backend:/tmp/static /tmp/static && \
	docker cp /tmp/static nginx:/etc/nginx/static

worker:
	cd app && celery -A settings worker -l info --autoscale=0,10

beat:
	cd app && celery -A settings beat -l info

pytest:
	docker compose exec -it backend pytest ./app/tests --cov=app --cov-report html && coverage report --fail-under=79.4287
