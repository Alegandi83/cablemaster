from pyspark import pipelines as dp
from pyspark.sql.functions import col

# This file defines a sample transformation.
# Edit the sample below or add new transformations
# using "+ Add" in the file browser.

@dp.table
def iothub_clean():
    return (
        spark.read.table("das_azure_iot_brokers.azure_iothub.iothub_raw")
        .select("*")
    )
