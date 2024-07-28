docker rm --force dsilvamarsh/ubuntu-jre8
docker rm $(docker ps --filter status=exited -q)
docker build -t dsilvamarsh/ubuntu-jre8 .
