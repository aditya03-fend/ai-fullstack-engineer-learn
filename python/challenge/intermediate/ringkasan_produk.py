products = [
    {"nama": "Laptop", "stok": 5},
    {"nama": "Mouse", "stok": 0},
    {"nama": "Keyboard"}
]

def ringkas_produk(produk):
    ringkasan = []
    for item in produk:
        try:
            stok = item.get("stok")

            if stok is None:
                ringkasan.append(f"{item["nama"]}: stok tidak di ketahui")
            elif stok > 0:
                ringkasan.append(f"{item["nama"]}: Tersedia")
            else:
                ringkasan.append(f"{item["nama"]}: Habis")
        except ValueError:
            ringkasan.append(f"{item.get('nama', 'Unknown')}: Error terjadi")
    return ringkasan

print(ringkas_produk(products))