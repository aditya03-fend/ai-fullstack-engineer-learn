from collections import defaultdict

transaksi = [
    {"user": "Ani", "total": 10000},
    {"user": "Budi", "total": "20000"},
    {"user": "Ani", "total": 5000},
    {"user": "Caca", "total": "invalid"}
]

def akumulasi_transaksi(data):
    hasil = {}
    
    for item in data:
        try:
            nama = item["user"]
            nilai = int(item["total"])
            
            if nama in hasil:
                hasil[nama] += nilai
            else:
                hasil[nama] = nilai
                
        except (ValueError, KeyError, TypeError):
            continue
            
    return hasil

print(akumulasi_transaksi(transaksi))