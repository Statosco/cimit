import ssl
ssl._create_default_https_context = ssl._create_unverified_context

import tensorflow as tf
import numpy as np
from tensorflow import keras
import matplotlib.pyplot as plt

# Load Fashion MNIST dataset
fashion_mnist = keras.datasets.fashion_mnist
(trained_images, train_labels), (test_images, test_labels) = fashion_mnist.load_data()

# Normalize pixel values
trained_images = trained_images / 255.0
test_images = test_images / 255.0

# Build the model
model = keras.Sequential([
    keras.layers.Flatten(input_shape=(28, 28)),
    keras.layers.Dense(units=128, activation=tf.nn.relu),
    keras.layers.Dense(units=10, activation=tf.nn.softmax)
])

# Compile the model
model.compile(optimizer=tf.optimizers.Adam(), loss='sparse_categorical_crossentropy', metrics=['accuracy'])

# Display model summary
model.summary()

# Train the model
model.fit(trained_images, train_labels, epochs=5)

# Evaluate the model on the test set
test_loss = model.evaluate(test_images, test_labels)

# Visualize a prediction
predictions = model.predict(test_images)
img_index = 1
plt.imshow(test_images[img_index], cmap='gray')
plt.title(f"True Label: {test_labels[img_index]}, Predicted Label: {np.argmax(predictions[img_index])}")
plt.show()

print(f"Test Loss: {test_loss}")
