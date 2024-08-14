import numpy as np


def softmax(z: np.ndarray) -> float:
    return np.exp(z) / np.sum(np.exp(z))

def grad_softmax(z: np.ndarray):
    # create S diagonal matrix with softmax(z_i, z)
    # create outer product matrix of softmax(z_i, z)
    # grad = S - outer_product(softmax, softmax.T)
    sz = softmax(z)
    return np.diag(sz) - np.outer(sz, sz)