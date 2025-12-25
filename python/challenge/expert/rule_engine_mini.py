def rule_data(rule: dict, user: dict) -> dict:
    """Memvalidasi akses user berdasarkan aturan umur dan percobaan."""
    try:
        # Konversi dan ambil data dalam satu langkah aman
        is_eligible = (
            int(user["umur"]) >= rule["min_age"] and 
            int(user["attempt"]) <= rule["max_attempt"]
        )
        return {"access": is_eligible}
        
    except (ValueError, KeyError, TypeError):
        # Jika data hilang atau format salah, akses otomatis ditolak
        return {"access": not is_eligible}

# Data contoh
rules = {"min_age": 18, "max_attempt": 3}
user = {"umur": "20", "attempt": 4}

print(rule_data(rules, user)) # Output: {'access': False}