import numpy as np
from numpy import ndarray

from module.ml.nn.mynn.Layer import Layer


class MyNNModel(object):
    def __init__(self, layers: [Layer]=None):
        if layers is None:
            layers = []
        # layers - dont include input layer
        self._layers = layers
        # weight matrices
        self._weights = [np.ndarray]
        return

    @property
    def weights(self):
        """
        :return: list of weight matrices
        """
        return self._weights

    def add(self, Layer):
        self._layers.append(Layer)
        return

    def compile(self, optimizer=None, loss=None, metrics=None):
        return

    def fit(self, y_train: np.ndarray=None, epoch = 1):
        return

    def predict(self, Y: ndarray):
        return

