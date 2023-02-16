import ingest
import transform
import persist
from pyspark.sql import SparkSession
import logging
# call function to read file config
import logging.config
import sys
class PipeLine:
    # logging.basicConfig(level="INFO")
    logging.config.fileConfig('resource/configs/logging.conf')

    def __init__(self):
        self.persist = None
        self.ingest = None
        self.transform = None
        self.spark = None

    def create_spark_session(self):
        print("Creating Spark Session")
        self.spark = SparkSession.builder.appName("Demo")\
            .master("local[*]")\
            .enableHiveSupport()\
            .getOrCreate()
        return self.spark
    
    def run_pipeline(self):
        logger = logging.getLogger("sLogger")
        try:

            logger.info("Running Pipeline")

            #  Ingest processing
            spark = self.create_spark_session()

            self.ingest = ingest.Ingest(spark)
            df = self.ingest.ingest_data()
            # Transform processing
            self.transform = transform.Transform(spark)

            transformed_df = self.transform.transform_data(df)

            #  Persist Processing
            self.persist = persist.Persist()
            self.persist.persist_data(transformed_df)
            return
        except Exception as exp:
            logger.error("An error ocured while running the pipeline >" + str(exp))
            sys.exit(1)


if __name__ == "__main__":
    logger = logging.getLogger("sLogger")
    logger.info("Running Pipeline 1")

    pipeline = PipeLine()
    pipeline.create_spark_session()
    pipeline.run_pipeline()
