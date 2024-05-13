import xml.etree.ElementTree as ET
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

def convert_xml_to_yolo(xml_file, output_folder):
    """
    XML dosyasındaki verileri YOLO formatına dönüştürür.
    """
    tree = ET.parse(xml_file)
    root = tree.getroot()
    # Sınıf etiketlerini ve ID'leri eşleştirmek için bir sözlük oluştur
    class_labels = {
        "is_bee": 0,
        "is_wasp": 1,
        "is_otherinsect": 2,
        "is_other": 3
    }
    # XML dosyasındaki her nesne için dön
    for obj in root.findall('object'):
        # Nesnenin sınıf etiketini al
        label = obj.find('label').text
        # Yalnızca belirtilen sınıf etiketleri varsa devam et
        if label in class_labels:
            # Nesnenin sınıf etiketinin YOLO numarasını al
            class_id = class_labels[label]
            # Nesnenin koordinatlarını al
            bbox = obj.find('bbox')
            # Koordinatları YOLO formatına dönüştür
            b = (float(bbox.find('xmin').text), float(bbox.find('xmax').text), float(bbox.find('ymin').text), float(bbox.find('ymax').text))
            image_size = (640, 480) # Örneğin, görüntü boyutunu (genişlik, yükseklik) olarak alabilirsiniz.
            yolo_box = convert_coordinates(image_size, b)
            # Dosya adını al
            file_name = root.find('path').text.split("/")[-1].split(".")[0] + ".txt"
            # Dosyaya yazmak için çıktı yolu oluştur
            output_path = os.path.join(output_folder, file_name)
            # YOLO formatındaki koordinatları ve sınıf etiketlerini dosyaya yaz
            with open(output_path, 'a') as out_file:
                out_file.write(f"{class_id} {' '.join([str(coord) for coord in yolo_box])}\n")

# Kullanımı örnek olarak göstermek için
xml_file = "C:\\Users\\Bedirhan\\Desktop\\Kaggle_egitim\\kaggle_bee_vs_wasp\\labels.xml"  # dönüştürmek istediğiniz .xml dosyasının adını buraya yazın
output_folder = "C:\\Users\\Bedirhan\\Desktop\\Kaggle_egitim\\kaggle_bee_vs_wasp\\validation\\yolo"  # YOLO formatında çıktı dosyalarının kaydedileceği klasörün adını buraya yazın
convert_xml_to_yolo(xml_file, output_folder)
