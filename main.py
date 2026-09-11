# from src.cnnClassifier import logger
from cnnClassifier import logger
from cnnClassifier.pipeline.stag_1_data_ingestion import DataIngestionTrainingPipeline
from cnnClassifier.pipeline.stage_2_prepare_base_model import PrepareBaseModelTrainingPipeline
from cnnClassifier.pipeline.stage3_model_training import ModelTrainingPipeline 
# from cnnClassifier.components.data_ingestion import DataIngestion
# logger.info("wellcome to our custom log")

# Stage_Name = "Data Ingestion Stage"
# try:
#     logger.info(f">>>>>>>>stage {Stage_Name} started<<<")
#     Data_Ingestion = DataIngestionTrainingPipeline()
#     Data_Ingestion.main()
#     logger.info(f">>>>>> stage {Stage_Name} Completed <<<<<\n\nx=======")
# except Exception as e:
#     logger.info(e)
#     raise e 

Stage_Name = "Prepare Base Model"

try:
    logger.info(f"*********************")
    logger.info(f">>>>>>> Stage {Stage_Name} started <<<<")
    prepare_base_model = PrepareBaseModelTrainingPipeline()
    prepare_base_model.main()
    logger.info("<<<<<<<Stage  {Stage_Name} completed <<<<<<\n\nx======x")
except Exception as e:
    logger.info(e)
    raise e


Stage_Name = "Training"
try:
    logger.info(f"*****************")
    logger.info(f">>>>>>>>..Stage {Stage_Name} stared <<<<<<<")
    model_trainer = ModelTrainingPipeline()
    model_trainer.main()
    logger.info(f">>>>>>>>>Stage {Stage_Name} completed <<<<<\n\n====x")
except Exception as e:
    logger.exception(e)
    raise e