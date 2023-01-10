from concurrent.futures import ProcessPoolExecutor, Executor, ThreadPoolExecutor, wait, Future
from multiprocessing import get_context, Queue, Manager
from multiprocessing.context import BaseContext

import numpy as np

def mulMatrix(mat1: np.ndarray, mat2: np.ndarray) -> np.ndarray:
    rs: np.ndarray = np.ndarray(shape=(mat1.shape[0], mat2.shape[1]), dtype=int)
    for i in range(0, len(mat1)):
        for j in range(0, len(mat2[0])):
            s = 0
            for k in range(0, len(mat1[0])):
                s += mat1[i][k]*mat2[k][j]
            rs[i, j] = s
    return rs

def calculateMulAndSum(rs: np.ndarray, m1: np.ndarray, m2: np.ndarray, row_no: int, col_no: int) -> None:
    total: int = 0
    for k in range(0, len(m1[0])):
        total += m1[row_no, k] * m2[k, col_no]
    # with ctx.Lock():
    #     queue.put((row_no, col_no, total))
    # return queue
    # rs = ctx.Value("b")
    rs[row_no, col_no] = total
    # print(f"Rs id:{id(rs)}\n{rs}")

def mulMatrixParallel(mat1: np.ndarray, mat2: np.ndarray, threadCount: int = 4) -> np.ndarray:
    context = get_context('fork') # spawn, fork, forkserver
    with ProcessPoolExecutor(max_workers=threadCount, mp_context=context) as executor:
        rs: np.ndarray = np.ndarray(shape=(mat1.shape[0], mat2.shape[1]), dtype=int)
        # queue = context.Queue(mat1.shape[0] * mat2.shape[1])
        # queue = Queue(mat1.shape[0] * mat2.shape[1])
        # chunkSize = (mat1.shape[0] * mat2.shape[1]) // threadCount
        resultArr: list[Future] = []
        for i in range(0, len(mat1)):
            for j in range(0, len(mat2[0])):
                # calculateMulAndSum(rs, mat1, mat2, i, j)
                # fut = executor.map(calculateMulAndSum, [rs], [mat1], [mat2], [i], [j])
                with context.Lock():
                    fut: Future = executor.submit(calculateMulAndSum, rs, mat1, mat2, i, j)
                    resultArr.append(fut)
        wait(fs=resultArr)
    return rs


def print_matrix():
    m1 = np.matrix([
        [2, 3, 4],
        [1, 0, 0]
    ])
    m2 = np.matrix([
        [0, 1000],
        [1, 100],
        [0, 10]
    ])
    rs = m1 * m2
    # rs = mulMatrixParallel(mat1=np.array(copy=False, dtype=int, object=m1),
    #                mat2=np.array(copy=False, dtype=int, object=m2))
    # rs = np.matrix(rs)
    print(f"Kết quả: \n{rs}")
    print(f"Dạng ma trận: {rs.shape}")
    print(f"Kiểu dữ liệu: {rs.dtype}")
    print(f"Số chiều: {rs.ndim}")
    print(f"Ma trận chuyển vị: {rs.T}")
    print(f"Phần ảo: {rs.imag}")
    print(f"Số lượng phần tử: {rs.size}")
    print(f"Kích thước mỗi phần tử (bytes): {rs.itemsize}")


print_matrix()
