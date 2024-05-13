import os

def rename_files(folder_path):
    # Klasördeki dosyaları listele
    file_list = os.listdir(folder_path)
    
    # Sadece resim dosyalarını (jpg, png, vb.) al
    image_files = [f for f in file_list if f.endswith(('.jpg', '.jpeg', '.png'))]
    
    # Dosyaları sırala
    image_files.sort()
    
    # Dosya adlarını değiştir
    for i, filename in enumerate(image_files):
        new_filename = f"{i+76}.jpg"  # Yeni dosya adı
        os.rename(os.path.join(folder_path, filename), os.path.join(folder_path, new_filename))

#Kullanım örneği:
#Klasör yolunu belirt
folder_path = "C:\\Users\\Bedirhan\\Desktop\\Python\\resim_2"
rename_files(folder_path)