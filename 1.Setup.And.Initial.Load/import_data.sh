#!/bin/bash  
while read line
do
  curl -H "Content-Type: application/json" -v -X POST -d "$line" http://localhost:9200/mydata/user/ 
done < users.json
