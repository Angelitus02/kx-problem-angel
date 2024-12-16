# kx-problem-angel

One file called storage.py to store data with getters/setters(or just getters as data can be hardcoded) that is accessed by another class/file: gateway.py
Get everything running without Docker first and then containerised application after

Each python file will have a dockerfile (two in total) and a docker-compose.yaml with instructions on how the app works: 1 gateway and 3 storages.
Application is run calling docker-compose

I used an AI to check what routing framework is best for this application.
I considered Flask and FastAPI but I want to remain dependency free
and use Pythons built in standard library: http.server

I implemented the storage.py to be able to get data and status.
I will implement the round robyn randomess later on.
Round robyn implemented with a very simple index. (Could use iterator python classes as an improvement)

Some problems encountered:

Docker-compose command doesnt work with docker desktop in windows 
Fix: docker compose (without the -)

The reponses were 200 but no data was retrieved
Some logs: 
kx-problem-angel-storage1-1  | 172.18.0.5 - - [15/Dec/2024 18:36:33] "GET /data HTTP/1.1" 200 -
kx-problem-angel-storage2-1  | 172.18.0.5 - - [15/Dec/2024 18:36:33] "GET /data HTTP/1.1" 200 -
kx-problem-angel-storage3-1  | 172.18.0.5 - - [15/Dec/2024 18:36:33] "GET /data HTTP/1.1" 200 -
kx-problem-angel-gateway-1   | 172.18.0.1 - - [15/Dec/2024 18:36:33] "GET /data HTTP/1.1" 503 -

You can see here we get 3 (200) responses, one for each storage service. Then the gateway returns 503.

I had a minor bug where I was returning the 503 error regardless.
Now all responses are 200 but no data is being displayed in the browser or in the console.

Improvements to the application would be using docker volumes to store the dummy data.
