
from tensorflow import keras
from tensorflow.keras import layers,callbacks
from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten
from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np

#We prepare data here so we can use it on model
gestures = {'like':like1,'peace':peace1,'point':point1}
X = []
Y = []
Cnames = []
for index,(name,ds) in enumerate(gestures.items()):
  X.extend(normz(ds))
  Y.extend([index]*len(ds))
  Cnames.append(name)

X = np.array(X)
Y = np.array(Y)
Xte,Xtr,Yte,Ytr = train_test_split(X,Y,test_size=0.2,random_state=42)

earlyst = callbacks.EarlyStopping( 
    monitor='loss',
    min_delta=0.001, 
    patience=10, 
    restore_best_weights=True,
)

model = keras.Sequential([
    layers.Input(shape=(63,)),
    layers.Dense(128,activation='relu'),
    layers.Dropout(0.2),
    layers.Dense(128,activation='relu'),
    layers.Dropout(0.2),
    layers.Dense(64,activation='relu'),
    layers.Dropout(0.2),
    layers.Dense(3,activation='softmax')
])

model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy']) 
model.fit(
    Xtr,
    Ytr,
    callbacks=[earlyst],
    verbose=0,
    epochs=60)
model.evaluate(Xte,Yte)
model.save('Medmodel.keras')
