import cv2
import os
import numpy as np

def add_noise(image, noise_factor):
    """
    Bir gri renkli fotoğrafa gürültü ekler.

    Parameters:
        image: numpy array
            Gri renkli fotoğraf.
        noise_factor: float
            Gürültü faktörü. Daha büyük bir değer daha fazla gürültü ekler.

    Returns:
        noisy_image: numpy array
            Gürültülü fotoğraf.
    """
    # Gürültü eklemek için rastgele piksel değerleri oluştur
    noise = np.random.normal(loc=0, scale=noise_factor, size=image.shape)
    
    # Gürültüyü resme ekle
    noisy_image = np.clip(image + noise, 0, 255).astype(np.uint8)
    
    return noisy_image

def add_noise_to_images(input_folder, output_folder, noise_factor):
    # Giriş klasöründeki dosyaları listele
    file_list = os.listdir(input_folder)
    
    # Sadece resim dosyalarını al
    image_files = [f for f in file_list if f.endswith(('.jpg', '.jpeg', '.png'))]
    
    # Çıktı klasörünü oluştur
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    # Her bir resme gürültü ekle ve yeni klasöre kaydet
    for filename in image_files:
        input_path = os.path.join(input_folder, filename)
        output_path = os.path.join(output_folder, filename)
        
        # Resmi yükle
        image = cv2.imread(input_path, cv2.IMREAD_GRAYSCALE)  # Gri renkli fotoğrafı yükle
        
        # Gürültü ekle
        noisy_image = add_noise(image, noise_factor)
        
        # Resmi yeni klasöre kaydet
        cv2.imwrite(output_path, noisy_image)

# Kullanım örneği:
input_folder = "C:\\Users\\Bedirhan\\Desktop\\Python\\resim"
output_folder = "C:\\Users\\Bedirhan\\Desktop\\Python\\resim_2"
noise_factor = 30  # Gürültü faktörü

add_noise_to_images(input_folder, output_folder, noise_factor)
