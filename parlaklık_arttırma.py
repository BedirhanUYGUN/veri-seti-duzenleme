import cv2
import os

def adjust_brightness(image, brightness_factor):
    """
    Bir gri renkli fotoğrafın parlaklığını ayarlar.

    Parameters:
        image: numpy array
            Gri renkli fotoğraf.
        brightness_factor: float
            Parlaklık faktörü. Daha büyük bir değer daha parlak bir görüntü sağlar.

    Returns:
        brightened_image: numpy array
            Parlak görüntü.
    """
    # Parlaklık faktörünü kullanarak parlaklık ayarla
    brightened_image = cv2.convertScaleAbs(image, alpha=brightness_factor, beta=0)
    
    return brightened_image

def adjust_brightness_of_images(input_folder, output_folder, brightness_factor):
    # Giriş klasöründeki dosyaları listele
    file_list = os.listdir(input_folder)
    
    # Sadece resim dosyalarını al
    image_files = [f for f in file_list if f.endswith(('.jpg', '.jpeg', '.png'))]
    
    # Çıktı klasörünü oluştur
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    # Her bir resmin parlaklığını ayarla ve yeni klasöre kaydet
    for filename in image_files:
        input_path = os.path.join(input_folder, filename)
        output_path = os.path.join(output_folder, filename)
        
        # Resmi yükle
        image = cv2.imread(input_path, cv2.IMREAD_GRAYSCALE)  # Gri renkli fotoğrafı yükle
        
        # Parlaklığı ayarla
        brightened_image = adjust_brightness(image, brightness_factor)
        
        # Resmi yeni klasöre kaydet
        cv2.imwrite(output_path, brightened_image)

# Kullanım örneği:
input_folder = "C:\\Users\\Bedirhan\\Desktop\\Python\\resim"
output_folder = "C:\\Users\\Bedirhan\\Desktop\\Python\\resim_3"
brightness_factor = 1.5 # Parlaklık faktörü

adjust_brightness_of_images(input_folder, output_folder, brightness_factor)
