#### to run scale up your application to n intances use the command:
- docker-compose up --scale app=5


#### in this 
services:
  app:
    build:
      context: .
    ports:
      - ":5000"
                                                                                                                                          

No host port specified → Docker will automatically assign a random available port on the host machine and map it to port 5000 inside the container.