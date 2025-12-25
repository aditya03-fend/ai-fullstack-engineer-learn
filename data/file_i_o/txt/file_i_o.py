# Kode membaca file
file = open("data.txt", "r")
isi = file.read()
file.close()

# Menulis file
file = open("hasil.txt", "w")
file.write("Ini hasil proses AI")
file.close()

# menambah file
file = open("log.txt", "a")
file.write("\nTraining selesai")
file.close()

# Cara yang benar dan aman
with open("data.txt", "r") as file:
    isi = file.read()
    print(isi)

# membaca per baris
with open("data.txt", "r") as file:
    for baris in file:
        print(baris.strip())
