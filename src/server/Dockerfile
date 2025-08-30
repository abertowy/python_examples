FROM python:3.11-bookworm
RUN apt-get update && apt-get install -y git && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

WORKDIR /weather_app
RUN git clone https://github.com/abertowy/python_examples.git .

EXPOSE 5000

CMD ["python3", "/weather_app/src/server/weather.py"]