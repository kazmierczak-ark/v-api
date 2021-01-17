# v-api

## Prerequisites:
 - Python (minimal version 3.9.1)
 - docker-compose (local setup)

## Run instructions

* Local setup using docker compose:
```
docker-compose -f utils-dev/docker-compose.yaml up
```
* Swagger available under /spec path (port 8000; container exposing port 8000)
* docker-compose Includes docker setup of InfluxDB 
* V-API ensures existence of bucket/db used (InfluxDB 1.8.3 is in the transition stage of using v2.0 apis on top of 1.8 version which had naming changes)
* JWT token required by V-API can be any plain text - only implemented openapi spec-first enablement of token usage, there are no check
* Left in code: buildspec for aws codepipeline - not finished, not working + helm missing for planned eks deploy