# Akses Data ======================================================================================
print(user["nama"])
print(user["umur"])

# aman
print(user.get("email"))

# Mengubah & Menambah Dict ======================================================================================
user["umur"] = 21
user["email"] = "ndok@email.com"

# Operasi Penting ======================================================================================
user.keys()
user.values()
user.items()

# keys() ======================================================================================
print(user.keys()) # dict_keys(['nama', 'umur', 'is_admin'])

# values() ======================================================================================
print(user.values()) # dict_values(['Ndok', 20, False])

# items() ======================================================================================
print(user.items()) # dict_items([('nama', 'Ndok'), ('umur', 20), ('is_admin', False)])
