FROM ubuntu-jre17:latest

LABEL maintainer="dsilvamarsh92@gmail.com"
LABEL image="ubuntu-hadoop-"
ARG HIVE_TAR=https://dlcdn.apache.org/hive/hive-3.1.3/apache-hive-3.1.3-bin.tar.gz
RUN wget ${HIVE_TAR} && \
    tar -xvf apache-hive-3.1.3-bin.tar.gz && \
    rm apache-hive-3.1.3-bin.tar.gz && \
    mv apache-hive-3.1.3-bin /opt apache-hive-3.1.3 
ENV HIVE_HOME /apache-hive-3.1.3
ENV PATH $HIVE_HOME/bin:$PATH
ENTRYPOINT ["sleep","infinity"] 



