# databricks-extract-load-dbt
This repo contains example of extract and load using databricks and transformation into silver and gold using dbt.

## 1. Create virtual environment
```
python -m venv ../databricks_env
source ../databricks_env/bin/activate
```

## 2. Create and start cluster
```
pip install databricks-cli 
databricks clusters create --json-file config/cluster.json
databricks clusters list
databricks fs mkdirs dbfs:/tmp/generated_raw_csv_data
databricks fs  --recursive cp ~/local_data/ dbfs:/tmp/generated_raw_csv_data
databricks clusters delete --cluster-id 0xx-xx-xxx-vh0au
```
## 3. List dbfs filesystem and delete cluster
```
databricks fs mkdirs dbfs:/tmp/generated_raw_csv_data
databricks fs  --recursive cp ~/local_data/ dbfs:/tmp/generated_raw_csv_data
databricks clusters delete --cluster-id 0xx-xx-xxx-vh0au
```

## 4. Add secret to databricks environment (aktechthoughts)
```
databricks secrets create-scope --scope aktechthoughts
databricks secrets put --scope aktechthoughts --key github-token
```

## 5. Configuring dbt 
### 1. Install following python libraries in the environment.

```
python3 -m pip install dbt-core
python3 -m pip install dbt-databrics
```

### 2. Create dbt project using 
```
dbt init projects
```
#### 1. Every dbt project has ~/.dbt/profiles.yaml in the home directory.
#### 2. The profile file has all the details to connect to an environment.
#### 3. Sample connection detail below

```yaml
connection-to-elt-databricks:
  target: dev
  outputs:
    dev:
      type: databricks
      schema: gold
      host: adb-20138829935.15.azuredatabricks.net
      http_path: sql/protocolv1/o/20138829935/0630-yyyyy-26mie2ei
      token: dapi6yyyyy941aa9837bec7f761aae-2
      threads: 1
```

#### 4. Every dbt project needs a dbt_project.yml file — this is how dbt knows a directory is a dbt project. It also contains important information that tells dbt how to operate on your project.
#### 5. Initial Minimal dbt configuration below

```yaml
# Name your project! Project names should contain only lowercase characters and underscores.
name: 'databricks_extract_load_dbt'
version: '1.0.0'
config-version: 2

# This setting configures which "profile" dbt uses for this project. Taken from ~/.dbt/profiles.yaml
profile: 'connection-to-elt-databricks'

models:

```

#### 6. Initial dbt tests.

```bash
dbt test
dbt debug
```

### 3. Follow Databricks Documentation at
* [Connect to databricks](https://docs.databricks.com/dev-tools/databricks-connect.html#set-up-your-ide-or-notebook-server)
* [Setup dbt project](https://docs.getdbt.com/reference/dbt_project.yml)

