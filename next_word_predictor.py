# Next Word Prediction using LSTM (Minimal)

import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding, LSTM, Dense
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences

# 1. Sample text
text = "i love deep learning and i love nlp"

# 2. Tokenization
tokenizer = Tokenizer()
tokenizer.fit_on_texts([text])
seq = tokenizer.texts_to_sequences([text])[0]
vocab_size = len(tokenizer.word_index) + 1

# 3. Create input-output sequences
X, y = [], []
for i in range(1, len(seq)):
    X.append(seq[:i])
    y.append(seq[i])

X = pad_sequences(X)
y = tf.keras.utils.to_categorical(y, vocab_size)

# 4. Model
model = Sequential([
    Embedding(vocab_size, 10),
    LSTM(64),
    Dense(vocab_size, activation="softmax")
])

model.compile(loss="categorical_crossentropy", optimizer="adam")
model.fit(X, y, epochs=300, verbose=0)

# 5. Predict next word
def predict_next(text, n=1):
    for _ in range(n):
        s = tokenizer.texts_to_sequences([text])[0]
        s = pad_sequences([s], maxlen=X.shape[1])
        word_id = model.predict(s, verbose=0).argmax()
        text += " " + tokenizer.index_word[word_id]
    return text

print(predict_next("i love"))
