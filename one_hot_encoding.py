import numpy as np


samples = ["The cat sat on the mat", "The dog ate my homework"]

# build index of whole tokens data
token_index = {}
for sample in samples:
    # tokenization samples by split method(in big document remember about punctuation marks)
    for word in sample.split():
        # assigning unique index to every word, start by 1 not by 0
        if word not in token_index:
            token_index[word] = len(token_index) + 1

max_length = 10

results = np.zeros((len(samples), max_length, max(token_index.values()) + 1))

for i, sample in enumerate(samples):
    for j, word in list(enumerate(sample.split()))[:max_length]:
        index = token_index.get(word)
        results[i, j, index] = 1

print(results)