from cnnProject.config import ConfigrationManger
from cnnProject.componets import BaseModelPreparation
from cnnProject import logger

STAGE_NAME = "Prepare BaseModel Stage"


def main():
    config = ConfigrationManger()
    base_model_preration_config = config.get_base_model_perparation_config()
    base_model_prepare = BaseModelPreparation(config=base_model_preration_config)
    base_model_prepare.get_base_model()
    base_model_prepare.update_base_model()


if __name__ == "__main__":
    try:
        logger.info(f"\n\n{'*'*10}stage {STAGE_NAME} started {'*'*10}")
        main()
        logger.info(f"{'*'*10}stage {STAGE_NAME} completed {'*'*10}\n\n")
    except Exception as e:
        logger.exception(e)
        raise e
