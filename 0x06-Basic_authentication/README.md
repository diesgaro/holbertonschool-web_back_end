# 0x06. Basic authentication

In this project, you will learn what the authentication process means and implement a Basic Authentication on a simple API.

## Resources

* https://www.youtube.com/watch?v=501dpx2IjGY
* https://docs.python.org/3.7/library/base64.html
* https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Authorization
* https://palletsprojects.com/p/flask/
* https://en.wikipedia.org/wiki/Base64
* https://flask.palletsprojects.com/en/1.1.x/patterns/errorpages/
* https://flask.palletsprojects.com/en/1.1.x/api/#flask.Blueprint.before_request

## Learning objectives

* What authentication means
* What Base64 is
* How to encode a string in Base64
* What Basic authentication means
* How to send the Authorization header

## Tasks

### 0. Simple-basic-API 
### 1. Error handler: Unauthorized 
### 2. Error handler: Forbidden
### 3. Auth class 
### 4. Define which routes don't need authentication
### 5. Request validation! 
### 6. Basic auth 
### 7. Basic - Base64 part 
### 8. Basic - Base64 decode 
### 9. Basic - User credentials
### 10. Basic - User object 
### 11. Basic - Overload current_user - and BOOM! 
### 12. Basic - Allow password with ":" 
### 13. Require auth with stars 

---

## Simple API

Simple HTTP API for playing with `User` model.


### Files

#### `models/`

- `base.py`: base of all models of the API - handle serialization to file
- `user.py`: user model

#### `api/v1`

- `app.py`: entry point of the API
- `views/index.py`: basic endpoints of the API: `/status` and `/stats`
- `views/users.py`: all users endpoints


### Setup

```
$ pip3 install -r requirements.txt
```


### Run

```
$ API_HOST=0.0.0.0 API_PORT=5000 python3 -m api.v1.app
```


### Routes

- `GET /api/v1/status`: returns the status of the API
- `GET /api/v1/stats`: returns some stats of the API
- `GET /api/v1/users`: returns the list of users
- `GET /api/v1/users/:id`: returns an user based on the ID
- `DELETE /api/v1/users/:id`: deletes an user based on the ID
- `POST /api/v1/users`: creates a new user (JSON parameters: `email`, `password`, `last_name` (optional) and `first_name` (optional))
- `PUT /api/v1/users/:id`: updates an user based on the ID (JSON parameters: `last_name` and `first_name`)