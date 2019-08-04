import sys
import os
sys.path.append('C:/xampp/htdocs/intp/python')
import pandas as pd
from sqlalchemy import create_engine
import config as cfg
# require MySQLdb module too
engine = create_engine("mysql://root:@localhost/medihelp")
con = engine.connect()
 

df = pd.read_csv("C:/xampp/htdocs/intp/python/U031998124_111687.csv",keep_default_na=False)
df.head()
df.to_sql('stock', conn , if_exists ="append")
