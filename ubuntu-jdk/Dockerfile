FROM ubuntu-base:latest
LABEL maintainer="dsilvamarsh92@gmail.com"
LABEL image="ubuntu-jre21-headless"

ARG JAVA_TAR_PATH=https://download.java.net/java/GA/jdk21.0.1/415e3f918a1f4062a0074a2794853d0d/12/GPL/openjdk-21.0.1_linux-aarch64_bin.tar.gz
#ARG JAVA_TAR_PATHhttps://download.java.net/java/GA/jdk21.0.1/415e3f918a1f4062a0074a2794853d0d/12/GPL/openjdk-21.0.1_linux-x64_bin.tar.gz

ADD ${JAVA_TAR_PATH} /opt
RUN cd /opt && tar -xvf /opt/openjdk-21.0.1_linux-aarch64_bin.tar.gz && rm openjdk-21.0.1_linux-aarch64_bin.tar.gz
ENV JAVA_HOME /opt/jdk-21.0.1
ENV PATH $JAVA_HOME/bin:$PATH
ENTRYPOINT ["sleep","infinity"] 


