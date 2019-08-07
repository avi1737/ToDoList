import sys
import os
sys.path.append('C:/xampp/htdocs/intp/python')
import pandas as pd
from sqlalchemy import create_engine
import config as cfg
import datetime
# require MySQLdb module too
engine = create_engine("mysql://root:@localhost/medihelp")
conn = engine.connect()
 

df = pd.read_csv("C:/xampp/htdocs/intp/python/U031998124_111687.csv",keep_default_na=False)
df['Available'] = df['Qty'] 
df['Date_added']=datetime.datetime.now()
df.to_sql('stocks', conn , if_exists ="append", index=False)
