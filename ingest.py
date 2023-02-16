from pyspark.sql.types import IntegerType
import logging
import logging.config
class Ingest:
    logging.config.fileConfig("resource/configs/logging.conf")
    def __init__(self, spark):
        self.spark = spark

    def ingest_data(self):
        logger = logging.getLogger("Ingest")

        logger.info("Ingesting Data")

        df = self.spark.read.format("csv")\
            .option("header","true")\
            .load("./retailstore.csv")
        df.show()
        df.describe().show()
        return df
