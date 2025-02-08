from cnnClassifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from cnnClassifier import logger

STAHE_NAME="Data Ingestion stage"

try:
    logger.info(f">>>>> stage {STAHE_NAME} started <<<<<<<<")
    obj=DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f">>>>> stage {STAHE_NAME} completed <<<<<<<<")
except  Exception as e:
         logger.exception(e)
         raise e   