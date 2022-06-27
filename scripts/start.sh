#!/bin/bash
#set -x
databricks clusters create --json-file config/cluster.json > /dev/null 2>&1 