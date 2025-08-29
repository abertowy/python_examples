# Docker Swarm

Orchestartors
-------------
- auto scale up: adds more containers when the workload increases
- auto scale down: removes cntainers when the workload decreases
- high availability: ensures enough containers are running to provide the service
- garbage collection: terminates containers that have crashed

Docker Swarm
------------
- same as Swarm mode
- provides high levels of service availability by clustering Docker host systems
- node: a system that is part of the Docker Swarm (includes: Docker Engines, Managers, Workers)
- replicas / scaling: additional containers to handle increased workloads
- encrypts communication between nodes
- allows for internal networks
- provides service discovery

CMD
---------
```
docker swarm init                               # if not successful, try the next one
docker swarm init --addvertise-addr 10.4.8.15   # choose ip from prev output
docker swarm join --token <token> <ip>:<port>   # to add a worker to this swarm
docker swarm join-token worker                  # same as prev
docker swarm join-token manager                 # to add a manager to this swarm
                                                # check if required ports are open 2377, and others
docker info | grep -A5 Swarm
docker node ls
docker service create --name web -p 80:80 nginx:latest
docker service ls
docker service ps web
docker service inspect --pretty web
docker service scale web=2
docker service rm web
```