import numpy as np

vector data user
user = np.array([25, 5, 3])
[umur, jam_belajar, pengalaman_tahun]

print("User vector:", user)
print("Dimensi:", user.shape)

perkalian skalar
scaled_user = 0.1 * user
print("Scaled user:", scaled_user)

penjumlahan vector
bonus = np.array([0, 2, 1])

new_user = user + bonus
print("Updated user:", new_user)

bobot model
weights = np.array([0.2, 0.5, 1.5])

dot product
score = user @ weights
print("Skor kelayakan:", score)

matrix dataset (5 user, 3 fitur)
X = np.array([
    [25, 5, 3],
    [30, 2, 5],
    [22, 6, 1],
    [40, 1, 10],
    [28, 4, 4],
])

print("Dataset shape:", X.shape)

bobot sama seperti sebelumnya
W = np.array([0.2, 0.5, 1.5])

prediksi semua user
scores = X @ W

print("Skor semua user:")
print(scores)
bobot layer (3 fitur → 2 neuron)
W_layer = np.array([[0.2, 0.4], [0.5, 0.1], [1.5, 0.3]])

forward pass
output = X @ W_layer

print("Output layer:")
print(output)
print("Shape:", output.shape)

ambil 1 data
x = X[0]

manual = x @ W_layer
auto = output[0]

print("Manual:", manual)
print("Auto:", auto)


def predict(user_vector, weight_matrix):
    return user_vector @ weight_matrix


new_user = np.array([27, 3, 2])
prediction = predict(new_user, W_layer)

print("Prediksi user baru:", prediction)
