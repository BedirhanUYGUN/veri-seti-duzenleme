import os

def rename_files(folder1, folder2):
    """
    İki klasördeki dosyaların isimlerini sıralı bir şekilde yeniden adlandırır.
    """
    # Her iki klasördeki dosya listelerini al
    files1 = sorted(os.listdir(folder1))
    files2 = sorted(os.listdir(folder2))
    
    # Her iki klasördeki dosyalar için sıralı bir şekilde yeniden adlandırma işlemi yap
    for i, (file1, file2) in enumerate(zip(files1, files2), start=1):
        # Dosya uzantısını al
        ext = os.path.splitext(file1)[-1]
        # Yeni dosya adını oluştur
        new_name1 = f"{i}{ext}"
        new_name2 = f"{i}.txt"
        # Yeni adları ile eski dosyaları yeniden adlandır
        os.rename(os.path.join(folder1, file1), os.path.join(folder1, new_name1))
        os.rename(os.path.join(folder2, file2), os.path.join(folder2, new_name2))
        print(f"{file1} -> {new_name1}")
        print(f"{file2} -> {new_name2}")

# Kullanımı örnek olarak göstermek için
folder1 = "C:\\Users\\Bedirhan\\Desktop\\Kaggle_egitim\\kaggle_bee_vs_wasp\\deneme1"  # İlk klasör
folder2 = "C:\\Users\\Bedirhan\\Desktop\\Kaggle_egitim\\kaggle_bee_vs_wasp\\deneme2"  # İkinci klasör
rename_files(folder1, folder2)
