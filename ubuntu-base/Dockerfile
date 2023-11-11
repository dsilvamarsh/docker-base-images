FROM ubuntu
LABEL maintainer="dsilvamarsh92@gmail.com"
LABEL image="ubuntu-base"
RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends  \
      net-tools \
      curl \
      netcat \
      gnupg \
      libsnappy-dev \
      && rm -rf /var/lib/apt/lists/*
ENTRYPOINT ["sleep","infinity"]