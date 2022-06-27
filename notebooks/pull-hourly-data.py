# Databricks notebook source
# This notebook pulls hourly json data from https://start.vag.de/dm-poc/api/v2/fahrten and stores in parquet format.

# COMMAND ----------

## Initilize token from the secret.
#token = dbutils.secrets.get(scope="aktechthoughts", key="github-token") # Not required for next command.
#pip install git+https://abhishek_ku@yahoo.com:$token@https://github.com/aktechthoughts/databricks-extract-load-dbt/blob/main/requirements.txt


# COMMAND ----------

## Install directly from the repository file.
#%pip install -r https://raw.githubusercontent.com/aktechthoughts/databricks-extract-load-dbt/main/requirements.txt

# COMMAND ----------

## Read data from remote api

import urllib.request, json,pandas as pd
from datetime import datetime
url = "https://start.vag.de/dm-poc/api/v2/fahrten"
response = urllib.request.urlopen(url)
result = json.loads(response.read())



# COMMAND ----------

# Save data in local variable.
ts = result['metadata']['timestamp']
ver = result['metadata']['version']

df = pd.json_normalize(result['data'])
df['ts'] = ts
df['version'] = ver


# COMMAND ----------

# Save data in parquet file.

date_time = datetime.now().strftime("%Y%m%d%H%M%S")
df.to_parquet('/dbfs/bronze/movement_'+date_time+'.gzip', compression='gzip')

#

# COMMAND ----------


