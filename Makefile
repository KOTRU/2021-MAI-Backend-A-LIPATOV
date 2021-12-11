up_prod:
	docker-compose -f docker-compose.prod.yml up -d --build
run_prod: up_prod
	docker-compose -f docker-compose.prod.yml exec web python manage.py collectstatic --no-input --clear
fresh_run_prod: run_prod
	docker-compose -f docker-compose.prod.yml exec web python manage.py migrate --noinput
	docker-compose -f docker-compose.prod.yml exec web python manage.py createsuperuser --noinput

up_dev:
	docker-compose up -d --build
static_dev: up_dev
	docker-compose -f docker-compose.yml exec web python manage.py collectstatic --no-input --clear
run_dev: static_dev
	docker-compose -f docker-compose.yml exec web python manage.py createsuperuser --noinput

up_debug:
	docker-compose -f docker-compose.debug.yml up -d --build
stop_debug:
	docker-compose -f docker-compose.debug.yml down -v
	
stop_prod:
	docker-compose -f docker-compose.prod.yml down
stop_dev:
	docker-compose -f docker-compose.yml down -v

migrate_dev: up_dev
	docker-compose -f docker-compose.yml exec web python manage.py migrate --noinput
migrate_prod: up_prod
	docker-compose -f docker-compose.prod.yml exec web python manage.py migrate --noinput
new_migration_dev: up_dev
	docker-compose -f docker-compose.yml exec web python manage.py makemigrations