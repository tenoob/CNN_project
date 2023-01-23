from cnnProject.config import ConfigrationManger
from cnnProject.componets import CallbackPreparation
from cnnProject import logger

STAGE_NAME = "Prepare CallBack Stage"


def main():
    config = ConfigrationManger()
    callback_preparation_config = config.get_callback_perparation_config()
    callback_prepare = CallbackPreparation(config=callback_preparation_config)
    callback_lst = callback_prepare.get_tb_checkpoint_callback()
    return callback_lst

#python src/cnnProject/pipeline/stage_2_base_model_preparation.py
#src\cnnProject\pipeline\state_3_callback_preparation.py
#src/cnnProject/pipeline/stage_3_callback_preparation.py
if __name__ == "__main__":
    try:
        logger.info(f"\n\n{'*'*10}stage {STAGE_NAME} started {'*'*10}")
        main()
        logger.info(f"{'*'*10}stage {STAGE_NAME} completed {'*'*10}\n\n")
    except Exception as e:
        logger.exception(e)
        raise e
