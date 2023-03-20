# api_final by @smart200481 <Mikhail Sutormin>

### Brief Description

This project API Final Yatube created for publish, update, delete and read of information in the posts and comments.
As well there implemented groups section and followers application posibilities.
Applied features like Django and API, REST Django Framework as permissions, mixins, serializers, filters, viewsets, pagination, routers, serializers, relations, validators, as well applied JWT-token for authentication.


##### For some endpoints and requests methods of the project please refer to here:

###### api/v1/posts/

http://127.0.0.1:8000/api/v1/posts/
**GET-request**

###### Response data example:
[
    {
        "id": 1,
        "author": "smart2004",
        "text": "qwerty",
        "pub_date": "2023-03-18T21:20:28.930072Z",
        "image": null,
        "group": 1
    },
    {
        "id": 2,
        "author": "admin",
        "text": "wertyu",
        "pub_date": "2023-03-18T21:53:43.820866Z",
        "image": null,
        "group": null
    }
]

http://127.0.0.1:8000/api/v1/posts/
**POST-request**

###### Input data example:
{
    "text": "qwerty",
    "group": "1"
}

###### Response data example:
{
    "id": 3,
    "author": "smart2004",
    "text": "qwerty",
    "pub_date": "2023-03-20T22:02:03.986440Z",
    "image": null,
    "group": 1
}


###### api/v1/posts/{id}/

http://127.0.0.1:8000/api/v1/posts/{id}/
**GET-request**

###### Response data example:
{
    "id": 1,
    "author": "smart2004",
    "text": "qwerty",
    "pub_date": "2023-03-18T21:20:28.930072Z",
    "image": null,
    "group": 1
}

http://127.0.0.1:8000/api/v1/posts/{id}/
**PUT-request**

###### Input data example:
{
    "text": "qwerty ytrewq",
    "group": "1"
}

###### Response data example:
{
    "id": 1,
    "author": "smart2004",
    "text": "qwerty ytrewq",
    "pub_date": "2023-03-18T21:20:28.930072Z",
    "image": null,
    "group": 1
}

http://127.0.0.1:8000/api/v1/posts/{id}/
**PATCH-request**

###### Input data example:
{
    "text": "qwerty"
}

###### Response data example:
{
    "id": 1,
    "author": "smart2004",
    "text": "qwerty",
    "pub_date": "2023-03-18T21:20:28.930072Z",
    "image": null,
    "group": 1
}

http://127.0.0.1:8000/api/v1/posts/{id}/
**DELETE-request**

###### Response data example:
[]


#### For further details please refer: http://127.0.0.1:8000/redoc/


### How to lauch the project:

##### Clone repository:

```
git clone git@github.com:smart2004/api_final_yatube.git
```

##### Switch to the folder:

```
cd yatube_api
```

##### Create and activate virtual environment:

```
py -3.9 -m venv venv
```

```
source venv/scripts/activate
```


##### Setup dependencies from requirements.txt file:

```
python -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

##### Apply migrations:

```
python manage.py makemigrations
```

```
python manage.py migrate
```

##### Launch server:

```
python manage.py runserver
```
