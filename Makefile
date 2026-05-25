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

.PHONY: network-ls
network-ls:
	docker network ls

.PHONY: network-inspect-backend
network-inspect-backend:
	docker network inspect bookstore_backend

.PHONY: network-inspect-frontend
network-inspect-frontend:
	docker network inspect bookstore_frontend
