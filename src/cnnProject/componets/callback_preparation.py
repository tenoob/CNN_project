#CallbackPrepareComponent
import os
import time
import urllib.request as request
from zipfile import ZipFile
import tensorflow as tf
from cnnProject.entity import CallbackPreparationConfig

class CallbackPreparation:
    def __init__(self,config:CallbackPreparationConfig) -> None:
        self.config = config

    @property
    def _create_tb_callbacks(self):
        #good ideal to create a folder structure with timestamps
        timestamp = time.strftime("%Y-%m-%d-%H-%M-%S")

        tb_running_log_dir = os.path.join(
            self.config.tensorboard_root_log_dir,
            f"tb_logs_at_{timestamp}"
        )

        return tf.keras.callbacks.TensorBoard(log_dir=tb_running_log_dir)


    @property
    def _create_ckpt_callbacks(self):
        return tf.keras.callbacks.ModelCheckpoint(
            filepath=self.config.checkpoint_model_filepath,
            save_best_only=True  #save only best weights aka loss was less
        )



    def get_tb_checkpoint_callback(self):
        return [
            self._create_tb_callbacks,
            self._create_ckpt_callbacks
        ]

   
    