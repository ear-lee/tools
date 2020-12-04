FROM dockerhub.datagrand.com/base_image/python37:1.8

RUN apt-get update
RUN cd / && ln -sf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime

RUN python -m pip install pip==19.3.1
ADD requirements /scheduler/requirements
RUN cd /scheduler/requirements/ &&\
    pip install -r requirements.txt &&\
    rm -rf /scheduler/requirements

ADD scheduler /scheduler/scheduler
ADD start_server.py /scheduler/start_server.py
ADD docker/run_prod.sh /scheduler/run_prod.sh

RUN rm -f `find / -name "*.whl"` && \
    rm -f `find / -name "*jquery.js"`

RUN chmod +777 /scheduler/run_prod.sh

WORKDIR /scheduler

CMD ./run_prod.sh