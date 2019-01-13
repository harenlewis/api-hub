## API HUB - FreightBro
-----

This project was built for the FreightBro coding assignment.

A mock server application where dummy APIs can be created and
accessed by multiple users. Built using [Django Web Framework](https://www.djangoproject.com/ "Django"),  [DRF](https://www.django-rest-framework.org/ "Django Rest Framework").

### Steps to run the project
 **(Note: Requires python3)**

 1. Clone the respository
    
    $ `git clone https://github.com/harenlewis/api-hub.git`

    and 
    
       `cd api_hub`
 
 2. Create a virtual envirnoment and activate it.
 
       `virtualenv -p python3 envname`
        `source envname/bin/active`

 3. Install requirements and dependencies.
    
       ` pip install -r requirements.txt`  

 4. Run database migrations.

       `python manage.py migrate`  

4. Create a superuser using the following command. Please note the username and password as this is admin user: 
       `python manage.py createsuperuser`

 5. Run server

       `python manage.py runserver`

The API can be tested using [Postman](https://www.getpostman.com/ "Postman").


**POST /api/v1/register**
- Request Data:
    - `username: string`
    - `email: string`
    - `password: string`

- Response: Return user token for future API calls.
    - `{ 58fb9cf9f2d88ca678aa34407d9d22b761c36bd6 }`
-----
**POST /api/v1/login**
- Request Data:
    - `username: string`
    - `password: string`


- Response: Returns user token for future API calls.
    - `{ 58fb9cf9f2d88ca678aa34407d9d22b761c36bd6 }`

**This token is requires for future API calls.**

**POST /api/v1/projects**

- Header:
    -   `Authorization: Token <token>`

- Request Data:
    - `name: string`

- Response: Returns project data.
    - ```
        "id": 78,
        "name": "Dummy Proj",
        "uuid": "8e767e81-1cb7-40b2-87aa-ad359a43c4e4",
        "created_by": "John Doe",
        "created_at": "2019-01-14T23:08:20",
        "modified_by": "John Doe",
        "modified_at": "2019-01-14T23:08:20",
        ```

**POST /api/v1/projects/:project_id**

- Header:
    -   `Authorization: Token <token>`

- Request Data:
    - `path: string`
    - `method: integer`
    - `res_type: integer`
    - `res_body: string`

- Response: Returns project data.
    - ```
        "id": 78,
        "project": "Dummy Project",
        "path": "some/path",
        "method": 100,
        "res_type": 600,
        "res_body": "<p>Hey there</p>",
        "created_by": "John Doe",
        "created_at": "2019-01-14T23:08:20",
        "modified_by": "John Doe",
        "modified_at": "2019-01-14T23:08:20"
        ```
##### Project API's are accessible through project's UUID.
**GET | POST | PUT | DELETE**

**`http://<project_uuid>localhost:8000/api/v1/mock/`**

- Append API path to above url. For eg taking above data:
    -   `http://8e767e81-1cb7-40b2-87aa-ad359a43c4e4.localhost:8000/api/v1/mock/some/path`       

- Request Data:
    - None
- Response: Returns saved API response from DB.