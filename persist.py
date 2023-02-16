import pyspark
from pyspark.sql import SparkSession
import logging
import logging.config
import sys

class Persist:
    logging.config.fileConfig("resource/configs/logging.conf")
    def __init__(self):
        self.df = None

    def persist_data(self, df):
        logger = logging.getLogger("Persist")

        try:
            # Apply Persist Logger config setting in logging.conf
            logger.info("Persisting data")
            df.write.format("csv")\
                .option("header","true")\
                .save("transformed_retailstore.csv")

        except Exception as exception:
            logger.error("An error occur while persisting data > " + str(exception))
            # send email notifications or save to database

            # Raise Exception for main code catch == sys.exit(1). Khi raise Exception thì app will exit.
            raise Exception("HDFS Directory already exists")

