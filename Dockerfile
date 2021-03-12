FROM python:3.9

RUN apt-get update && apt-get install -y --no-install-recommends 
RUN apt-get install rabbitmq-server -y
#RUN rabbitmq-plugins enable rabbitmq_management
#RUN service rabbitmq-server start
WORKDIR /usr/src/app 

COPY requirements.txt . 
RUN pip install --upgrade pip && pip install -r requirements.txt  
COPY service.py . 
#CMD [ "nameko", "run", "service" ]