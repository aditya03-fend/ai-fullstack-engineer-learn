import pandas as pd
from pathlib import Path


def load_data(file_path):
    """
    Memuat data dari file CSV atau JSON menggunakan pathlib.
    """
    # Mengubah string menjadi objek Path
    path = Path(file_path)

    # Mengecek apakah file benar-benar ada
    if not path.exists():
        return f"Error: File '{path}' tidak ditemukan."

    # Mengambil ekstensi file (sudah termasuk titik, misal: '.csv')
    extension = path.suffix.lower()

    try:
        if extension == ".csv":
            return pd.read_csv(path)
        elif extension == ".json":
            return pd.read_json(path)
        else:
            raise ValueError(f"Ekstensi {extension} tidak didukung.")

    except Exception as e:
        return f"Terjadi kesalahan saat membaca file: {e}"


df = print(load_data("anjeng"))
