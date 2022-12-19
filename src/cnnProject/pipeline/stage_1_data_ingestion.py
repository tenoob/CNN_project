from cnnProject.config import ConfigrationManger
from cnnProject.componets import DataIngestion
from cnnProject import logger

STAGE_NAME = 'Data Ingestion Stage'

def main():
    config = ConfigrationManger()
    data_ingestion_config = config.get_data_ingestion_config()
    data_ingestion = DataIngestion(config=data_ingestion_config)
    data_ingestion.download_file()
    data_ingestion.unzip_and_clean()


if __name__=='__main__':
    try:
        logger.info(f"\n\n{'*'*10}stage {STAGE_NAME} started {'*'*10}")
        main()
        logger.info(f"{'*'*10}stage {STAGE_NAME} completed {'*'*10}\n\n")
    except Exception as e:
        logger.exception(e)
        raise e