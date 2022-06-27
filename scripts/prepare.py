# Databricks notebook source
# MAGIC %fs ls /tmp/derovis_data/

# COMMAND ----------

# MAGIC %sh
# MAGIC mkdir /dbfs/tmp/derovis_data_csv/
# MAGIC ls /dbfs/tmp/derovis_data/ | while read line
# MAGIC do
# MAGIC sed  "/^data/!d" /dbfs/tmp/derovis_data/$line > /dbfs/tmp/derovis_data_csv/$line
# MAGIC done

# COMMAND ----------

# Define the input and output formats and paths and the table name.
read_format = "csv"
write_format = "delta"
load_path = "dbfs:/tmp/derovis_data_csv/*"
save_path = "dbfs:/tmp/derovis_delta"
table_name = "default.movements"

# Load the data from its source.
movement = (
    spark.read.format(read_format)
    .option("header", "false")
    .option("delimiter", ";")
    .load(load_path)
)

header = [
    "#data",
    "measuring_number",
    "vehicle_id",
    "line",
    "stop_id",
    "stop_name",
    "stop_index",
    "course",
    "dest",
    "direction",
    "door_code",
    "count_in",
    "count_out",
    "timestamp_ibis",
    "timestamp_local",
    "latitude",
    "longitude",
    "prec",
    "timestamp_open",
    "timestamp_close",
    "category",
    "odo",
    "pet",
    "extra_column",
]

movement = movement.toDF(*header)
movement.show()


# COMMAND ----------

# Write the data to its target.
movement.write \
    .format(write_format) \
    .mode('overwrite') \
    .save(save_path)

# Create the table.
spark.sql("CREATE TABLE " + table_name + " USING DELTA LOCATION '" + save_path + "'")

# COMMAND ----------

# MAGIC %sql
# MAGIC select vehicle_id,count(*) from default.movements group by vehicle_id

# COMMAND ----------


