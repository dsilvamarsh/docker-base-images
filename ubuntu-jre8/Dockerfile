FROM dsilvamarsh/ubuntu-base:latest
LABEL maintainer="dsilvamarsh92@gmail.com"
LABEL image="ubuntu-jre8-headless"

ARG JAVA_TAR_PATH=https://download.java.net/java/GA/jdk21.0.1/415e3f918a1f4062a0074a2794853d0d/12/GPL/openjdk-21.0.1_linux-aarch64_bin.tar.gz
#ARG JAVA_TAR_PATHhttps://download.java.net/java/GA/jdk21.0.1/415e3f918a1f4062a0074a2794853d0d/12/GPL/openjdk-21.0.1_linux-x64_bin.tar.gz
RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y --fix-missing --no-install-recommends openjdk-8-jre
ENV JAVA_HOME /usr/lib/jvm/java-8-openjdk-arm64
ENV PATH $JAVA_HOME/bin:$PATH
ENTRYPOINT ["sleep","infinity"] 


