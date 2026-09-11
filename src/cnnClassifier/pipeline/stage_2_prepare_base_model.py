from cnnClassifier.components.prepare_base_model import PrepareBaseModel
from cnnClassifier.config.configuration import ConfigurationManger
from cnnClassifier import logger

Stage_Name = "Prepare Base Model"

class PrepareBaseModelTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config =ConfigurationManger()
        preapare_base_model_config = config.get_prepare_base_model_config()
        preapare_base_model = PrepareBaseModel(config= preapare_base_model_config)
        preapare_base_model.get_base_model()
        preapare_base_model.update_base_model()

if __name__=='__main__':
    try:
        logger.info(f"*********************")
        logger.info(f">>>>>>> Stage {Stage_Name} started <<<<")
        obj = PrepareBaseModelTrainingPipeline()
        obj.main()
        logger.info(">>>>>>>> Stage  {Stage_Name} completed <<<<<<\n\nx======x")
    except Exception as e:
        logger.info(e)
        raise e
