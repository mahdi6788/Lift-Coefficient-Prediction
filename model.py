import numpy as np
import pandas as pd
import tensorflow as tf
from tensorflow import keras
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
# from google.colab import files

# files.upload()

data = pd.read_csv("DatabaseAll.csv")
data = np.array(data)
scaler= StandardScaler()
scaled= scaler.fit_transform(X=data)
database= np.array(scaled)
# input 1
training_airfoil = database[:4200,:200]
testing_airfoil = database[4200:,:200]
# input 2
training_re_alpha = database[:4200,200:202]
testing_re_alpha = database[4200:,200:202]
# output
training_cl = database[:4200,202]
testing_cl = database[4200:,202]

## Network
# CNN
input_cnn = keras.Input(shape=(200,))
cnn = keras.layers.Reshape((2,100,1), input_shape=(200,))(input_cnn)
cnn = keras.layers.Conv2D(20, kernel_size=(2,10), activation=keras.layers.LeakyReLU(alpha=0.1))(cnn)
cnn_flat = keras.layers.Flatten()(cnn)
# FC
input_fc = keras.Input(shape=(2,))
fc_flat = keras.layers.Flatten()(input_fc)
cnn_fc=tf.concat([cnn_flat]+[fc_flat],axis=1)

fc = keras.layers.Dense(200, activation=keras.layers.LeakyReLU(alpha=0.1))(cnn_fc)
fc = keras.layers.Dense(10, activation=keras.layers.LeakyReLU(alpha=0.1))(fc)
output = keras.layers.Dense(1, activation="tanh")(fc)

model= keras.Model(inputs=[input_cnn, input_fc], outputs=[output])
optimizer=keras.optimizers.Adam(learning_rate=0.0005)
# model.load_weights("model_weights.h5")
model.compile(loss="mean_squared_error", optimizer=optimizer)
history = model.fit(x=[training_airfoil, training_re_alpha], y=training_cl, epochs=200)
model.save_weights("model_weights.h5")

pd.DataFrame(history.history).plot()
plt.show()

prediction= model.predict(x=[testing_airfoil,testing_re_alpha])
test_concat=np.concatenate((testing_airfoil, testing_re_alpha, prediction), axis=1)
scaled_back= scaler.inverse_transform(test_concat)
scaled_back_frame=pd.DataFrame(scaled_back)
print(scaled_back_frame)