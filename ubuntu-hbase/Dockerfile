FROM ubuntu-jre17:latest

LABEL maintainer="dsilvamarsh92@gmail.com"
LABEL image="ubuntu-hadoop-hbase"
ARG HBSAE_TAR=https://dlcdn.apache.org/hbase/2.5.6/hbase-2.5.6-bin.tar.gz
RUN wget ${HBSAE_TAR} && \
    tar -xvf hbase-2.5.6-bin.tar.gz && \
    rm hbase-2.5.6-bin.tar.gz && \
    mv hbase-2.5.6 /opt/
ENV HBASE_HOME /hbase-2.5.6
ENV PATH $HBASE_HOME/bin:$PATH
ENTRYPOINT ["sleep","infinity"] 



