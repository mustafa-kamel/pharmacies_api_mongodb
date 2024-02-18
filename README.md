# Pharmacies API MongoDB

This project is a simple Django REST API that integrates MongoDB as the main database. It implements CRUD operations on a Pharmacies collection.

## Features
- MongoDB database to store pharmacy documents 
- Django REST Framework to build the RESTful API
- djongo MongoDB adapter to connect Django and MongoDB
- Basic authentication for API endpoints
- API documentation using OpenAPI/Swagger
- API testing

## Setup
### Prerequisites
- Python >= 3.8
- Django
- Django Rest Framework
- MongoDB

### Steps
1. Clone the repo `git@github.com:mustafa-kamel/pharmacies_api_mongodb.git`
2. Create a virtual environment `python -m venv venv`
3. Activate virtual environment `source venv/bin/activate`
4. Install dependencies: `pip install -r requirements.txt`
5. Copy the `.env.example` file to `.env` run `cp .env.example .env`
6. Update the variables in `.env` file according to your configurations.
7. Apply migrations: `python manage.py migrate`
8. Create a superuser: `python manage.py createsuperuser`
9. Run the server: `python manage.py runserver`

## Database 
The project uses MongoDB as the backend database. Make sure MongoDB is installed locally and running on port 27017.

Create a local MongoDB database called `pharmacies` from MongoDBCompass or from shell using:

```bash
mongosh
use pharmacies
```

> If you want to use a cloud database instead you will need to add its configuration to the project settings file.


### Environment Variables
Make sure to set the following environment variables in `.env`:
- `MONGO_DB`: The mongodb name.
- `SECRET_KEY`: Django secret key.
- `DEBUG`: Set to `True` for development, `False` for production.


## Creating New User
- Use the Django admin interface or the API endpoint `/api/users/` to create a new user, Or you can do that simply from the django shell:
```bash
python manage.py shell
```

Then you need to create a new user using this code:
```python
from django.contrib.auth.models import User
User.objects.create_user(username="USERNAME", password="USER_PASSWORD")
```

These user credentials will be used for basic authentication.


## Running the API
- Use the Django development server to run the API: `python manage.py runserver`
- Access the API at `http://localhost:8000/pharmacies/`


## Running Tests
- Use pytest to run tests: `coverage run -m pytest`.
- Generate coverage report: `coverage report` or `coverage html` for HTML report that shows a 99% test coverage.


## API Documentation
- API documentation is available at http://localhost:8000/api/schema/swagger-ui/ or http://localhost:8000/api/schema/redoc/ once the server is running.
- Also check the project's Postman collection for a comprehensive API documentation, including request examples; also you can select the `pharmacies` environment and run the Postman collection to validate its functionality.

[<img src="https://run.pstmn.io/button.svg" alt="Run In Postman" style="width: 128px; height: 32px;">](https://app.getpostman.com/run-collection/1861377-d0deee14-feba-47fd-8810-b6f56cd65c84?action=collection%2Ffork&source=rip_markdown&collection-url=entityId%3D1861377-d0deee14-feba-47fd-8810-b6f56cd65c84%26entityType%3Dcollection%26workspaceId%3Df1fa4edc-8602-4006-bfa5-78678901d698)
