# databricks-extract-load-dbt
This repo contains example of extract and load using databricks and transformation into silver and gold using dbt.


# databricks-certification-preparation



## Create virtual environment
```
python -m venv ../databricks_env
source ../databricks_env/bin/activate
```

## Create and start cluster
```
pip install databricks-cli 
databricks clusters create --json-file config/cluster.json
databricks clusters list
databricks fs mkdirs dbfs:/tmp/generated_raw_csv_data
databricks fs  --recursive cp ~/local_data/ dbfs:/tmp/generated_raw_csv_data
databricks clusters delete --cluster-id 0xx-xx-xxx-vh0au
```
## List dbfs filesystem and delete cluster
```
databricks fs mkdirs dbfs:/tmp/generated_raw_csv_data
databricks fs  --recursive cp ~/local_data/ dbfs:/tmp/generated_raw_csv_data
databricks clusters delete --cluster-id 0xx-xx-xxx-vh0au
```

 
## Add your files
Follow Databricks Documentation at
https://docs.databricks.com/dev-tools/databricks-connect.html#set-up-your-ide-or-notebook-server
