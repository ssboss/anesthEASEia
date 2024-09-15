import tensorflow as tf
import pandas as pd

# Note: all of these dosages are for general anesthesia

train8_csv_path = 'train8_data.csv'
train8_ds = pd.read_csv(train8_csv_path)
test8_csv_path = 'test8_data.csv'
test8_ds = pd.read_csv(test8_csv_path)

x_train1 = train8_ds['time']
x_train2 = train8_ds['inspired_no2']
x_train3 = train8_ds['heart_rate']
y_train = train8_ds['binary_res_no']

x_test1 = test8_ds['time']
x_test2 = test8_ds['tidal_o2']
x_test3 = test8_ds['heart_rate']
y_test = test8_ds['binary_res_no']

train9_csv_path = 'train9_data.csv'
train9_ds = pd.read_csv(train9_csv_path)
test9_csv_path = 'test9_data.csv'
test9_ds = pd.read_csv(test9_csv_path)

x_train11 = train9_ds['time']
x_train22 = train9_ds['inspired_no2']
x_train33 = train9_ds['heart_rate']
y_train1 = train9_ds['binary_res_no']

x_test11 = test9_ds['time']
x_test22 = test9_ds['tidal_o2']
x_test33 = test9_ds['heart_rate']
y_test11 = test9_ds['binary_res_no']

train10_csv_path = 'train10_data.csv'
train10_ds = pd.read_csv(train10_csv_path)
test10_csv_path = 'test10_data.csv'
test10_ds = pd.read_csv(test10_csv_path)

x_train111 = train10_ds['time']
x_train222 = train10_ds['inspired_no2']
x_train333 = train10_ds['heart_rate']
y_train11 = train10_ds['binary_res_no']

x_test111 = test10_ds['time']
x_test222 = test10_ds['tidal_no2']
x_test333 = test10_ds['heart_rate']
y_test111 = test10_ds['binary_res_no']

train11_csv_path = 'train11_data.csv'
train11_ds = pd.read_csv(train11_csv_path)
test11_csv_path = 'test11_data.csv'
test11_ds = pd.read_csv(test11_csv_path)

x_train1111 = train11_ds['time']
x_train2222 = train11_ds['inspired_no2']
x_train3333 = train11_ds['heart_rate']
y_train111 = train11_ds['binary_res_no']

x_test1111 = test11_ds['time']
x_test2222 = test11_ds['tidal_no2']
x_test3333 = test11_ds['heart_rate']
y_test1111 = test11_ds['binary_res_no']

train12_csv_path = 'train12_data.csv'
train12_ds = pd.read_csv(train12_csv_path)
test12_csv_path = 'test12_data.csv'
test12_ds = pd.read_csv(test12_csv_path)

x_train11111 = train12_ds['time']
x_train22222 = train12_ds['inspired_no2']
x_train33333 = train12_ds['heart_rate']
y_train1111 = train12_ds['binary_res_no']

x_test11111 = test12_ds['time']
x_test22222 = test12_ds['tidal_no2']
x_test33333 = test12_ds['heart_rate']
y_test11111 = test12_ds['binary_res_no']

train13_csv_path = 'train13_data.csv'
train13_ds = pd.read_csv(train13_csv_path)
test13_csv_path = 'test13_data.csv'
test13_ds = pd.read_csv(test13_csv_path)

x_train11111 = train11_ds['time']
x_train22222 = train11_ds['inspired_no2']
x_train33333 = train11_ds['heart_rate']
y_train1111 = train11_ds['binary_res_no']

x_test11111 = test10_ds['time']
x_test22222 = test10_ds['tidal_no2']
x_test33333 = test10_ds['heart_rate']
y_test11111 = test10_ds['binary_res_no']



# x_train1 = tf.keras.utils.normalize(x_train1, axis=1)
# x_train2 = tf.keras.utils.normalize(x_train2, axis=1)

model = tf.keras.models.Sequential([
    tf.keras.layers.Dense(256, input_dim=1, activation='relu'),
    tf.keras.layers.Dense(128, activation='relu'),
    tf.keras.layers.Dense(64, activation='relu'),
    tf.keras.layers.Dense(32, activation='relu'),
    tf.keras.layers.Dense(16, activation='relu'),
    tf.keras.layers.Dense(8, activation='relu'),
    tf.keras.layers.Dense(4, activation='relu'),
    tf.keras.layers.Dense(2, activation='softmax'),
    tf.keras.layers.Dropout(0.2)
])
loss_fn = tf.keras.losses.SparseCategoricalCrossentropy(from_logits=False)

model.compile(optimizer='adam', loss=loss_fn, metrics=['accuracy'])

model.fit([x_train1, x_train2, x_train3], y_train, epochs=5, batch_size=322)
model.fit([x_train11, x_train22, x_train33], y_train1, epochs=5, batch_size=322)
model.fit([x_train111, x_train222, x_train333], y_train11, epochs=5, batch_size=322)
model.fit([x_train1111, x_train2222, x_train3333], y_train111, epochs=5, batch_size=322)
model.fit([x_train11111, x_train22222, x_train33333], y_train1111, epochs=5, batch_size=322)

model.evaluate([x_test1, x_test2, x_test3], y_test)
model.evaluate([x_test11, x_test22, x_test33], y_test11)

