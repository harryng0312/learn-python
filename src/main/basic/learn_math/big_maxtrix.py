import numpy as np
import datetime as dt

file1Path = "data/matrix/mat1.txt"
file2Path = "data/matrix/mat2.txt"
matSize = 16_384

def generate_square_maxtrix(n: int) -> np.matrix :
    m1 = np.random.randint(low=-128, high=127, size=(n, n))
    return m1

def save_matrix(filepath: str, mat: np.matrix) -> None:
    np.savetxt(fname=filepath, X=mat, fmt="%d")

def load_matrix(filepath: str) -> np.matrix:
    return np.loadtxt(fname=filepath, dtype=int)


def mulMatrix(mat1: np.ndarray, mat2: np.ndarray) -> np.ndarray:
    rs: np.ndarray = np.ndarray(shape=(matSize, matSize))
    for i in range(0,len(mat1)):
        temp: int = []
        for j in range(0,len(mat2[0])):
            s = 0
            for k in range(0,len(mat1[0])):
                s += mat1[i][k]*mat2[k][j]
            temp.append(s)
        rs[i] = temp
    return rs

# mat1 = generate_square_maxtrix(matSize)
# save_matrix(file1Path, mat1)

# mat2 = generate_square_maxtrix(matSize)
# save_matrix(file2Path, mat2)

startLoadTime = dt.datetime = dt.datetime.now();
mat1 = load_matrix(file1Path)
mat2 = load_matrix(file2Path)
endLoadTime = dt.datetime = dt.datetime.now();
print(f"Load done in {endLoadTime - startLoadTime}...")

mat1Arr: np.ndarray = np.array(copy=False, dtype=int, object=mat1)
mat2Arr: np.ndarray = np.array(copy=False, dtype=int, object=mat2)
# print(f"{type(np.array(copy=False, dtype=int, object=mat1))}")
startTime: dt.datetime = dt.datetime.now();
# matRs = mulMatrix(mat1Arr, mat2Arr)
endTime: dt.datetime = dt.datetime.now();
# print(f"{str(matRs)}")
print(f"python time:{(endTime - startTime)}")

startTime: dt.datetime = dt.datetime.now();
matRs = mat1 * mat2
endTime: dt.datetime = dt.datetime.now();

print(f"{str(matRs)}")
print(f"native python time:{(endTime - startTime)}")