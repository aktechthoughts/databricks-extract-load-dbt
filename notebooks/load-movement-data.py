# Databricks notebook source
# This notebook is to load movement data into silver table.

# COMMAND ----------

# MAGIC %sql
# MAGIC CREATE SCHEMA IF NOT EXISTS silver;

# COMMAND ----------

## Crate a silver table if it doesn't exists

# COMMAND ----------

# MAGIC %sql
# MAGIC CREATE TABLE IF NOT EXISTS 
# MAGIC   silver.movement 
# MAGIC     PARTITIONED BY (fahrtStart)
# MAGIC     SELECT * FROM movement where 1=2;

# COMMAND ----------

# MAGIC %sql
# MAGIC MERGE INTO silver.movement 
# MAGIC USING movement 
# MAGIC ON 1=2
# MAGIC WHEN NOT MATCHED
# MAGIC   THEN INSERT *

# COMMAND ----------

# MAGIC %sql
# MAGIC select count(*) from silver.movement;

# COMMAND ----------


