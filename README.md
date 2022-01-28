# Django web app on development

Note: Create a .env for own development environment - .env.dist populated only required env for the web app.

# Prerequisite

- Docker 20.10.7

### Set up the web app for development

1. docker-compose build
2. docker-compose up -d

Helpful commands:

1. docker-compose exec web python manage.py flush --no-input
2. docker-compose exec web python manage.py migrate
