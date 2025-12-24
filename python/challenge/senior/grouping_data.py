def grup_data(data):
    admin = []
    user = []

    for res in data:
        try:
            role = res["role"]

            if role == "admin":
                admin.append(res["nama"])
            else:
                user.append(res["nama"])
        except:
            continue

    result = {
        "admin": admin,
        "user": user
    }

    return result


users = [
    {"nama": "Ani", "role": "admin"},
    {"nama": "Budi", "role": "user"},
    {"nama": "Caca", "role": "admin"}
]


print(grup_data(users)) 
    