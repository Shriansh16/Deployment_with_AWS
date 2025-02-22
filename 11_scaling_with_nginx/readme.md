1. image:: Uses the latest official NGINX Docker image from Docker Hub.
2. volumes::
Maps a local configuration file (nginx.conf) to the container’s default NGINX configuration path (/etc/nginx/nginx.conf).
The :ro means read-only, so NGINX can read the file but not modify it.
3. depends_on:: Ensures that the app service starts before the NGINX service starts.
4. ports::
"80:80" means:
5. Exposes port 80 on the host machine (default HTTP port).
6. Maps it to port 80 inside the NGINX container.
7. You can access your application at http://localhost after starting the container.

## How Does It Work Together?
1. The app runs on port 5000 inside its container.
2. The NGINX container listens on port 80 and forwards requests to the app service.
3. Users access the app through NGINX by visiting http://localhost, and NGINX routes the requests internally to the app running on port 5000.

## Purpose of NGINX in This Setup
NGINX is acting as a load balancer. Here's why it's essential:

1. Distributes Traffic Evenly

When multiple instances of your app are running, NGINX will distribute incoming HTTP requests across all 5 containers.
This helps balance the load, preventing any single instance from being overwhelmed.
2. Single Access Point

Instead of accessing different ports for each container, NGINX provides a single entry point (http://localhost:80).
It handles routing and forwards requests to the available app containers running on port 5000.
3. Improves Reliability

If one app instance crashes, NGINX can route traffic to the remaining active instances.
This setup makes your application more fault-tolerant.
4. Scalability

You can easily scale the number of app containers without changing how clients interact with your app.
Just update the number of replicas, and NGINX will automatically distribute traffic to all running instances.


#### how is this possilbr? how can we run muliple things on a single port

Docker’s Internal DNS

When you scale your app using Docker Compose (--scale app=5), Docker assigns different internal IPs to each instance.
NGINX uses these internal IPs (like app:5000) to communicate with all instances, even though from the outside, you’re still just hitting http://localhost:80.


## Full Explanation of nginx.conf
1. events {
    worker_connections 1000;
}

events Block
Manages how NGINX handles connections.
worker_connections 1000; means that each worker process can handle up to 1000 simultaneous connections.
This setting is useful for high-traffic websites since it controls how many clients NGINX can handle at the same time.


2. http {
    server {
        listen 80;

        location / {
            proxy_pass http://app:5000;
        }
    }
}


 - http Block
Handles all HTTP-related configurations, such as setting up servers, handling requests, and defining routes.
- 🔒 server Block
Defines a virtual server that handles incoming HTTP requests.
- listen 80;

Tells NGINX to listen for incoming HTTP requests on port 80 (the default port for HTTP).
When you visit http://localhost, this is the port NGINX is listening to.
- location / { ... }

Specifies how to handle requests that match a particular path.
In this case, / means any request that comes to the root URL (like http://localhost/).
- proxy_pass http://app:5000;

This line tells NGINX to forward incoming requests to the service named app running on port 5000.
Docker Compose automatically creates an internal DNS name (app here) that resolves to one of the app containers.
This is the reverse proxy magic—NGINX receives the request on port 80 and passes it to an app container on port 5000.