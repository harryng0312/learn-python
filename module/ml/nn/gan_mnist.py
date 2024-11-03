import numpy as np
import matplotlib.pyplot as plt
from tensorflow.keras.datasets import mnist
from tensorflow.keras import layers, models, optimizers

# Tải dữ liệu MNIST
(X_train, y_train), (_, _) = mnist.load_data()
X_train = (X_train.astype(np.float32) - 127.5) / 127.5  # Chuẩn hóa về [-1, 1]
X_train = np.expand_dims(X_train, axis=-1)  # Thêm chiều cho kênh màu
y_train = y_train.astype(np.float32)

# Định nghĩa các tham số
latent_dim = 100
num_classes = 10

# Xây dựng Generator
def build_generator():
    model = models.Sequential()
    model.add(layers.Input(shape=(latent_dim + num_classes,)))  # Kết hợp vector ngẫu nhiên với nhãn
    model.add(layers.Dense(256, activation='relu'))
    model.add(layers.Dense(512, activation='relu'))
    model.add(layers.Dense(1024, activation='relu'))
    model.add(layers.Dense(28 * 28, activation='tanh'))  # Hình ảnh 28x28
    model.add(layers.Reshape((28, 28, 1)))
    return model

# Xây dựng Discriminator
def build_discriminator():
    model = models.Sequential()
    model.add(layers.Input(shape=(28, 28, 1)))
    model.add(layers.Flatten())
    model.add(layers.Dense(512, activation='relu'))
    model.add(layers.Dense(256, activation='relu'))
    model.add(layers.Dense(1, activation='sigmoid'))  # Phân loại thật giả
    return model

# Khởi tạo mô hình
generator = build_generator()
discriminator = build_discriminator()

# Biên dịch Discriminator
discriminator.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

# Kết hợp Generator và Discriminator
discriminator.trainable = False  # Không huấn luyện Discriminator khi huấn luyện GAN
gan_input = layers.Input(shape=(latent_dim + num_classes,))
fake_image = generator(gan_input)
gan_output = discriminator(fake_image)

gan = models.Model(gan_input, gan_output)
gan.compile(loss='binary_crossentropy', optimizer='adam')

# Huấn luyện cGAN
def train(epochs=10000, batch_size=128):
    for epoch in range(epochs):
        # Lấy một batch dữ liệu
        idx = np.random.randint(0, X_train.shape[0], batch_size)
        real_images = X_train[idx]
        real_labels = y_train[idx]

        # Tạo nhãn cho dữ liệu thật và giả
        real_labels_for_discriminator = np.ones((batch_size, 1))
        noise = np.random.normal(0, 1, (batch_size, latent_dim))
        sampled_labels = np.random.randint(0, num_classes, batch_size)
        sampled_labels_one_hot = np.zeros((batch_size, num_classes))
        sampled_labels_one_hot[np.arange(batch_size), sampled_labels] = 1

        # Tạo hình ảnh giả
        generator_input = np.concatenate([noise, sampled_labels_one_hot], axis=1)
        fake_images = generator.predict(generator_input)
        fake_labels_for_discriminator = np.zeros((batch_size, 1))

        # Huấn luyện Discriminator
        d_loss_real = discriminator.train_on_batch(real_images, real_labels_for_discriminator)
        d_loss_fake = discriminator.train_on_batch(fake_images, fake_labels_for_discriminator)
        d_loss = 0.5 * np.add(d_loss_real, d_loss_fake)

        # Huấn luyện Generator
        g_loss = gan.train_on_batch(generator_input, real_labels_for_discriminator)

        # In ra kết quả mỗi 1000 epoch
        if epoch % 1000 == 0:
            print(f"{epoch} [D loss: {d_loss[0]:.4f}, acc.: {100 * d_loss[1]:.2f}%] [G loss: {g_loss:.4f}]")

# Bắt đầu huấn luyện
train()

# Hàm tạo hình ảnh từ số điều kiện
def generate_images(condition_labels, n=10):
    noise = np.random.normal(0, 1, (n, latent_dim))
    condition_labels_one_hot = np.zeros((n, num_classes))
    condition_labels_one_hot[np.arange(n), condition_labels] = 1
    generator_input = np.concatenate([noise, condition_labels_one_hot], axis=1)
    generated_images = generator.predict(generator_input)

    # Hiển thị hình ảnh
    plt.figure(figsize=(n, 1))
    for i in range(n):
        plt.subplot(1, n, i + 1)
        plt.imshow(generated_images[i, :, :, 0], cmap='gray')
        plt.axis('off')
    plt.show()

# Tạo hình ảnh cho số điều kiện từ 0 đến 9
generate_images(condition_labels=np.arange(10))