Trong Faster R-CNN, quá trình huấn luyện bao gồm nhiều giai đoạn khác nhau, với mỗi giai đoạn sử dụng các nhãn (labels) khác nhau để tối ưu hóa các phần của mạng. Mạng Faster R-CNN gồm ba thành phần chính: Backbone (mạng trích xuất đặc trưng), Region Proposal Network (RPN), và Region of Interest (RoI) Head. Dưới đây là cách các nhãn được sử dụng cho từng thành phần trong quá trình huấn luyện:

1. Backbone (Mạng trích xuất đặc trưng)
- Vai trò: Trích xuất các đặc trưng từ hình ảnh đầu vào. Backbone có thể là một mạng đã được tiền huấn luyện như ResNet, VGG, hoặc MobileNet.
- Sử dụng nhãn: Backbone không trực tiếp sử dụng nhãn cho việc huấn luyện. Thay vào đó, nó chuyển đổi hình ảnh đầu vào thành bản đồ đặc trưng (feature map) và cung cấp cho các thành phần khác của Faster R-CNN.

2. Region Proposal Network (RPN)
- Vai trò: Dự đoán các hộp đề xuất (region proposals) mà có khả năng chứa đối tượng trong ảnh.
- Sử dụng nhãn: RPN sử dụng các nhãn để xác định xem mỗi anchor (hộp ban đầu với kích thước và tỷ lệ cố định) là “đối tượng” hay “nền”.
- Nhãn cho RPN: RPN sử dụng hai loại nhãn:
- Nhãn nhị phân (binary labels): Để xác định xem mỗi anchor là một “foreground” (đối tượng, nếu nó trùng với một hộp ground-truth nhất định với IoU ≥ 0.7) hay “background” (nền, nếu IoU ≤ 0.3 với bất kỳ hộp ground-truth nào).
- Hộp điều chỉnh (bounding box regression targets): Các hộp đề xuất được điều chỉnh sao cho khớp chính xác với các hộp ground-truth tương ứng.

3. RoI Pooling (Region of Interest Pooling)
- Vai trò: Tích hợp các đặc trưng từ các hộp đề xuất vào một kích thước cố định (đầu ra từ backbone có thể có kích thước khác nhau).
- Sử dụng nhãn: RoI Pooling không yêu cầu nhãn để huấn luyện. Nó chỉ áp dụng pooling trên các vùng đặc trưng của bản đồ đặc trưng theo các hộp đề xuất từ RPN.

4. Region of Interest (RoI) Head
- Vai trò: Dự đoán lớp của mỗi hộp đề xuất (classification) và điều chỉnh lại các hộp đề xuất (bounding box regression).
- Sử dụng nhãn: RoI Head sử dụng các nhãn để huấn luyện hai nhánh:
- Nhánh phân loại (classification branch): Sử dụng các nhãn lớp của các hộp ground-truth để phân loại các hộp đề xuất.
- Nhánh điều chỉnh hộp (bounding box regression branch): Sử dụng các nhãn hộp điều chỉnh (bounding box targets) từ các hộp ground-truth để tinh chỉnh các hộp đề xuất cuối cùng.

Tóm tắt quá trình sử dụng nhãn
- RPN: Sử dụng nhãn nhị phân (foreground/background) và hộp điều chỉnh để huấn luyện các hộp đề xuất.
- RoI Head: Sử dụng các nhãn lớp cho việc phân loại và nhãn hộp điều chỉnh để tinh chỉnh các hộp cuối cùng.

Trong quá trình huấn luyện, Faster R-CNN kết hợp các mục tiêu (loss) khác nhau, bao gồm loss của RPN (classification và bounding box regression) và loss của RoI Head (classification và bounding box regression) để tối ưu hóa toàn bộ mô hình.