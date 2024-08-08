# 0x02. Session authentication

Simple HTTP API for playing with `User` model.


## Background Context
In this project, you will implement a Session Authentication. You are not allowed to install any other module.

In the industry, you should not implement your own Session authentication system and use a module or framework that doing it for you (like in Python-Flask: Flask-HTTPAuth). Here, for the learning purpose, we will walk through each step of this mechanism to understand it by doing.
### Resources
Read or watch:

- [REST API Authentication Mechanisms - Only the session auth part](https://intranet.alxswe.com/rltoken/oofk0VhuS0ZFZTNTVrQeaQ)
- [HTTP Cookie](https://intranet.alxswe.com/rltoken/peLV8xuJ4PDJMOVFqk-d2g)
- [Flask](https://intranet.alxswe.com/rltoken/AI1tFR5XriGfR8Tz7YTYQA)
- [Flask Cookie](https://intranet.alxswe.com/rltoken/QYfI5oW6OHUmHDzwKV1Qsw)

### `models/`

- `base.py`: base of all models of the API - handle serialization to file
- `user.py`: user model

### `api/v1`

- `app.py`: entry point of the API
- `views/index.py`: basic endpoints of the API: `/status` and `/stats`
- `views/users.py`: all users endpoints


## Setup

```
$ pip3 install -r requirements.txt
```


## Run

```
$ API_HOST=0.0.0.0 API_PORT=5000 python3 -m api.v1.app
```


## Routes

- `GET /api/v1/status`: returns the status of the API
- `GET /api/v1/stats`: returns some stats of the API
- `GET /api/v1/users`: returns the list of users
- `GET /api/v1/users/:id`: returns an user based on the ID
- `DELETE /api/v1/users/:id`: deletes an user based on the ID
- `POST /api/v1/users`: creates a new user (JSON parameters: `email`, `password`, `last_name` (optional) and `first_name` (optional))
- `PUT /api/v1/users/:id`: updates an user based on the ID (JSON parameters: `last_name` and `first_name`)
