1. Start app:  
`python3 src/weather.py`

2. Request data:  
`curl http://127.0.0.1:5000/weather?city=Belgrade`

3. Build docker container  
`docker build -t weather-app . --no-cache`  

4. Run Docker container
`docker run -p 5000:5000 weather-app`  

5. Get info via browser:  
`http://localhost:5000/weather?city=Belgrade`  
or via curl:  
`curl localhost:5000/weather?city=Belgrade`  