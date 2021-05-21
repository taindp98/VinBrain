import pandas as pd 
import json
import os
from glob import glob

_DATA_PATH = '../data/mekhoebekhoe.com'
_RESOURCE_PATH = '../resource'

list_file = glob(os.path.join(_DATA_PATH,'*.json'))
# print(len(list_file))
records = []
for f in list_file:
    for line in open(f,'r'):
        try:
            records.append(json.loads(line))
        except Exception as e:
            print('Fail {0},{1}'.format(str(e),f))
# print(len(records))
df = pd.DataFrame(records)
# print(len(df))
df.to_csv(os.path.join(_RESOURCE_PATH,'df_mekhoebekhoe.csv'),index=False,header=True)
# print(df.head())
