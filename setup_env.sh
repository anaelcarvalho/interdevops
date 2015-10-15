#!/bin/bash
mkdir elastic_home
cd elastic_home
wget https://download.elastic.co/elasticsearch/elasticsearch/elasticsearch-1.7.2.zip
unzip elasticsearch-1.7.2.zip
./elasticsearch-1.7.2/bin/plugin -install mobz/elasticsearch-head
wget https://download.elastic.co/kibana/kibana/kibana-4.1.2-linux-x64.tar.gz
tar -xvzf kibana-4.1.2-linux-x64.tar.gz
wget https://download.elastic.co/logstash/logstash/logstash-1.5.4.zip
unzip logstash-1.5.4.zip
cd ..
