def filter_data(data):
    hasil = []

    for item in data:
        try:
            angka = int(item)
            hasil.append(angka)
        except:
            pass
        
    return hasil
            
data = [1, "2", 3, "empat", 5]
print(filter_data(data))