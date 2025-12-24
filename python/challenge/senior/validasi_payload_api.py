def validasi(data):
    if "nama" not in data or not data["nama"]:
        return {"error": "nama wajib di is"}
    
    if "umur" not in data or not data["umur"]:
        return {"error": "umur wajib di is"}
    
    if not str(data["umur"]).isdigit():
        return {"error": "umur harus berupa angka"}
    
    umur = int(data["umur"])

    if umur < 18:
        return {"error": "umur harus lebih dari 18 tahun"} 
    
    return {"status": "ok"}

payload = {
    "nama": "Ndok",
    "umur": "17",
    "email": "ndok@mail.com"
}

print(validasi(payload))