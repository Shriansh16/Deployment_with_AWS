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

#### now we will deploy it to ec2 server and literaaly we will use only this code in ec2

#### now create an instance and connect it to the vscode using the same old method, here is the command:

ssh -i "C:\Users\Shrian Singh\.ssh\sheenu.pem" ubuntu@<public ip of instance>

- now use old technique of connecting you vscode to ec2 instance.
- create a new directory and code .
- create a new file "docker-compose.yml" and paste the entire few lines of code that are provided here.
- install docker extension
- from docker-compose.yml file, remove aws wala part because our ec2 instance is already connected with s3 bucket
- now install docker-compose, using this command
"sudo apt install docker-compose"


#### before moving ahead, do one thing add the latest version of docker using these commands
1. sudo apt-get remove docker docker-engine docker.io containerd runc
2. sudo apt-get update
3. sudo apt-get install docker.io
4. sudo systemctl start docker
5. sudo systemctl enable docker
6. sudo usermod -aG docker $USER
7. sudo systemctl status docker (to check whether it is running or not)

#### if you are using private docker repo, then authentication is required, "docker login" else not needed
- now use the command
- docker-compose up
#### you can also scale your application using this command
- docker-compose up --scale app=2

Purpose: It starts your Docker Compose setup and scales the service named app to 2 running instances (containers).

🔍 Why use it?
Load Balancing: Run multiple instances of a service to handle more traffic.
High Availability: If one container fails, others can continue running.
Parallel Processing: Useful for microservices or tasks that can run in parallel.