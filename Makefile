run:
	python app/manage.py runserver 0.0.0.0:8000

migrate:
	python app/manage.py migrate

makemigrations:
	python app/manage.py makemigrations

shell:
	python app/manage.py shell_plus --print-sql

createsuperuser:
	python app/manage.py createsuperuser

worker:
	cd app && celery -A settings worker -l info --autoscale=0,10

beat:
	cd app && celery -A settings beat -l info
