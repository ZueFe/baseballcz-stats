FROM python:3.6.5
MAINTAINER Jan Ferko <jan.ferko3@gmail.com>

# Install apt dependencies
COPY /scripts/deb_list.txt /
RUN echo 'deb http://security.debian.org/ stretch/updates main' > /etc/apt/sources.list.d/debian-mozilla.list && \
    wget mozilla.debian.net/pkg-mozilla-archive-keyring_1.1_all.deb && \
    #wget https://download.mozilla.org/?product=firefox-latest&os=linux64&lang=en-US && \
    dpkg -i pkg-mozilla-archive-keyring_1.1_all.deb && \
    apt-get update && \
    apt-get install -y `cat deb_list.txt`

# Install geckodriver
#WORKDIR /tmp
RUN wget https://github.com/mozilla/geckodriver/releases/download/v0.17.0/geckodriver-v0.17.0-linux64.tar.gz -O geckodriver.tar.gz && \
    tar -xvf ./geckodriver.tar.gz && \
    mv geckodriver /opt/geckodriver && \
    rm geckodriver.tar.gz && \
    chmod 755 /opt/geckodriver && \
    ln -fs /opt/geckodriver /usr/bin/geckodriver

# Setup xvfb
ENV SCREEN_WIDTH 1360
ENV SCREEN_HEIGHT 1020
ENV SCREEN_DEPTH 24
ENV DISPLAY :99.0
ENV GIT_BRANCH master
ENV PIP_DEFAULT_TIMEOUT 10000

# Copy application source
RUN git clone https://github.com/ZueFe/baseballcz-stats.git /opt/app && \
    cd /opt/app && \
    git checkout $GIT_BRANCH && \
    echo '-=!!--c!!o!n!i!ng bra!nch de!a!!n!!'
WORKDIR /opt/app

# Install pipenv and download dependencies
RUN pip install --upgrade pip && pip install -r remote/requirements.txt && echo 'done downloading liibraries'

ENTRYPOINT ["python"]
CMD ["remote/server/server.py"]

