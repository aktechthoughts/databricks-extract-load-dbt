#!/bin/bash
#set -x
cluster_id=$(databricks clusters list | grep RUNNING | awk '{ print $1}')
databricks clusters delete --cluster-id $cluster_id > /dev/null 2>&1 
echo "The clusrer id:"$cluster_id" is stopped."