1. COMMANDS  
```
docker run -it -p 5000:5000 weather-app /bin/bash

docker exec -it 4b78a203f2b8 bash
docker exec -it d946af217980 curl http://127.0.0.1:5000/weather?city=Belgrade

docker exec -d weather-app touch /opt/forecast.txt  # create a forecst file in container

docker top weather-app                              # same as top for host -> show processes

docker logs -t weather-app                          # shows logs from container
grep -i docker /var/log/syslog                      # shows logs from docker itself
journalctl --no-pager -u docker.service -n 25                  # the same
```

2. Docker registries  
```
docker pull docker.io/ubuntu:bionic                         # default registry
docker pull ubuntu:bionic                                   # the same as prev

docker pull registry.hub.docker.com/library/ubuntu:bionic   # another registry is used
# need to run docker login command to enable usage of external registries
docker login
```
