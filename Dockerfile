FROM python:3.9

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN mkdir /code
WORKDIR /code

COPY . /code
COPY ./entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

RUN python -m pip install --upgrade pip
RUN python -m pip install -r requirements.txt
RUN python -m pip install psycopg2-binary
RUN python -m pip install gunicorn
RUN python -m pip install requests
RUN python -m pip install simplejson

ENTRYPOINT [ "bash","-c", "/entrypoint.sh" ]
