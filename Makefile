.PHONY: migrate
migrate:
	docker-compose exec web python manage.py migrate --noinput

.PHONY: up
up:
	docker-compose up -d --build

.PHONY: down
down:
	docker-compose down

.PHONY: logs
logs:
	docker-compose logs -f

.PHONY: shell
shell:
	docker-compose exec web python manage.py shell
