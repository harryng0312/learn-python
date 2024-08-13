import numpy as np

from module.ml.nn.mynn.Layer import Layer


class Flatten(Layer):

    def __init__(self, input_shape=None, **kwargs):
        super().__init__()
        self.input_shape = input_shape
        self._x = None
        return

    def build(self):
        """
        :param x: 2d matrix
        :return:
        """
        if len(self.x.shape) == 1:
            return
        elif len(self.x.shape) == 2:
            return
        else:
            raise ValueError('Input must be 2d or 3d array')
        pass

    @property
    def x(self) -> np.ndarray:
        return self._x

    pass