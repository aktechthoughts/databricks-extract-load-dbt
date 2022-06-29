#!/bin/bash
#set -x

notbook_path="/Repos/abhishek_ku@yahoo.com/databricks-extract-load-dbt/notebooks/"
notbook_name="$1"

cluster_id=$(databricks clusters list | grep RUNNING | awk '{ print $1}')

jq '.existing_cluster_id = "'$cluster_id'" | .name = "'$notbook_name'" | .notebook_task.notebook_path = "'$notbook_path$notbook_name'"'  config/job-template.json \
> temp/$notbook_name.json 


JOB_ID=$(databricks jobs create --json-file temp/$notbook_name.json | jq '.job_id')

RUN_ID=$(databricks jobs run-now --job-id $JOB_ID | jq '.run_id')

job_status="PENDING"
while [ $job_status = "RUNNING" ] || [ $job_status = "PENDING" ]
do
    sleep 2
    job_status=$(databricks runs get --run-id $RUN_ID | jq -r '.state.life_cycle_state')
done

RESULT=$(databricks runs get-output --run-id $RUN_ID)

RESULT_STATE=$(echo $RESULT | jq -r '.metadata.state.result_state')
RESULT_MESSAGE=$(echo $RESULT | jq -r '.metadata.state.state_message')
if [ $RESULT_STATE = "FAILED" ]
then
    echo "##vso[task.logissue type=error;]$RESULT_MESSAGE"
    echo "##vso[task.complete result=Failed;done=true;]$RESULT_MESSAGE"
fi

result=$(echo $RESULT | jq '.metadata.state.result')

if [ $result = "null" ]
then
echo "The job "$notbook_name" is finished."
fi