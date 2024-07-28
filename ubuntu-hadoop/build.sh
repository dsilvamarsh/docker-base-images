docker rm --force dsilvamarsh/ubuntu-hadoop
docker rm $(docker ps --filter status=exited -q)
docker build -t dsilvamarsh/ubuntu-hadoop .
