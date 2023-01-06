import numpy as np


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
    print(f"Kết quả: \n{rs}")
    print(f"Dạng ma trận: {rs.shape}")
    print(f"Kiểu dữ liệu: {rs.dtype}")
    print(f"Số chiều: {rs.ndim}")
    print(f"Ma trận chuyển vị: {rs.T}")
    print(f"Phần ảo: {rs.imag}")
    print(f"Số lượng phần tử: {rs.size}")
    print(f"Kích thước mỗi phần tử (bytes): {rs.itemsize}")

print_matrix()