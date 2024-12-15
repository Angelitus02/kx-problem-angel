# kx-problem-angel

One file called storage.py to store data with getters/setters(or just getters as data can be hardcoded) that is accessed by another class/file: gateway.py

pip install flask

get everything running without Docker first and then containerised application after

Each python file will have a dockerfile (two in total) and a docker-compose.yaml with instructions on how the app works: 1 gateway and 3 storages.
Application is run calling docker-compose
