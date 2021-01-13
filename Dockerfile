FROM python:3.6

#USER root
WORKDIR /usr/src/app
#WORKDIR /app

#ADD . /app
COPY . .
#RUN pip install --trusted-host pypi.python.org -r requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 5000

ENV NAME World

CMD ["python", "./app.py"]
