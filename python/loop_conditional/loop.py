# Loop List ======================================================================================
umur = 20
is_admin = False

if umur >= 18 and not is_admin:
    print("User dewasa biasa")

# Loop Dict ======================================================================================
user = {
    "nama": "Ndok",
    "umur": 20
}

for key, value in user.items():
    print(key, ":", value)

# Loop List of Dict ======================================================================================
users = [
    {"nama": "Ani", "umur": 20},
    {"nama": "Budi", "umur": 25}
]

for user in users:
    print(user["nama"], "-", user["umur"])

# Loop While ======================================================================================
counter = 1

while counter <= 5:
    print(counter)
    counter += 1

# Break ======================================================================================
for i in range(1, 6):
    if i == 3:
        break
    print(i)

# Continue ======================================================================================
for i in range(1, 6): 
    if i == 3:
        continue
    print(i)
