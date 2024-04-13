FROM dsilvamarsh/ubuntu-base:latest
LABEL maintainer="dsilvamarsh92@gmail.com"
LABEL image="ubuntu-jre17-headless"

RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y --fix-missing --no-install-recommends openjdk-17-jdk

ENTRYPOINT ["sleep","infinity"] 


