# ATLAN CHALLENGE

## Introduction

The project is developed a solution to the Atlan challenge. Find the challenge statement [here](https://docs.google.com/document/d/1wma52BMH-07BOxpqWzqIUW5uKIXaCj0j6gPftiwLobE/edit).

## Approach

### Tech Stack

- Python
- Flask

## Project Architecture

### API Endpoints

The projects has been developed as a REST API. The various functionalities has been exposed as endpoints in the `/api/api.py` file.

The various endpoints are :

- `GET /status` : To get the current status of active procees, if it exists.

- `POST /create` : To start a new process, create a POST Request at this endpoint along with the CSV file in form data, with `file` as key.

- `GET /pause` : To pause the in-progress running process, create a POST Request at this endpoint.

- `GET /resume` : To resume the in-progress paused process, create a POST Request at this endpoint.

- `GET /stop` : To terminate the in-progress paused/running process, create a POST Request at this endpoint.

#### Handler

The `api.py` uses a Handler object to handle the process associated with the various endpoints. The Handler consist of implementation of corresponding functionality of the endpoints.

The Handler also keeps track of the current/last active process and ensures that only one file is processed at any given time. This has been implemented with inspiration from Singleton class of OOPS.

#### Process Thread

The process thread performs the actual processing on the CSV file. The `run` function is the target function for every thread. The logic for processing the CSV file must be implemented in the `run` function.

## Getting Started

### Installation

Please clone the repository and follow one of the following deployment method.

#### Docker

The project can be directly run in a container environment using the docker image.

Steps:

- Build the image
```
  docker build -t atlan-flask:latest . 
```
- Run the image in a container
```
  docker run -it  -d -p 5000:5007 atlan-flask
```
Here the ports 5000 and 5007 corresponds to the local and container port respectively.


#### Local Setup

The project can also run on the local environment.

Steps:

- Install the requirements
```
pip install -r requirements.txt
```
- Start the app
```
python3 ./api/api.py
```
