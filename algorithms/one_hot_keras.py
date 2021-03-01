from keras.preprocessing.text import Tokenizer


samples = ["The cat sat on the mat.", "The dog ate my homework."]

# This argument means, tokenizer will take only 1000 the most common words
tokenizer = Tokenizer(num_words=1000)

# building index of words
tokenizer.fit_on_texts(samples)

sequences = tokenizer.texts_to_sequences(samples)

one_hot_results = tokenizer.texts_to_matrix(samples, mode='binary')

word_index = tokenizer.word_index
print("Found %s unique tokens" % len(word_index))
print(one_hot_results)