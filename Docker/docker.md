to make image from container

```sh
docker commit id_container myUbuntuVersion:1.0
```

CRI ▶️ Container Runtime Interface

CNI ▶️ Container Network Interface

CSI ▶️ Container Storage Interface


# ----------------------------- Docker ----------------------------- #

run buld and run your app  
    docker build -t [dockehub_name]/[name_for_image] . 
    docker build -t khaledmohamedatia/app . 

    docker run -itd --name app -p 8087:80 [dockehub_name]/[name_for_image]
    docker run -itd --name app -p 8087:80 khaledmohamedatia/app


run jenkins container
    docker run -itd  --name jenkins -v /path/you want to map/:/var/jenkins_home:Z -v /var/run/docker.sock:/var/run/docker.sock:Z -p 8001:8080 -p 50000:50000  jenkins_docker_client_im
    docker exec -it jenkins bash

