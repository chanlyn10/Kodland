import random

# Daftar karakter yang bisa digunakan dalam password
elements = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

# Meminta pengguna untuk memasukkan panjang password
pass_length = int(input("Enter pass length: "))

# Membuat password kosong
password = ""

# Mengambil karakter acak dari elements sebanyak pass_length
for i in range(pass_length):
    password += random.choice(elements)

# Menampilkan hasil password yang dibuat
print(password)
