# docker-Compose for Elasticsearch Logstash Kibana and Filebeat

Steps
1. Clone the Repo.
2. Run docker-compose up -d
3. Verify all docker container are running
4. Run python script to generate dummy logs data using python logs_generator.py command
5. Open Kibana UI (Available on localhost:5601)
6. Create dataview on kibana (Name - any, pattern logstash-*). This will create your index pattern
7. Click on discover
8. you will get all your dummy log data here
