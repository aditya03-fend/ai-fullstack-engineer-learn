def sanitasi_data_pro(data: list) -> dict:
    def is_valid(val):
        try:
            return True, int(val)
        except (ValueError, TypeError):
            return False, val
    hasil_proses = [is_valid(x) for x in data]
    return {
        'valid': [val for status, val in hasil_proses if status],
        'invalid': [val for status, val in hasil_proses if not status]
    }

data = ["10", None, "20", "abc", 30]
print(sanitasi_data_pro(data))