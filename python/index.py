from rich import print

products = [
    {"id": 1, "nama": "Laptop", "stok": 5, "harga": 15000000},
    {"id": 2, "nama": "Mouse", "stok": 10, "harga": 150000},
    {"id": 3, "nama": "Keyboard", "stok": 0, "harga": 300000},
]

transactions = [
    {"product_id": 1, "qty": 2},
    {"product_id": 2, "qty": "3"},
    {"product_id": 3, "qty": 1},
    {"product_id": 99, "qty": 1},
    {"product_id": 1, "qty": "invalid"},
]


# Function 1
def find_product(products, product_id):
    for product in products:
        if product["id"] == product_id:
            return product
    return None


# Function 2
def process_transaction(products, transaction):
    try:
        qty = int(transaction.get("qty"))
        if qty <= 0:
            return None

        product = find_product(products, transaction.get("product_id"))
        if not product:
            return None

        if product["stok"] < qty:
            return None

        product["stok"] -= qty
        return qty * product["harga"]

    except (TypeError, ValueError):
        return None


# Function 3
def process_all_transactions(products, transactions):
    total_revenue = 0
    success = 0
    failed = 0

    for trx in transactions:
        result = process_transaction(products, trx)

        if result is None:
            failed += 1
        else:
            total_revenue += result
            success += 1

    return {"total_revenue": total_revenue, "success": success, "failed": failed}


# ===== RUN =====
summary = process_all_transactions(products, transactions)

print("[bold green]Ringkasan Transaksi[/bold green]")
print(summary)

print("\n[bold blue]Stok Akhir[/bold blue]")
for p in products:
    print(f"{p['nama']}: {p['stok']}")
