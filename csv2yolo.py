import csv
import os

def convert_coordinates(size, box):
    """
    YOLO formatına dönüştürmek için koordinatları yeniden boyutlandırır.
    """
    dw = 1.0 / size[0]
    dh = 1.0 / size[1]
    # YOLO formatında x, y koordinatlarını hesaplar
    x = (box[0] + box[1]) / 2.0
    y = (box[2] + box[3]) / 2.0
    # YOLO formatında genişlik ve yüksekliği hesaplar
    w = box[1] - box[0]
    h = box[3] - box[2]
    # YOLO formatına dönüştürülmüş koordinatları ve boyutları döndürür
    x = x * dw
    w = w * dw
    y = y * dh
    h = h * dh
    return (x, y, w, h)

def convert_csv_to_yolo(csv_file, output_folder):
    """
    CSV dosyasındaki verileri YOLO formatına dönüştürür.
    """
    with open(csv_file, 'r') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            # Satırdan nesnenin bilgilerini al
            image_path = row[1]
            label = row[-1]
            # YOLO formatında sınıf etiketlerini ve koordinatları al
            class_id = 0 if label == "is_bee" else 1 if label == "is_wasp" else 2 if label == "is_otherinsect" else 3
            bbox = (0, 1, 0, 1)  # Koordinatları örneğin (xmin, xmax, ymin, ymax) olarak alabilirsiniz
            yolo_box = convert_coordinates((640, 480), bbox)  # Görüntü boyutunu (genişlik, yükseklik) olarak belirtin
            # Dosyaya yazmak için çıktı yolu oluştur
            output_path = os.path.join(output_folder, os.path.splitext(os.path.basename(image_path))[0] + ".txt")
            # YOLO formatındaki koordinatları ve sınıf etiketlerini dosyaya yaz
            with open(output_path, 'a') as out_file:
                out_file.write(f"{class_id} {' '.join([str(coord) for coord in yolo_box])}\n")

# Kullanımı örnek olarak göstermek için
csv_file = "C:\\Users\\Bedirhan\\Desktop\\Kaggle_egitim\\kaggle_bee_vs_wasp\\labels.csv"  # dönüştürmek istediğiniz .csv dosyasının adını buraya yazın
output_folder = "C:\\Users\\Bedirhan\\Desktop\\Kaggle_egitim\\kaggle_bee_vs_wasp\\validation\yolo"  # YOLO formatında çıktı dosyalarının kaydedileceği klasörün adını buraya yazın
convert_csv_to_yolo(csv_file, output_folder)
