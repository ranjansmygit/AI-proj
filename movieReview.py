import tensorflow as tf
from tensorflow.keras.datasets import imdb
from tensorflow.keras.preprocessing.sequence import pad_sequences

# Load the IMDB dataset
vocab_size = 10000
max_length = 200
embedding_dim = 16
trunc_type = 'post'
padding_type = 'post'
oov_token = '<OOV>'
num_epochs = 10

(train_data, train_labels), (test_data, test_labels) = imdb.load_data(num_words=vocab_size)

# Preprocess the data
train_data = pad_sequences(train_data, maxlen=max_length, padding=padding_type, truncating=trunc_type)
test_data = pad_sequences(test_data, maxlen=max_length, padding=padding_type, truncating=trunc_type)

# Build the model
model = tf.keras.Sequential([
    tf.keras.layers.Embedding(vocab_size, embedding_dim, input_length=max_length),
    tf.keras.layers.GlobalAveragePooling1D(),
    tf.keras.layers.Dense(24, activation='relu'),
    tf.keras.layers.Dense(1, activation='sigmoid')
])

model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
model.summary()

# Train the model
history = model.fit(train_data, train_labels, epochs=num_epochs,
                    validation_data=(test_data, test_labels), verbose=2)

# Evaluate the model
loss, accuracy = model.evaluate(test_data, test_labels)
print(f"Test Accuracy: {accuracy * 100:.2f}%")
