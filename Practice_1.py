#           Mindset

# Misalkan kamu ingin membuat robot sederhana yang bisa:
# → Menerima NAMA seseorang
# → Mengucapkan salam kepada orang tersebut

# Sebagai MANUSIA, kalau kamu disuruh lakukan ini:
# 1. Orang bilang namanya: "Andi"
# 2. Kamu ingat nama itu
# 3. Kamu ucapkan: "Halo Andi! Senang bertemu!"

# Nah, sekarang ganti "Kamu" dengan "KOMPUTER".
# Komputer butuh instruksi yang ditulis dalam Bahasa Python.



#           Let's begin!
nama = "Rajif"

print(f'Halo {nama}!')

print('Selamat belajar programming!')
#           Berhasil dijalankan!
# Output:
# Halo Rajif!
# Selamat belajar programming!



#           Explanation
# Baris 1
# nama = nama variabel (label kotak penyimpanan)
# "Rajif" = nilai/isi yang disimpan
#       Analogi: 
# kotak kosong dinamai {nama}, 
# lalu dimasukkan kertas bertulis "Rajif" ke dalamnya dan disimpan

# Baris 3
# print = berfungsi MENAMPILAKN teks ke layar
# f'...' = f-string, membuka kotak variabel dan mengambil isinya
# {...} = variabel yang akan diganti dengan isinya (karena ada f-string)

#   Lebih detail tentang f-string
# 'Halo {nama}!' akan menampilkan Halo {nama} ,
# karena tidak ada f -> teks ditampilkan APA ADANYA
# f'Halo{nama}' akan menampilkan Halo Rajif! ,
# karena ada f -> {nama} DIGANTI dengan nilai variabel
# f = format -> memberitahu python: ada variabel di dalam kurungawat,
#                                   ganti dengan nilainya!

# Lebih detail tentang tanda = (sama dengan)
# = adalah tanda ASSIGNMENT (penyimpanan), 
# artinya: simpan nilai di KANAN ke variabel di KIRI