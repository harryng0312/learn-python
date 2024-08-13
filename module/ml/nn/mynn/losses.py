import numpy as np


def softmax(z_i: float, z: np.ndarray) -> float:
    return np.exp(z_i) / np.sum(np.exp(z))

def grad_softmax(z_i: float, z: np.ndarray):
    # create S diagonal matrix with softmax(z_i, z)
    # create outer product matrix of softmax(z_i, z)
    # grad = S - outer_product(softmax, softmax.T)
    return