# Contoh
user = {
    "nama": "Ndok",
    "umur": 20,
    "is_admin": False
}




# Akses Data
print(user["nama"])
print(user["umur"])

# aman
print(user.get("email"))



# Mengubah & Menambah Dict
user["umur"] = 21
user["email"] = "ndok@email.com"


# Operasi Penting
user.keys()
user.values()
user.items()

