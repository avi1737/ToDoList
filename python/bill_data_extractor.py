import sys
import os
sys.path.append(os.getcwd()+"/intp/python")
import pandas as pd
import config as cfg

df = pd.read_csv(os.getcwd()+"/intp/python/U031998124_111687.csv")
df['Available'] = df['Qty']
df
#df.to_sql('buying_medicine' , conn , if_exists = append)
