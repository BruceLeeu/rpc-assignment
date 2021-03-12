# Create docker container from Python image
FROM python:3.9

# Update repos and install latest rabbbitmq (dependency of nameko)
RUN apt-get update && apt-get install -y --no-install-recommends 
RUN apt-get install rabbitmq-server -y

# Work from this directory
WORKDIR /usr/src/app 

# Install all pip dependencies for 'service.py' using copied requirements.txt file
COPY requirements.txt . 
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy created microservice to current WORKDIR
COPY service.py . 
COPY dockerrun.sh /usr/local/bin/dockerrun.sh 
RUN chmod +x /usr/local/bin/dockerrun.sh

CMD [ "dockerrun.sh" ]

# To run this container, see ReadMe...