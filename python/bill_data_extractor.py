import sys
import os
sys.path.append('C:/xampp/htdocs/intp/python')
import pandas as pd
from sqlalchemy import create_engine
import config as cfg
import datetime
import sqlalchemy
import pymysql as sql
# require MySQLdb module too
engine = create_engine("mysql://root:@localhost/medihelp?charset=utf8")
conn = engine.connect()

con =  sql.connect(host = cfg.mysql_medihelp['server'],user= cfg.mysql_medihelp['username'],
                    password = cfg.mysql_medihelp['password'],db= cfg.mysql_medihelp['database']
                    ,cursorclass=sql.cursors.DictCursor)
cursor=con.cursor()

df = pd.read_csv("C:/xampp/htdocs/intp/python/U031998124_111687.csv",keep_default_na=False)
df['Available'] = df['Qty']+df['Free'] 


df_invoices = df[['Vendor','CUCode','Customer','InvNo','InvDate','CreditDays','InvAmt']]  
df_invoices['total_medicine'] = df['Available'].sum()
df_invoices=df_invoices.iloc[:1,:]
df_invoices.to_sql('invoices',conn,if_exists="append",index=False)


invno=df_invoices['InvNo'][0]
id_query =f"SELECT id from invoices where InvNo = '{invno}'"
id_invoice=cursor.execute(id_query)

df_stocks=df[['Manufacturer','ProductDesc','PrCode','PPack','BatchNo','ExpDate','Qty'
            ,'Free','Rate','GrsAmt','MRP','Barcode','HSNCode','IGSTPer','CGSTPer','SGSTPer'
            ,'Available']]
df_stocks['InvId'] = id_invoice
df_stocks['Date_added']=datetime.datetime.now()
df_stocks.to_sql('stocks', conn , if_exists ="append", index=False)


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

