transaksi = [
    {"user": "Ani", "total": 10000},
    {"user": "Budi", "total": "20000"},
    {"user": "Ani", "total": 5000}
]

def analisis(transaksi):
    data = []

    for users in transaksi:
            nama = users["user"]
            total = int(users["total"])

            if nama == nama:
                  data.append(f"{nama}: {total}")

    return data

print(analisis(transaksi))