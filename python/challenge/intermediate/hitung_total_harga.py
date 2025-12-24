items = [
    {"harga": 10000, "qty": 2},
    {"harga": "5000", "qty": 3},
    {"harga": "abc", "qty": 1}
]

def total_harga(barang):
    total_seluruh = 0

    for item in barang:
        try:
            harga = int(item["harga"])
            jumlah = item["qty"]

            total_seluruh += harga * jumlah
            
        except (ValueError, KeyError):
            continue
        
    return f"Total: {total_seluruh}"

print(total_harga(items))