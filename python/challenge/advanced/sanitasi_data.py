def sanitasi_data(data):
    valid = []
    invalid = []

    for number in data:
        try:
            valid_number = int(number)
            valid.append(valid_number)
        except:
            invalid.append(number)

    result = {
        'valid': valid,
        'invalid': invalid
    }

    return result

data = ["10", None, "20", "abc", 30]
print(sanitasi_data(data))