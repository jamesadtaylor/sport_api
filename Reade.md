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

