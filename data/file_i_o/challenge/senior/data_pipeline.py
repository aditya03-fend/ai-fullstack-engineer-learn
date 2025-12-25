import json
import logging
import pandas as pd
from pathlib import Path


# --- CONFIGURATION LAYER ---
def load_config(config_path="config.json"):
    with open(config_path, "r") as f:
        return json.load(f)


config = load_config()

# --- LOGGING SETUP ---
logging.basicConfig(
    filename=config["log_file"],
    level=logging.ERROR,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

# --- CORE FUNCTIONS (MODULAR) ---


def load_data(file_path):
    """Membaca data berdasarkan ekstensi file."""
    path = Path(file_path)
    if not path.exists():
        logging.error(f"File tidak ditemukan: {file_path}")
        raise FileNotFoundError(f"File {file_path} tidak ada.")

    ext = path.suffix.lower()
    if ext == ".csv":
        return pd.read_csv(path)
    elif ext == ".json":
        return pd.read_json(path)
    else:
        raise ValueError(f"Format {ext} tidak didukung.")


def validate_data(df):
    """Memastikan kolom yang dibutuhkan tersedia."""
    required_columns = {"nama", "nilai"}
    if not required_columns.issubset(df.columns):
        missing = required_columns - set(df.columns)
        logging.error(f"Kolom hilang: {missing}")
        return False
    return True


def transform_data(df, passing_grade):
    """Logika bisnis: Menentukan status kelulusan."""
    # Hanya mengambil kolom nama dan membuat kolom status
    df["status"] = df["nilai"].apply(
        lambda x: "lulus" if x >= passing_grade else "tidak lulus"
    )
    return df[["nama", "status"]]


def save_data(df, output_path):
    """Menyimpan hasil akhir ke format JSON."""
    df.to_json(output_path, orient="records", indent=4)
    print(f"Sukses! Hasil disimpan ke {output_path}")


# --- PIPELINE EXECUTION (CLEAN ARCHITECTURE) ---


def run_pipeline():
    try:
        # 1. Load
        raw_data = load_data(config["input_path"])

        # 2. Validate
        if not validate_data(raw_data):
            print("Gagal: Data tidak valid. Cek log.")
            return

        # 3. Transform
        processed_data = transform_data(raw_data, config["passing_grade"])

        # 4. Save
        save_data(processed_data, config["output_path"])

    except Exception as e:
        logging.critical(f"Pipeline berhenti karena error: {str(e)}")
        print(f"Terjadi kesalahan fatal. Detail tersimpan di {config['log_file']}")


if __name__ == "__main__":
    run_pipeline()
