FROM tensorflow/tensorflow:latest

RUN apt-get update && \
    apt-get -y install git

RUN pip3 install jupyterlab requests pandas numpy keras matplotlib scipy pandas-datareader xlrd h5py tables html5lib beautifulsoup4 lxml Jinja2 openpyxl PyYAML lightgbm

RUN mkdir /root/model
COPY model/* /root/model

COPY *.ipynb /root

COPY start_on_docker.sh /root
COPY start_notebooks.py /root

ARG DISCORD_URL
ENV DISCORD_URL=${DISCORD_URL}

ARG NOTEBOOK_TIMEOUT
ENV NOTEBOOK_TIMEOUT=${NOTEBOOK_TIMEOUT}

CMD /root/start_on_docker.sh
