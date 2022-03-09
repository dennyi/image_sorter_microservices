# About
Project consists of 3 microservices and a library of shared packages.

## Microservices:
    1. image_loader
        Periodically checks for images inside \storage\new , when there
        are any, validates them, moves them to a folder queue and notifies image_processor
        by sending a message through NATS message broker. When there are any files present
        in the folder that are not valid images, deletes these files.
    2. image_processor
        Waits for a message from image_loader about a new image being ready for processing
        inside \storage\queue folder, computes the average color of that image and sends
        a message to image_sorter, containing the name of the image and the average color
    3. image_sorter
        Waits for a message from image_processor, then picks up the image from the queue folder,
        calculates a closest web_color to the average color of that image and moves the image
        to a corresponding folder inside a \storage\sorted folder.

Each microservice contains two separate env files, src\\.env is used for local environment,
when building a docker image, .env gets overwritten by .env_container.


## Shared packages
Folder libs contains multiple packages, which are installed localy 
using pip when building a service docker image. This prevents code duplication without the
need to push these packages to a remote repository.

# Prequisities
    1. docker installed and running
    2. docker-compose installed
# Installation
## Local environment
    1. Install all dependencies:
        - pip install -r requirements_dev.txt
    2. Run tests:
        - cd .\src\
        - python -m unittest discover tests
    3. run a microservice:
        - set a NATS server url in \src\\{service_name}\src\\.env
        - cd .\src\\{service_name}\src
        - python .


## Build and launch containers
docker-compose up

