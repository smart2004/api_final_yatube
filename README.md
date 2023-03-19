# api_final

### Brief Description

This project API Final Yatube created for publish, update, delete and read of information in the posts and comments.
As well there implemented groups section and followers application posibilities.


##### For endpoints and requests methods of the project please refer to here:

###### api/v1/posts/

http://127.0.0.1:8000/api/v1/posts/
**GET-request**

http://127.0.0.1:8000/api/v1/posts/
**POST-request**


###### api/v1/posts/{id}/

http://127.0.0.1:8000/api/v1/posts/{id}/
**GET-request**

http://127.0.0.1:8000/api/v1/posts/{id}/
**PUT-request**

http://127.0.0.1:8000/api/v1/posts/{id}/
**PATCH-request**

http://127.0.0.1:8000/api/v1/posts/{id}/
**DELETE-request**


###### api/v1/posts/{post_id}/comments/

http://127.0.0.1:8000/api/v1/posts/{post_id}/comments/
**GET-request**

http://127.0.0.1:8000/api/v1/posts/{post_id}/comments/
**POST-request**


###### api/v1/posts/{post_id}/comments/{id}/

http://127.0.0.1:8000/api/v1/posts/{post_id}/comments/{id}/
**GET-request**

http://127.0.0.1:8000/api/v1/posts/{post_id}/comments/{id}/
**PUT-request**

http://127.0.0.1:8000/api/v1/posts/{post_id}/comments/{id}/
**PATCH-request**

http://127.0.0.1:8000/api/v1/posts/{post_id}/comments/{id}/
**DELETE-request**


###### api/v1/groups/

http://127.0.0.1:8000/api/v1/groups/
**GET-request**


###### api/v1/groups/{id}/

http://127.0.0.1:8000/api/v1/groups/{id}/
**GET-request**


###### api/v1/follow/

http://127.0.0.1:8000/api/v1/follow/
**GET-request**

http://127.0.0.1:8000/api/v1/follow/
**POST-request**


#### api/v1/jwt/create/

http://127.0.0.1:8000/api/v1/jwt/create/
**POST-request**


#### api/v1/jwt/refresh/

http://127.0.0.1:8000/api/v1/jwt/refresh/
**POST-request**


#### api/v1/jwt/verify/

http://127.0.0.1:8000/api/v1/jwt/verify/
**POST-request**


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