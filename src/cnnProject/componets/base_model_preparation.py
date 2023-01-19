import os
import urllib.request as request
from cnnProject.entity import BaseModelPreparationConfig
import tensorflow as tf
from pathlib import Path

class BaseModelPreparation:
    def __init__(self,config:BaseModelPreparationConfig) -> None:
        self.config = config

    #get the base model
    def get_base_model(self):
        self.model = tf.keras.applications.vgg16.VGG16(
            #they are part of parameters
            input_shape=self.config.params_image_size,
            weights=self.config.params_weights,
            include_top=self.config.params_include_top
            )
        """
                include_top means whether to include the ANN part of the model or not
        """
        print("base model type:",type(self.model))
        #base_model_path = self.config.base_model_path
        self.save_model(path=self.config.base_model_path , model = self.model)

    @staticmethod
    def _prepare_full_model(model,classes,freeze_all,freeze_till,learning_rate):
        """
        model: the model which we are using
        classes: output classes(Cat,Dog)
        freeze_all : Freezes weights of all the layers in CNN part.
        freeze_till: freeze weights uptill the layer given in the CNN part.
        learning_rate
        """

        #CNN part
        if (freeze_all):
            for layer in model.layers:
                layer.trainable = False
        elif (freeze_till is not None) and (freeze_till > 0):
            for layer in model.layers[:-freeze_till]:
                layer.trainable = False

        # Ann part
    
        flattern_in = tf.keras.layers.Flatten()(model.output) #passing the model output though a flattern layer method
        prediction = tf.keras.layers.Dense(
            units=classes,
            activation="softmax"
        )(flattern_in)  #passing the flattern output though a dense layer
        #the above approch is known as fuctional approch

        full_model = tf.keras.models.Model(
            inputs = model.input,
            outputs = prediction
        )

        full_model.compile(
            optimizer=tf.keras.optimizers.SGD(learning_rate=learning_rate),
            loss=tf.keras.losses.CategoricalCrossentropy(),
            metrics=["accuracy"]
        )

        full_model.summary()
        return full_model

    #update the base model
    def update_base_model(self):
        self.full_model = self._prepare_full_model(
            model = self.model,
            classes = self.config.params_classes,
            freeze_all = True,
            freeze_till = None,
            learning_rate = self.config.params_learning_rate
        )
        print("updated model type:",type(self.full_model))
        self.save_model(path = self.config.updated_base_model_path,model = self.full_model)

    @staticmethod
    def save_model(path:Path , model :tf.keras.Model):
        model.save(path)

    