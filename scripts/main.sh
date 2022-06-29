#!/bin/bash
#set -x

./scripts/start.sh
./scripts/run.sh pull-hourly-data
./scripts/run.sh load-movement-data
./scripts/stop.sh