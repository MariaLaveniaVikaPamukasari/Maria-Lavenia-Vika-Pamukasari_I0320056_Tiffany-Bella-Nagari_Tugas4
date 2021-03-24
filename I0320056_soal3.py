# Program Pemeriksaan Berat Bagasi Lion Air JT908
# Mulai
print("\t\t\tSelamat datang di konter pemeriksaan berat bagasi Lion Air JT908")
# Menginput berat dalam Kg
# Mengubah lbs menjadi Kg
a = 0.45
b = a * 60
print("\nBerat maksimum untuk 1 orang pernumpang adalah",b,"Kg")
print("Silahkan masukkan berat bagasi Anda dalam Kg")
ab = int(input("Masukkan berat bagasi Anda:"))
if ab > 27 :
    print("Berat bagasi Anda melebihi batas maksimum")
    print("Silahkan mengurangi barang bawaan Anda atau membayar biaya tambahan")
else :
    print("Barang bawaan Anda tidak melebihi batas maksimum")
    print("Silahkan menuju ruang tunggu")

print("\n\t\t\tTerimakasih atas kerja samanya")
input("Tekan enter untuk kembali")