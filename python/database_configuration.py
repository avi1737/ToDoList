import pymysql as sql
import config as cfg
print(cfg.mysql_medihelp)

conn =  sql.connect(host = cfg.mysql_medihelp['server'],username= cfg.mysql_medihelp['username'] , password = cfg.mysql_medihelp['password'],cursorclass=sql.cursors.DictCursor)
cursor=conn.cursor()
cursor.execute('create database IF NOT EXISTS medihelp')

cursor.close()
conn.close()
