import pandas as pd
import os, sys


ds = pd.read_csv('case13.csv')

print(ds.head())
print(ds.info())

time = ds['time']
tidal_no2 = ds['End tidal nitrous oxide concentration (etN20) values']
tidal_o2 = ds['End tidal oxygen concentration (etO2) values']
binary_res_no = [0]
binary_res_o = [0]

for i in range(len(tidal_no2) - 1):
    if tidal_no2[i + 1] > tidal_no2[i]:
        binary_res_no.append(1)
    else:
        binary_res_no.append(0)
    if tidal_o2[i + 1] > tidal_o2[i]:
        binary_res_o.append(1)
    else:
        binary_res_o.append(0)

data = {
    'time':  ds['time'],
    'tidal_no2': ds['End tidal nitrous oxide concentration (etN20) values'],
    'tidal_o2': ds['End tidal oxygen concentration (etO2) values'],
    'heart_rate': ds['Heart rate (HR) value'],
    'binary_res_no': binary_res_no,
    'binary_res_o': binary_res_o,
}

test_data = pd.DataFrame(data)
print(test_data)

sys.path.append('./')
test_data.to_csv('cases/test13_data.csv', index=False)