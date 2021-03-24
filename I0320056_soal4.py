# Program Pengujian Spesifikasi Kursus Mobil Online
#Mulai
print("\t\t\tSelamat datang di Mobiline")
print("\t\t\tBelajar bisa,Bisa belajar,Saya bisa")

a = input("\nSiapakah nama Anda? :")
print("Nama Anda adalah",a)
b = int(input("Berapa usia Anda? :"))
print("Usia Anda adalah",b,"tahun")
if b < 21 :
    print("\nMaaf Anda terlalu muda untuk masuk ke sini")
    input("Silahkan tekan enter untuk melanjutkan")
else :
    print("\nUsia Anda telah mencukupi, silahkan masuk")

print("\n\t\t\tSelamat datang di tahap selanjutnya")
ab = str(input("Apakah Anda telah lulus ujian kualifikasi MobiLine? Yes/No :"))
if ab == "Yes":
    print("Selamat", a,"!","Anda dapat mendaftar kursus ini")
    input("Silahkan tekan enter untuk kembali")
else :
    print("Anda tidak dapat mendaftar kursus ini")
    input("Silahkan tekan enter untuk kembali")
#Selesai