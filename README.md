# Optimo Development Microservice


To run the microservice you need to build image of the current code repository first.
You can do it by executing the following *docker* command:

`docker build . --tag abirek-optimo-development:1.0`

The output image name and tag will be *abirek-optimo-development:1.0*.
You can change it but then you need to change it also in the *docker-compose.yaml* file 
in *api*, *ingest* and *generator* sections.

After the image is successfully built you can start the microservice by executing
the following command:

`docker-compose up -d`

It will take a short while to have the *mysql* and *rabbitmq* services set up. 
Once the microservice is up and running you can get currently generated fibonacci numbers
by sending a HTTP GET request to the endpoint: 

`http://127.0.0.1:5000/numbers`

for example using the *curl* tool.

By default Fibonacci numbers are generated every 30 seconds. 
You can change it by setting a different value of the GENERATOR_DELAY environment variable
in *generator* section of *docker-compose.yaml* file.

If you want to stop the microservice just execute:

`docker-compose stop`

To start the microservice once again execute

`docker-compose start`