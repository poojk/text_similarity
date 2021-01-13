FROM python:3.6

USER root

WORKDIR /app

ADD . /app

# Install our requirements.txt
#ADD requirements.txt /app/requirements.txt
#RUN pip install -r requirements.txt

RUN pip install --trusted-host pypi.python.org -r requirements.txt

EXPOSE 80

ENV NAME World

CMD ["python", "app.py"]
