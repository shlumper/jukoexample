FROM ubuntu:latest

RUN apt-get update \
  && apt-get install -y python3-pip python3-dev \
  && apt-get install -y git \
  && cd /usr/local/bin \
  && ln -s /usr/bin/python3 python \
  && pip3 --no-cache-dir install --upgrade pip \
  && rm -rf /var/lib/apt/lists/*


WORKDIR /root  
RUN pip3 install requests
RUN pip3 install py-fibonacci
ADD regression_kube_executer.py .
ADD start_script.sh .
