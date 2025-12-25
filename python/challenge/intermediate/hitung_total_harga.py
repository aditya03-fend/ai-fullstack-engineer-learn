def hitung_item(item: dict) -> int:
    """Helper function untuk menghitung subtotal satu item secara aman."""
    try:
        # Menghitung langsung tanpa simpan ke variabel perantara
        return int(item["harga"]) * int(item.get("qty", 0))
    except (ValueError, TypeError, KeyError):
        return 0

def total_harga_pro(barang: list) -> str:
    # Menggunakan sum() dengan generator expression
    total = sum(hitung_item(item) for item in barang)
    
    # f-string dengan formatting ribuan (1.000)
    return f"Total: {total:,}".replace(",", ".")

items = [
    {"harga": 10000, "qty": 2},
    {"harga": "5000", "qty": 3},
    {"harga": "abc", "qty": 1}
]

print(total_harga_pro(items)) # Output: Total: 35.000