up_prod:
	docker-compose -f docker-compose.prod.yml up -d --build
static_prod: up_prod
	docker-compose -f docker-compose.prod.yml exec web python manage.py collectstatic --no-input --clear
run_prod: static_prod
	docker-compose -f docker-compose.prod.yml exec web python manage.py createsuperuser


up_dev:
	docker-compose up -d --build
static_dev: up_dev
	docker-compose -f docker-compose.yml exec web python manage.py collectstatic --no-input --clear
run_dev: static_dev
	docker-compose -f docker-compose.yml exec web python manage.py createsuperuser


stop_prod:
	docker-compose -f docker-compose.prod.yml down -v
stop_dev:
	docker-compose -f docker-compose.yml down -v

migrate_dev: up_dev
	docker-compose -f docker-compose.yml exec web python manage.py migrate --noinput
migrate_prod: up_prod
	docker-compose -f docker-compose.prod.yml exec web python manage.py migrate --noinput
new_migration_dev: up_dev
	docker-compose -f docker-compose.yml exec web python manage.py makemigrations