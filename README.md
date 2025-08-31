1. Start app:  
`python3 src/weather.py`

2. Request data:  
`curl http://127.0.0.1:5000/weather?city=Belgrade`

3. Build docker container  
```
docker build -t weatherapp:X.X.X . --no-cache
docker build -t weatherclient:X.X.X . --no-cache
```  

4. Run Docker container
```
docker network create weather_net
docker run -p 5000:5000 --rm --network weather_net weatherapp:1.1.0
docker inspect weather_net                                              # get server ip addr
docker run -it -p 5001:5000 --network weather_net -e SERVER_ADDR=<IP_ADD> weatherclient:1.3.0

```  

5. Get info via browser (non server/app mode):  
`http://localhost:5000/weather?city=Belgrade`  
or via curl:  
`curl localhost:5000/weather?city=Belgrade`  

6. Other options  
    - do not clone repo in docker container
    - instead mount src  
        `docker run -p 5000:5000 weather-app -v ${PWD}/src:/opt:ro`

7. TBD:  
    - Client should save Weather in weather.json
    - /tmp/weather dir should be mounted to /tmp/weather
  
    - Docker compose!!! 
    - ENV
    - Build args
    - COPY vs mount
  
    - AWS Load Balancer (Health endpoint)

8. Install Docker on EC2 instance:
```
# on host
chmod 400 weather-test.pem
ssh -o IdentitiesOnly=yes -i weather-test.pem ec2-user@ec2-18-185-138-87.eu-central-1.compute.amazonaws.com

# on EC2
sudo yum update -y
sudo yum -y install docker
sudo service docker start
sudo usermod -a -G docker ec2-user
sudo systemctl enable docker
sudo chmod 666 /var/run/docker.sock
docker version
```