# Todo API - Built to productive front-end developers

## Built using
- Django Rest Framework
- JWT Authentication
- Swagger
- PostgreSQL

## Available actions
- Create, Update, Read and Delete [Tasks]
- Create [Users]
- Authentication and Refresh token [Users]
- Admin Panel

## API Documentation
http://localhost:8000/api/docs/

## Setup dev environment
Copy env file:
```bash
cp .env.sample .env
```

With Docker and Docker Compose installed, run:
```bash
docker-compose up --build
# Just in first time, next run: docker-compose up
```

API available on:
- http://localhost:8000/api/docs

Admin available on:
- http://localhost:8000/admin
```
user: admin 
pass: 123
```
