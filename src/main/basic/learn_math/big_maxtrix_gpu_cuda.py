import numpy as np
import cupy as cp
import cupyx as cpx
import datetime as dt
import io

FILE_MAT_NAME_1 = "data/matrix/mat1"
FILE_MAT_NAME_2 = "data/matrix/mat2"
FILETXT_MAT_NAME_1 = "data/matrix/mat1.txt"
FILETXT_MAT_NAME_2 = "data/matrix/mat2.txt"
MAT_SIZE = 2048

def generate_square_maxtrix(n: int) -> np.matrix :
    m1 = np.random.randint(low=-128, high=127, size=(n, n))
    return m1

def save_matrix(filepath: str, mat: np.matrix) -> None:
    # np.savetxt(fname=filepath, X=mat, fmt="%d")
    file: io.FileIO = None
    try:
        file = open(file=filepath, mode="bw")
        np.save(file=file, arr=np.array(object=mat, dtype=int))
    finally:
        if file is not None:
            file.close()

def load_matrix(filepath: str) -> np.matrix:
    result: np.matrix = None
    file: io.FileIO = None
    try:
        file = open(file=filepath, mode="br")
        result = np.matrix(data=np.load(file=filepath, fix_imports=True), dtype=int)
    finally:
        if file is not None:
            file.close()
    return result

def savetxt_matrix(filepath: str, mat: np.matrix) -> None:
    np.savetxt(fname=filepath, X=mat, fmt="%d")

def loadtxt_matrix(filepath: str) -> np.matrix:
    return np.matrix(data=np.loadtxt(fname=filepath, dtype=int), dtype=int)
    
def mulMatrix(mat1: cp.ndarray, mat2: cp.ndarray) -> cp.ndarray:
    rs: cp.ndarray = cp.matmul(mat1, mat2)
    return rs

# mat1 = generate_square_maxtrix(MAT_SIZE)
# save_matrix(filepath=FILE_MAT_NAME_1, mat=mat1)
# savetxt_matrix(filepath=FILETXT_MAT_NAME_1, mat=mat1)

# mat2 = generate_square_maxtrix(MAT_SIZE)
# save_matrix(filepath=FILE_MAT_NAME_2, mat=mat2)
# savetxt_matrix(filepath=FILETXT_MAT_NAME_2, mat=mat2)

startLoadTime = dt.datetime = dt.datetime.now()
# mat1 = load_matrix(FILE_MAT_NAME_1)
# mat2 = load_matrix(FILE_MAT_NAME_2)
mat1 = loadtxt_matrix(FILETXT_MAT_NAME_1)
mat2 = loadtxt_matrix(FILETXT_MAT_NAME_2)
endLoadTime = dt.datetime = dt.datetime.now()
print(f"Load done in {endLoadTime - startLoadTime}...")
print(f"mat1 {type(mat1)}:\n{mat1}\nmat2 {type(mat2)}:\n{mat2}")

mat1Arr: np.ndarray = np.array(copy=False, dtype=int, object=mat1)
mat2Arr: np.ndarray = np.array(copy=False, dtype=int, object=mat2)


print(f"runtime info: {cpx.get_runtime_info()}")
# mat1cpArr = cp.array(obj=mat1Arr, dtype=int)
# mat2cpArr = cp.array(obj=mat2Arr, dtype=int)
mat1cpArr = cp.asarray(a=mat1Arr, dtype=int)
mat2cpArr = cp.asarray(a=mat2Arr, dtype=int)
startTime: dt.datetime = dt.datetime.now();
# matRs = mat1 * mat2
matRs1 = mulMatrix(mat1cpArr, mat2cpArr)
endTime: dt.datetime = dt.datetime.now();
matRs = np.matrix(data=cp.asnumpy(a=matRs1), copy=False)

print(f"Result by CUDA GPU:\n{str(matRs)}")
print(f"Run on CUDA GPU time:{(endTime - startTime)}")