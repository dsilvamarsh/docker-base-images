FROM dsilvamarsh/ubuntu-jre8:latest

LABEL maintainer="dsilvamarsh92@gmail.com"
LABEL image="ubuntu-hadoop-"
#ARG HADOOP_TAR=https://dlcdn.apache.org/hadoop/common/hadoop-3.3.6/hadoop-3.3.6.tar.gz
ARG HADOOP_TAR=https://dlcdn.apache.org/hadoop/common/hadoop-3.3.6/hadoop-3.3.6-aarch64.tar.gz
RUN wget ${HADOOP_TAR} && \
    tar -xvf hadoop-3.3.6-aarch64.tar.gz && \ 
    rm hadoop-3.3.6-aarch64.tar.gz && \
    mv hadoop-3.3.6 /opt  
ENV HADOOP_HOME /opt/hadoop-3.3.6 
ENV PATH $HADOOP_HOME/bin:$PATH

#Hadoop configs
RUN mkdir /opt/datanode
RUN mkdir /opt/namenode
ENTRYPOINT ["sleep","infinity"] 
