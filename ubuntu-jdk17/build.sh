docker rm --force dsilvamarsh/ubuntu-jdk17
docker rm $(docker ps --filter status=exited -q)
docker build -t dsilvamarsh/ubuntu-jdk17 .
