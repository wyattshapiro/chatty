## Purpose

Service to create a custom chatbot indexed on the data you provide it.

## Usage

### Build

1. Install Docker
2. Create an environment file called {bot_name}.env (see .env.example)
3. Move custom data under data/{bot_name}

###  Run
1. In one terminal, create docker container with `docker-compose up -d`
    - Rebuild docker container with `docker-compose up -d --build --force-recreate`
2. In another terminal, start interactive chatbot in your terminal with `docker-compose exec chat python3 chat.py`

### Stop
1. Remove docker container with `docker-compose down --rmi all -v`


## To Do

- store data remotely (GCS, S3)
- deploy on cloud as interactive service (GCP, AWS)
