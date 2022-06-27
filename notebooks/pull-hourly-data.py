# Databricks notebook source
# This notebook pulls hourly json data from https://start.vag.de/dm-poc/api/v2/fahrten and stores in parquet format.

# COMMAND ----------

##

import urllib.request, json, pandas as pd
url = "https://start.vag.de/dm-poc/api/v2/fahrten"
response = urllib.request.urlopen(url)
result = json.loads(response.read())
ts = result['metadata']['timestamp']
ver = result['metadata']['version']

df = pd.json_normalize(result['data'])
df['ts'] = ts
df['version'] = ver

df.to_parquet('df.parquet.gzip', compression='gzip')

df1=pd.read_parquet('df.parquet.gzip')
print(df1)