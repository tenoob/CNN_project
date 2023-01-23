from cnnProject.config import ConfigrationManger
from cnnProject.componets import CallbackPreparation
from cnnProject.componets import Training
from cnnProject import logger

STAGE_NAME = "Training Stage"


def main():
    config = ConfigrationManger()
    callback_preparation_config = config.get_callback_perparation_config()
    callback_prepare = CallbackPreparation(config=callback_preparation_config)
    callback_lst = (
        callback_prepare.get_tb_checkpoint_callback()
    )  # callback list prepared

    training_config = config.get_training_config()
    training = Training(config=training_config)
    training.get_base_model()
    training.train_valid_generator()  # create a training and validation generator similar to train_test_split but not exactly  same
    training.train(
        callback_list=callback_lst,
    )


if __name__ == "__main__":
    try:
        logger.info(f"\n\n{'*'*10}stage {STAGE_NAME} started {'*'*10}")
        main()
        logger.info(f"{'*'*10}stage {STAGE_NAME} completed {'*'*10}\n\n")
    except Exception as e:
        logger.exception(e)
        raise e
