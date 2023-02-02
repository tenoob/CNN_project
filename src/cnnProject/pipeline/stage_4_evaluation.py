from cnnProject.config import ConfigrationManger
from cnnProject.componets import Evaluation
from cnnProject import logger

STAGE_NAME = "Evaluation Stage"


def main():
    config = ConfigrationManger()

    val_config = config.get_validation_config()
    evaluation = Evaluation(val_config)
    evaluation.evaluation()
    evaluation.save_score()


if __name__ == "__main__":
    try:
        logger.info(f"\n\n{'*'*10}stage {STAGE_NAME} started {'*'*10}")
        main()
        logger.info(f"{'*'*10}stage {STAGE_NAME} completed {'*'*10}\n\n")
    except Exception as e:
        logger.exception(e)
        raise e
