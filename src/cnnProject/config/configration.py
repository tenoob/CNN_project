from cnnProject.constant import CONFIG_FILE_PATH, PARAMS_FILE_PATH
from cnnProject.utils import read_yaml, create_directories
import os
from cnnProject.entity import DataIngestionConfig , BaseModelPreparationConfig,CallbackPreparationConfig
from pathlib import Path


class ConfigrationManger:
    def __init__(
        self, config_file_path=CONFIG_FILE_PATH, params_file_path=PARAMS_FILE_PATH
    ) -> None:
        self.config = read_yaml(config_file_path)
        self.params = read_yaml(params_file_path)
        create_directories([self.config.artifact_root])

    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config.data_ingestion

        create_directories([config.root_dir])

        data_ingestion_config = DataIngestionConfig(
            root_dir=config.root_dir,
            source_URL=config.source_URL,
            local_data_file=config.local_data_file,
            unzip_dir=config.unzip_dir,
        )
        return data_ingestion_config


    def get_base_model_perparation_config(self) -> BaseModelPreparationConfig :
        config = self.config.base_model_preparation

        create_directories([config.root_dir])

        base_model_prepare_config = BaseModelPreparationConfig(
            root_dir = Path(config.root_dir),
            base_model_path= Path(config.base_model_path),
            updated_base_model_path= Path(config.updated_base_model_path),
            params_image_size = self.params.IMAGE_SIZE,
            params_learning_rate = self.params.LEARNING_RATE,
            params_include_top = self.params.INCLUDE_TOP,
            params_weights = self.params.WEIGHTS,
            params_classes=self.params.CLASSES
        )

        return base_model_prepare_config

    def get_callback_perparation_config(self) -> CallbackPreparationConfig :
        config = self.config.callback_preparation

        model_checkpoint_dir = os.path.dirname(config.checkpoint_model_filepath)
        create_directories([
            Path(config.tensorboard_root_log_dir),
            Path(model_checkpoint_dir)
        ])

        callback_prepare_config = CallbackPreparationConfig(
            root_dir = Path(config.root_dir),
            tensorboard_root_log_dir = Path(config.tensorboard_root_log_dir),
            checkpoint_model_filepath = Path(config.checkpoint_model_filepath)
        )

        return callback_prepare_config
