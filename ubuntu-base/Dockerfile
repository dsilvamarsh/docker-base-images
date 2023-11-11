FROM ubuntu
LABEL maintainer="dsilvamarsh92@gmail.com"
LABEL image="ubuntu-base"
ARG INSTALL_PACKAGES=wget net-tools curl netcat gnupg libsnappy-dev
RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y --fix-missing --no-install-recommends wget net-tools curl netcat gnupg libsnappy-dev  \ 
      && rm -rf /var/lib/apt/lists/*
ENTRYPOINT ["sleep","infinity"]