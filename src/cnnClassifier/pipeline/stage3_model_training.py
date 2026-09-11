from cnnClassifier.config.configuration import ConfigurationManger
from cnnClassifier.components.model_training import Training
from cnnClassifier import logger
Stage_Name = "Training"

class ModelTrainingPipeline:
    def __inti__(self):
        pass

    def main(self):
        config = ConfigurationManger()
        training_config = config.get_training_config()
        training = Training(config=training_config)
        training.get_base_model()
        training.train_valid_generator()
        training.train()

if __name__ == '__main__':
    try:
        logger.info(f"*****************")
        logger.info(f">>>>>>>>..Stage {Stage_Name} stared <<<<<<<")
        obj = ModelTrainingPipeline()
        obj.main()
        logger.info(f">>>>>>>>>Stage {Stage_Name} completed <<<<<\n\n====x")
    except Exception as e:
        logger.exception(e)
        raise e