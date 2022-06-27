# Databricks notebook source
# This notebook pulls hourly json data from https://start.vag.de/dm-poc/api/v2/fahrten and stores in parquet format.

# COMMAND ----------

## Read data from remote api

import urllib.request, json, pandas as pd
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

date_time = now.strftime("%m%d%Y%H%M%S")
df.to_parquet('/dbfs/bronze/movement_'+date_time+'.gzip', compression='gzip')
