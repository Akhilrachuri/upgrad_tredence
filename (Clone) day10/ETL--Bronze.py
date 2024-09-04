# Databricks notebook source
# MAGIC %run /Workspace/Users/akhil_1724384742435@npupgradassessment.onmicrosoft.com/day10/includes

# COMMAND ----------

dbutils.widgets.text("environment","dev")
v=dbutils.widgets.get("environment")

# COMMAND ----------

df=spark.read.csv(f"{input_path}products.csv",header=True,inferSchema=True)
df1=add_ingestion_col(df)
df2=df1.withColumn("environment",lit(v))
df2.write.mode("overwrite").option("mergeSchema", "true").saveAsTable("bronze.products_bronze")
