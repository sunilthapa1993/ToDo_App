# ToDo Application - REST API Documentation

This is the documentation of REST APIs for a ToDo Application.

The entire application is built using Django Framework.

Please follow the below steps in windows terminal for running the application.

## Clone repository

    git clone https://github.com/sunilthapa1993/Bytive_Assignment.git

## Change to project directory

    cd Bytive_Assignment

## Run migrations

    python manage.py migrate

## Run server

    python manage.py runserver

Open chrome and enter below URL to access the API endpoints: 

    http://127.0.0.1:8000/tasks/

The REST API endpoints to the Todo application is described below.

## Create a new Task

### Request

`POST /tasks/`

    curl --location 'http://127.0.0.1:8000/tasks/' \
    --header 'Content-Type: application/json' \
    --data '{
    "title": "Purchase Shoes",
    "description": "Order new shoes from online store"
    }'

### Response

    HTTP/1.1 201 Created
    Date: Sun, 05 Jan 2025 15:54:54 GMT
    Server: WSGIServer/0.2 CPython/3.12.6
    Content-Type: application/json
    Vary: Accept, Cookie
    Allow: POST, OPTIONS, GET
    X-Frame-Options: DENY
    Content-Length: 102
    X-Content-Type-Options: nosniff
    Referrer-Policy: same-origin
    Cross-Origin-Opener-Policy: same-origin
     
    {"id":3,"title":"Purchase Shoes","description":"Order new shoes from online store","status":"Pending"}

## Get list of Tasks

### Request

`GET /tasks/`

    curl --location 'http://127.0.0.1:8000/tasks'

### Response

    HTTP/1.1 200 OK
    Date: Sun, 05 Jan 2025 16:03:14 GMT
    Server: WSGIServer/0.2 CPython/3.12.6
    Content-Type: application/json
    Vary: Accept, Cookie
    Allow: POST, OPTIONS, GET
    X-Frame-Options: DENY
    Content-Length: 212
    X-Content-Type-Options: nosniff
    Referrer-Policy: same-origin
    Cross-Origin-Opener-Policy: same-origin
     
    [{"id":1,"title":"Get Milk","description":"Got to the grocery store and buy some milk","status":"Completed"},        {"id":3,"title":"Purchase Shoes","description":"Order new shoes from online store","status":"Pending"}]

## Get task by ID

### Request

`GET /tasks/:id`

    curl --location 'http://127.0.0.1:8000/tasks/3'

### Response

    HTTP/1.1 200 OK
    Date: Sun, 05 Jan 2025 16:08:15 GMT
    Server: WSGIServer/0.2 CPython/3.12.6
    Content-Type: application/json
    Vary: Accept, Cookie
    Allow: DELETE, PUT, OPTIONS, GET
    X-Frame-Options: DENY
    Content-Length: 102
    X-Content-Type-Options: nosniff
    Referrer-Policy: same-origin
    Cross-Origin-Opener-Policy: same-origin
     
    {"id":3,"title":"Purchase Shoes","description":"Order new shoes from online store","status":"Pending"}

## Update Task by ID

### Request

`PUT /tasks/:id`

    curl --location --request PUT 'http://127.0.0.1:8000/tasks/3/' \
    --header 'Content-Type: application/json' \
    --data '{
        "title": "Purchase Shoes",
        "description": "Order new shoes from online store",
        "status": "Completed"
    }'

### Response

    HTTP/1.1 200 OK
    Date: Sun, 05 Jan 2025 16:10:26 GMT
    Server: WSGIServer/0.2 CPython/3.12.6
    Content-Type: application/json
    Vary: Accept, Cookie
    Allow: DELETE, PUT, OPTIONS, GET
    X-Frame-Options: DENY
    Content-Length: 104
    X-Content-Type-Options: nosniff
    Referrer-Policy: same-origin
    Cross-Origin-Opener-Policy: same-origin
     
    {"id":3,"title":"Purchase Shoes","description":"Order new shoes from online store","status":"Completed"}

## Delete Task by ID

### Request

`DELETE /tasks/:id/`

    curl --location --request DELETE 'http://127.0.0.1:8000/tasks/4/'

### Response

    HTTP/1.1 204 No Content
    Date: Sun, 05 Jan 2025 16:11:51 GMT
    Server: WSGIServer/0.2 CPython/3.12.6
    Vary: Accept, Cookie
    Allow: DELETE, PUT, OPTIONS, GET
    X-Frame-Options: DENY
    Content-Length: 0
    X-Content-Type-Options: nosniff
    Referrer-Policy: same-origin
    Cross-Origin-Opener-Policy: same-origin
