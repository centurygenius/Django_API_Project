# Online Store Inventory and Supplier Management API

## Set up instruction
- Install Python from the official site at https://www.python.org/downloads/ if not already present.
- Clone the repository
- Create a virtual environment
- Install Django
- Create a project using the django-admin tool
- Create an app 
- Install Django Rest Framework - Example: pip install django djangorestframework
## Run migrations using:
       python manage.py makemigrations
       python manage.py migrate
## Start the development server using:
       python manage.py runserver

## API Endpoints
# Items
GET  items/ - Lists all items
POST items/create/ - Creates a new item
GET items/<int:pk>/ - Retrieves an item
PUT items/<int:pk>/ - Updates an item
DELETE items/<int:pk>/ - Deletes an item

# Suppliers
GET suppliers/ - Lists all suppliers
POST suppliers/create/ - Creates a new supplier
GET suppliers/<int:pk>/ - Retrieves a supplier
PUT suppliers/<int:pk>/ - Updates a supplier

### Run the server
Using the toll: python manage.py runserver

### Tool for testing
A tool like the Postman can be used to test the API functionality.
In addition, the Django admin site may also be a good tool to monitor the API. You can also test the funtionality using your browser (Chrome is recommended) as you hit the endpoints. 


