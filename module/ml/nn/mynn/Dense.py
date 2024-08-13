import numpy as np

from module.ml.nn.mynn.Layer import Layer


class Dense(Layer):

    def __init__(self, units: int, **kwargs):
        super().__init__()
        self._weight = None
        self._bias = None
        self.units = units
        return

    def build(self):
        """
        buidl Layer
        :return:
        """
        self._weight = np.random.randn(self.units)
        # self.bias = np.random.randint(self.input_feature_size)
        self._bias = np.zeros(self.units)
        return

    @property
    def weight(self):
        return self._weight

    @property
    def bias(self):
        return self._bias

    pass