import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense
#from tensorflow.keras.models import Sequential
# from tensorflow.keras.layers import LSTM, Dense
import matplotlib.pyplot as plt

df = pd.read_csv('df.csv')
df = df[["close_time","close_price"]]

df['close_time'] = pd.to_datetime(df['close_time'])

df.set_index('close_time', inplace=True)

df.index = pd.to_datetime(df.index)

scaler = MinMaxScaler()
df_scaled = scaler.fit_transform(df)

train_size = int(len(df_scaled) * 0.8)
train, test = df_scaled[0:train_size, :], df_scaled[train_size:len(df_scaled), :]

def create_dataset(dataset, time_steps=1):
    dataX, dataY = [], []
    for i in range(len(dataset)-time_steps-1):
        a = dataset[i:(i+time_steps), 0]
        dataX.append(a)
        dataY.append(dataset[i + time_steps, 0])
    return np.array(dataX), np.array(dataY)

time_steps = 5
X_train, y_train = create_dataset(train, time_steps)
X_test, y_test = create_dataset(test, time_steps)

X_train = np.reshape(X_train, (X_train.shape[0], 1, X_train.shape[1]))
X_test = np.reshape(X_test, (X_test.shape[0], 1, X_test.shape[1]))

model = Sequential()
model.add(LSTM(50, input_shape=(1, time_steps)))
model.add(Dense(1))
model.compile(optimizer='adam', loss='mean_squared_error')

model.fit(X_train, y_train, epochs=50, batch_size=32, verbose=2)

train_predict = model.predict(X_train)
test_predict = model.predict(X_test)

train_predict = scaler.inverse_transform(train_predict)
y_train = scaler.inverse_transform([y_train])
test_predict = scaler.inverse_transform(test_predict)
y_test = scaler.inverse_transform([y_test])

train_predict_plot = np.empty_like(df_scaled)
train_predict_plot[:, :] = np.nan
train_predict_plot[time_steps:len(train_predict)+time_steps, :] = train_predict

test_predict_plot = np.empty_like(df_scaled)
test_predict_plot[:, :] = np.nan
test_predict_plot[len(train_predict)+(time_steps*2)+1:len(df_scaled)-1, :] = test_predict

plt.figure(figsize=(20, 10))
plt.plot(scaler.inverse_transform(df_scaled), label='Observed')
plt.plot(train_predict_plot, label='Training')
plt.plot(test_predict_plot, label='Test')
plt.xlabel('Time')
plt.ylabel('close_price')
plt.title('Predicion bitcoin with LSTM')
plt.legend()
plt.savefig('ml_result.jpg', format='jpeg')
plt.show()