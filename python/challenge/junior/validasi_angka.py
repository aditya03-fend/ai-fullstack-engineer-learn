def cek_angka(angka):
    try:
        angka = float(angka)

        if angka > 0:
            return "Positif"
        elif angka < 0:
            return "Negatif"
        else:
            return "Nol"
    except:
        return "Input Tidak Valid!"
    
print(cek_angka("a"))