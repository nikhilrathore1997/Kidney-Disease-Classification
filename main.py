# from src.cnnClassifier import logger
from cnnClassifier import logger
from cnnClassifier.pipeline.stag_1_data_ingestion import DataIngestionTrainingPipeline
# logger.info("wellcome to our custom log")

Stage_Name = "Data Ingestion Stage"
try:
    logger.info(f">>>>>>>>stage {Stage_Name} started<<<")
    obj = DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f">>>>>> stage {Stage_Name} Completed <<<<<\n\nx=======")
except Exception as e:
    raise e