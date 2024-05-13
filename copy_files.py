import os
import shutil

def find_and_copy_txt_files(photo_folder, txt_folder, target_folder):
    """
    Belirtilen fotoğraf ve .txt klasörlerinde aynı isme sahip .txt dosyalarını bulur ve hedef klasöre kopyalar.
    """
    # Hedef klasördeki tüm dosyaları listeler
    target_files = os.listdir(target_folder)
    
    # Fotoğraf klasöründeki her fotoğraf dosyası için işlem yap
    for filename in os.listdir(photo_folder):
        # Dosya adını kontrol etmek için .txt uzantısını ekleyin
        txt_filename = os.path.splitext(filename)[0] + ".txt"
        # Eğer txt klasöründe bu isimde bir .txt dosyası varsa, hedef klasöre kopyala
        if txt_filename in os.listdir(txt_folder):
            source_path = os.path.join(txt_folder, txt_filename)
            target_path = os.path.join(target_folder, txt_filename)
            # Dosyayı kopyala
            shutil.copyfile(source_path, target_path)
            print(f"{txt_filename} kopyalandı.")

# Kullanımı örnek olarak göstermek için
photo_folder = "C:\\Users\\Bedirhan\\Desktop\\Kaggle_egitim\\kaggle_bee_vs_wasp\\deneme1"  # Fotoğrafların bulunduğu klasör
txt_folder = "C:\\Users\\Bedirhan\\Desktop\\Kaggle_egitim\\kaggle_bee_vs_wasp\\validation\yolo"  # .txt dosyalarının bulunduğu klasör
target_folder = "C:\\Users\\Bedirhan\\Desktop\\Kaggle_egitim\\kaggle_bee_vs_wasp\\deneme2"  # Kopyalanacak .txt dosyalarının hedef klasörü
find_and_copy_txt_files(photo_folder, txt_folder, target_folder)
