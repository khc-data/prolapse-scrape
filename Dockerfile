FROM ubuntu:latest
RUN apt-get update && apt-get install -y software-properties-common && apt-get update

RUN apt-get install -y python cron pip
RUN pip install beautifulsoup4

ADD crontab /
ADD scrape.py /
RUN chmod a+x scrape.py

RUN crontab /crontab
ENTRYPOINT cron -f