import numpy as np

# Dosya yolunu düzeltin (r"..." veya diğer yöntemlerle)
dosya_yolu = r"C:\Users\user\OneDrive\Masaüstü\123\original_matrix.npy"

# Dosyayı yükleyin
veri = np.load(dosya_yolu)

# Veriyi inceleyin
print("Veri türü:", type(veri))
print("Veri içeriği:", veri)
