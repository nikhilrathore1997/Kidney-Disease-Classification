from cnnClassifier.constants import *
from cnnClassifier.utils.common import read_yaml,create_directorries,get_size
from cnnClassifier.entity.config_entity import DataIngestionConfig
class ConfigurationManger:
    def __init__(
        self ,config_file_path = CONFIG_FILE_PATH,
        params_file_path = PARAMS_FILE_PATH):

        self.config = read_yaml(config_file_path)
        self.params = read_yaml(params_file_path)
        # logger(f"Path : {CONFIG_FILE_PATH}")

        create_directorries([self.config.artifacts_root])
    
    def get_data_ingestion_config(self)->DataIngestionConfig:
        config = self.config.data_ingestion
        create_directorries([config.root_dir])

        data_ingestion_config = DataIngestionConfig(root_dir=config.root_dir,
            source_URL=config.source_URL,
            local_data_file=config.local_data_file,
            unzip_dir = config.unzip_dir
        )
        return data_ingestion_config



