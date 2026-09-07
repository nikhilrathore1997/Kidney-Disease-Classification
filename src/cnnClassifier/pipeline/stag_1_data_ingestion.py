from cnnClassifier.config.configuration import ConfigurationManger
from cnnClassifier.components.data_ingestion import DataIngestion
from cnnClassifier import logger

Stage_Name = "Data Ingestion stage"

class DataIngestionTrainingPipeline:
    def __init__(self):
        pass
    def main(self):
        config = ConfigurationManger()
        data_ingestion_config = config.get_data_ingestion_config()
        data_ingestion = DataIngestion(config=data_ingestion_config)

        data_ingestion.downlaod_file()
        data_ingestion.extract_zip_file()

if __name__=="__main__":
    try:
        logger.info(f">>>>>>>>stage {Stage_Name} started<<<")
        obj = DataIngestionTrainingPipeline()
        obj.main()
        logger.info(f">>>>>> stage {Stage_Name} Completed <<<<<\n\nx=======")
    except Exception as e:
        raise e
        