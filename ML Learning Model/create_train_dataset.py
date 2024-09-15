import pandas as pd
import os, sys


ds = pd.read_csv('case13.csv')

print(ds.head())
print(ds.info())

time = ds['time']
inspired_no2 = ds['Inspired nitrous oxide concentration (inN20) values']
inspired_o2 = ds['Inspired oxygen concentration (inO2) values']
binary_res_no = [0]
binary_res_o = [0]

for i in range(len(inspired_no2) - 1):
    if inspired_no2[i + 1] > inspired_no2[i]:
        binary_res_no.append(1)
    else:
        binary_res_no.append(0)
    if inspired_o2[i + 1] > inspired_o2[i]:
        binary_res_o.append(1)
    else:
        binary_res_o.append(0)

data = {
    'time':  ds['time'],
    'inspired_no2': ds['Inspired nitrous oxide concentration (inN20) values'],
    'inspired_o2': ds['Inspired oxygen concentration (inO2) values'],
    'heart_rate': ds['Heart rate (HR) value'],
    'binary_res_no': binary_res_no,
    'binary_res_o': binary_res_o,
}

test_data = pd.DataFrame(data)
print(test_data)

sys.path.append('./')
test_data.to_csv('cases/train13_data.csv', index=False)