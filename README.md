# sport_api
Basic Python REST API
## The What
Provides a REST endpoint that details the last 5 Leeds United results (http://127.0.0.1:5000/previousfivegames if running locally.) 
![super leeds](https://www.yorkshireeveningpost.co.uk/webimg/QVNIMTE5MTUyNDE2.jpg?width=1024&enable=upscale)

## The How
This is a basic RESTFUL API developed in Python using the Flask framework. 
It utilises one GET endpoint from the the sportsdb API (https://www.thesportsdb.com/api.php), translates the response and then makes 
it available as a JSON payload. Basic swagger documentation has been incorporated, but this needs to be enhanced as it is currently not useful.

## Running Instructions
1. Activate Virtual Environment
2. Run main.py

### Docker Commands
## build image
docker build -t sports_image .

## create container and run on port 5000
docker run --name=sports -d -p 5000:5000 sports_image

## check contents of image
docker run -it sports_image sh

## check which containers are running
docker ps

## check logs for container
docker container logs sports



 
