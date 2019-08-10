import sys
import os
sys.path.append('C:/xampp/htdocs/intp/python')
import pandas as pd
from sqlalchemy import create_engine
import config as cfg
import datetime
import sqlalchemy
# require MySQLdb module too
engine = create_engine("mysql://root:@localhost/medihelp?charset=utf8")
conn = engine.connect()


df = pd.read_csv("C:/xampp/htdocs/intp/python/U031998124_111687.csv",keep_default_na=False)
df['Available'] = df['Qty'] 
df['Date_added']=datetime.datetime.now()
df.to_sql('stocks', conn , if_exists ="append", index=False)


#run the below code once after creating its equivalent table medicine_info from 
#database_configuration and comment this code

"""
df_excel =pd.read_excel("C:/xampp/htdocs/intp/python/Sample_New_Medicine_Data.xlsx",keep_default_na=False)

df_excel.rename(columns = {0:'medicine_name','Use' : 'uses'},inplace =True)

df_excel.columns=df_excel.columns.str.replace(' ', '_')
df_excel.drop(['Price','How_It_Works','FAQ','Expert_Advice','Image_Name'],axis=1 ,inplace=True)
df_excel.to_sql('medicine_info',conn,if_exists = "append",index=False)
"""

#after running this df_excel medine_info table will be created
#go to phpmyadmin and go to structure of medicine_info of medihelp database
#drop these fields 
#price
#how it Works
#FAQ
#Expert advice
#Image Name
# now you  are done here

