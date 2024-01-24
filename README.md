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
- Python 3.8 or above
- MongoDB
- Pip

### Steps
1. Clone the repo
   ```bash
   git clone https://github.com/mustafa-kamel/pharmacies_api_mongodb.git
   ```
2. Create a virtual environment
   ```bash
   python -m venv venv  
   ```
3. Activate virtual environment
   ```bash
   source venv/bin/activate
   ```
4. Install requirements
   ```
   pip install -r requirements.txt
   ```
   
## Database 
The project uses MongoDB as the backend database. Make sure MongoDB is installed locally and running on port 27017.

Create a local MongoDB database called `pharmacies` from MongoDBCompass or from shell using:

```bash
mongosh
use pharmacies
```

> If you want to use a cloud database instead you will need to add its configuration to the project settings file.


## Environment Variables
Copy the `.env.example` file to `.env` and configure:
```bash
cp .env.example .env
```

- MONGO_DB = pharmacies


## Creating New User
To be able to run the API you need to create a new user, you can do that simply from the django shell:
```bash
python manage.py shell
```

Then you need to create a new user using this code:
```python
from django.contrib.auth.models import User
User.objects.create_user(username="mk", password="password")
```

This user credentials will be used for basic authentication.


## Running the API
```
python manage.py runserver
```

The API will be available at http://localhost:8000/pharmacies/

## API Documentation
API docs are available at http://localhost:8000/api/schema/swagger-ui/ or http://localhost:8000/api/schema/redoc/ once the server is running.


For full API Documentation for the API along with examples, you can run this postman collection and make sure you select the pharmacies envoirnment:

[<img src="https://run.pstmn.io/button.svg" alt="Run In Postman" style="width: 128px; height: 32px;">](https://app.getpostman.com/run-collection/1861377-d0deee14-feba-47fd-8810-b6f56cd65c84?action=collection%2Ffork&source=rip_markdown&collection-url=entityId%3D1861377-d0deee14-feba-47fd-8810-b6f56cd65c84%26entityType%3Dcollection%26workspaceId%3Df1fa4edc-8602-4006-bfa5-78678901d698)


Also the postman collection contains tests for the requests, you can run the collection to validate it's working fine.


## Testing
Run the test cases using pytest with:
```bash
pytest
```
Or using coverage with:

```bash
coverage run -m pytest
```

The test coverage is 99%, you can view that in console after running the previous command with:

```bash
coverage report
```
Or you can generate an interactive version of it that you can open in your browser with:

```bash
coverage html
```
