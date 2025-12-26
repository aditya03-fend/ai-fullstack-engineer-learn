import numpy as np

kata = np.array([0.2, 0.5, 0.1])

# cosine similarity
similarity = np.dot(kata, kata) / (np.linalg.norm(kata) ** 2)
print(similarity)
