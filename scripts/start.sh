#!/bin/bash
#set -x

job_id_status=$(databricks clusters list | grep 'PENDING\|RUNNING' | awk '{ print $1"|"$3}')
job_id=$(echo "$job_id_status"| awk -F"|" '{ print $1 }')
job_status=$(echo "$job_id_status"| awk -F"|" '{ print $2 }')

if [[ "$job_status" = "RUNNING" ]]
then
    echo "$job_id"
    exit 0
fi

if [[ "$job_status" = "" ]]
then
  databricks clusters create --json-file config/cluster.json > /dev/null 2>&1 
fi

job_status="PENDING"
while [[ "$job_status" = "PENDING" ]]
do
    sleep 2
    job_id_status=$(databricks clusters list | grep 'PENDING\|RUNNING' | awk '{ print $1"|"$3}')
    job_id=$(echo "$job_id_status"| awk -F"|" '{ print $1 }')
    job_status=$(echo "$job_id_status"| awk -F"|" '{ print $2 }')
done

echo "$job_id"
exit 0