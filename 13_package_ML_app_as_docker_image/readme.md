This Docker Compose code runs two containers:

1. app service: Runs a custom application from the Docker image shriansh16/app. It mounts AWS credentials from your local ./.aws directory to /root/.aws inside the container (read-only). This is typically used for authentication with AWS services.

2. nginx service: Runs an NGINX server from the image shriansh16/nginx. It depends on the app service, meaning it will start only after the app is running. It maps port 80 on the host machine to port 80 in the container, making the app accessible via http://localhost.                    

🎯 Overall Purpose
This setup runs a web application (likely needing AWS access) behind an NGINX server, which acts as a reverse proxy, handling incoming HTTP requests and forwarding them to the app.


- To run this, use the command:
- docker-compose up --build

- to run scale the application, use this command:
- docker-compose up --build --scale app=2


## NOW ALL ARE PACKAGED AS A SINGLE PACKAGE
### BEAUTY OF DOCKER