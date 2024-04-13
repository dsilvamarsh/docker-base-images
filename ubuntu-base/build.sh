docker rm --force dsilvamarsh/ubuntu-base
docker rm $(docker ps --filter status=exited -q)
docker build -t dsilvamarsh/ubuntu-base .
