import cv2
import os
import numpy as np
def adjust_and_save_images(input_folder, output_folder, saturation_factor):
    # Giriş klasöründeki dosyaları listele
    file_list = os.listdir(input_folder)
    
    # Sadece resim dosyalarını al
    image_files = [f for f in file_list if f.endswith(('.jpg', '.jpeg', '.png'))]
    
    # Çıktı klasörünü oluştur
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    # Her bir resmi işle, doygunluğunu ayarla ve yeni klasöre kaydet
    for filename in image_files:
        input_path = os.path.join(input_folder, filename)
        output_path = os.path.join(output_folder, filename)
        
        # Resmi yükle
        image = cv2.imread(input_path)
        
        # Doygunluğunu ayarla
        adjusted_image = adjust_saturation(image, saturation_factor)
        
        # Resmi yeni klasöre kaydet
        cv2.imwrite(output_path, adjusted_image)

def adjust_saturation(image, factor):
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    hsv[:,:,1] = np.clip(hsv[:,:,1] * factor, 0, 255).astype(np.uint8)
    return cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)

# Kullanım örneği:
input_folder = "C:\\Users\\Bedirhan\\Desktop\\Python\\resim"
output_folder = "C:\\Users\\Bedirhan\\Desktop\\Python\\resim_2"
saturation_factor = 100  # Doygunluk faktörü

adjust_and_save_images(input_folder, output_folder, saturation_factor)
