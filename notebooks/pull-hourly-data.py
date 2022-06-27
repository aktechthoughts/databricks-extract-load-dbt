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

date_time = now.strftime("%m%d%Y%H%M%S")
df.to_parquet('movement_'+date_time+'.gzip', compression='gzip')

