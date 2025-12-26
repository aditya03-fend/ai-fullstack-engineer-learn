import json
import logging
import pandas as pd
from pathlib import Path


def load_config(config_path="config.json"):
    with open(config_path, "r") as f:
        return json.load(f)


config = load_config()

logging.basicConfig(
    filename=config["log_file"],
    level=logging.ERROR,
    format="%(asctime)s - %(levelname)s - %(message)s",
)


def load_data(file_path):
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
    required_columns = {"nama", "nilai"}
    if not required_columns.issubset(df.columns):
        missing = required_columns - set(df.columns)
        logging.error(f"Kolom hilang: {missing}")
        return False
    return True


def transform_data(df, passing_grade):
    df["status"] = df["nilai"].apply(
        lambda x: "lulus" if x >= passing_grade else "tidak lulus"
    )
    return df[["nama", "status"]]


def save_data(df, output_path):
    df.to_json(output_path, orient="records", indent=4)
    

def run_pipeline():
    try:
        raw_data = load_data(config["input_path"])

        if not validate_data(raw_data):
            print("Gagal: Data tidak valid. Cek log.")
            return

        processed_data = transform_data(raw_data, config["passing_grade"])

        save_data(processed_data, config["output_path"])

    except Exception as e:
        logging.critical(f"Pipeline berhenti karena error: {str(e)}")
        print(f"Terjadi kesalahan fatal. Detail tersimpan di {config['log_file']}")


if __name__ == "__main__":
    run_pipeline()
