# training Component
from pathlib import Path
import tensorflow as tf
from cnnProject.utils import save_json
from cnnProject.entity import EvaluationConfig


class Evaluation:
    def __init__(self, config: EvaluationConfig) -> None:
        self.config = config

    def _valid_generator(self):
        # will be doing augmentation

        datagenerator_kwargs = dict(rescale=1.0 / 255, validation_split=0.10)

        dataflow_kwargs = dict(
            target_size=self.config.params_image_size[
                :-1
            ],  # only takes rows and columns, channels not aka index 0,1
            batch_size=self.config.params_batch_size,
            interpolation="bilinear",
            # interpolation is a process of determining the unknown values that lie in between the known data points.
            # ex find value between 1 and 2 on a line.
        )

        valid_datagenerator = tf.keras.preprocessing.image.ImageDataGenerator(
            **datagenerator_kwargs
        )

        # validation data
        self.valid_generator = valid_datagenerator.flow_from_directory(
            directory=self.config.training_data,
            subset="validation",
            shuffle=False,
            **dataflow_kwargs
        )

    @staticmethod
    def load_model(path: Path):
        return tf.keras.models.load_model(path)

    # start training
    def evaluation(self):
        model = self.load_model(self.config.path_of_model)
        self._valid_generator()
        self.score = model.evaluate(self.valid_generator)

    def save_score(self):
        scores = {"loss": self.score[0], "accuracy": self.score[1]}

        save_json(path=Path("scores.json"), data=scores)
        # store the scores.json in root for dvc to track it easily
