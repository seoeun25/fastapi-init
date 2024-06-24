# fastapi-init
FastAPI Skeleton Project 

## Project Structure

```
├── .github/
├── coverage/
├── app/ 
├     ├── api/
├     ├── models/               
├     ├── config/
├     ├── server.py                     # Our main app server
├── tests/
├── main.py                             # Docker entry point. uvicorn run.
├── Dockerfile                          # Docker configuration file for backend application
├── README.md                           # Documentation for app

```

## How to deploy

### dev
* develop branch 에 push되면, 즉 feature branch 작업을 develop 에 merge 하면 dev 인프라에 배포된다.

### stg
* release/xxx 브랜치가 생성되면 stg 인프라에 배포된다.
* release/{data} 형식, 예를 들면 release/2024.5.28 브랜치를 push 하면 이 브랜치 기준으로 stg에 배포된다.
* Docker image 는 latest가 된다.

## How to start 

Local에서 API Server 를 실행하는 방법

1. Start the app

STACK=local
```
## docker build
$ docker build . --build-arg VERSION=$(date +%Y%m%d) --build-arg STACK=local -t fastapi-init

## run a container
$ docker run -d -p 80:80 fastapi-init

```


2. 확인 

health: http://localhost

```
$ curl -X GET 'http://localhost' -H 'Content-Type: application/json

$ curl -X GET 'http://localhost/v1/message/hello' -H 'Content-Type: application/json'

$ curl -X POST 'http://localhost/v1/message/items' -H 'Content-Type: application/json' -d '{ "name":"iPad", "description": "10 inch" }'

```

## Demo
Swagger: http://localhost/swagger

