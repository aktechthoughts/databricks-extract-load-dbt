#!/bin/bash
#set -x

cluster_id_status=$(databricks clusters list | grep 'PENDING\|RUNNING' | awk '{ print $1"|"$3}')
cluster_id=$(echo "$cluster_id_status"| awk -F"|" '{ print $1 }')
cluster_status=$(echo "$cluster_id_status"| awk -F"|" '{ print $2 }')

if [[ "$cluster_status" = "RUNNING" ]]
then
    echo "The clusrer id:"$cluster_id" is started."
    exit 0
fi

if [[ "$cluster_status" = "" ]]
then
  databricks clusters create --json-file config/cluster.json > /dev/null 2>&1 
fi

cluster_status="PENDING"
while [[ "$cluster_status" = "PENDING" ]]
do
    sleep 2
    cluster_id_status=$(databricks clusters list | grep 'PENDING\|RUNNING' | awk '{ print $1"|"$3}')
    cluster_id=$(echo "$cluster_id_status"| awk -F"|" '{ print $1 }')
    cluster_status=$(echo "$cluster_id_status"| awk -F"|" '{ print $2 }')
done

echo "The clusrer id:"$cluster_id"is started."
exit 0