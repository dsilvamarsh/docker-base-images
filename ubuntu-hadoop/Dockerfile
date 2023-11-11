FROM ubuntu-jre17:latest

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
RUN mkdir /opt/hdfs
ENV HADOOP_CONF_DIR=${HADOOP_HOME}
ENV HADOOP_COMMON_HOME=${HADOOP_HOME}
ENV HADOOP_COMMON_PATH=${HADOOP_HOME}
ENV HADOOP_MAPRED_HOME=${HADOOP_HOME}
ENV HADOOP_YARN_HOME=${HADOOP_HOME}
ENV HADOOP_HDFS_HOME=/opt/hdfs
ENTRYPOINT ["sleep","infinity"] 
