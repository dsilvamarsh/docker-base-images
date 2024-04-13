FROM dsilvamarsh/ubuntu-base:latest
LABEL maintainer="dsilvamarsh92@gmail.com"
LABEL image="ubuntu-jre17-headless"
RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y --fix-missing --no-install-recommends openjdk-17-jre
#ENV JAVA_HOME /usr/lib/jvm/java-17-openjdk-arm64
#ENV PATH $JAVA_HOME/bin:$PATH
ENTRYPOINT ["sleep","infinity"] 


