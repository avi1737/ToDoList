{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{'server': 'localhost', 'username': 'root', 'password': '', 'database': 'medihelp', 'billing_table': 'billing', 'sell_out_table': 'sell_out', 'orders_table': 'orders', 'stocks_table': 'stocks', 'profit_table': 'profits'}\n"
     ]
    }
   ],
   "source": [
    "import pymysql as sql\n",
    "import config as cfg\n",
    "print(cfg.mysql_medihelp)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "CREATE TABLE IF NOT EXIST billing (id PRIMARY KEY AUTO INCREMENT,medicine_name varchar(50))\n",
      "CREATE TABLE IF NOT EXIST sell_out (id PRIMARY KEY AUTO INCREMENT,medicine_name varchar(50))\n",
      "CREATE TABLE IF NOT EXIST stocks (id PRIMARY KEY AUTO INCREMENT,medicine_name varchar(50))\n",
      "CREATE TABLE IF NOT EXIST orders (id PRIMARY KEY AUTO INCREMENT,medicine_name varchar(50))\n",
      "CREATE TABLE IF NOT EXIST profits (id PRIMARY KEY AUTO INCREMENT,medicine_name varchar(50))\n"
     ]
    }
   ],
   "source": [
    "#conn =  sql.connect(host = cfg.mysql_medihelp['server'],username= cfg.mysql_medihelp['username'] , password = cfg.mysql_medihelp['password'],cursorclass=sql.cursors.DictCursor)\n",
    "#cursor=conn.cursor()\n",
    "#cursor.execute('create database IF NOT EXISTS medihelp')\n",
    "\n",
    "\n",
    "billing_query = f\"CREATE TABLE IF NOT EXIST {cfg.mysql_medihelp['billing_table']} (id PRIMARY KEY AUTO INCREMENT,medicine_name varchar(50))\"\n",
    "print(billing_query)                \n",
    "#cursor.execute(billing_query)\n",
    "\n",
    "sell_out_query = f\"CREATE TABLE IF NOT EXIST {cfg.mysql_medihelp['sell_out_table']} (id PRIMARY KEY AUTO INCREMENT,medicine_name varchar(50))\"\n",
    "print(sell_out_query)                 \n",
    "#cursor.execute(sell_out_query)\n",
    "\n",
    "stocks_query = f\"CREATE TABLE IF NOT EXIST {cfg.mysql_medihelp['stocks_table']} (id PRIMARY KEY AUTO INCREMENT,medicine_name varchar(50))\"\n",
    "print(stocks_query)                 \n",
    "#cursor.execute(stocks_query)\n",
    "\n",
    "orders_query = f\"CREATE TABLE IF NOT EXIST {cfg.mysql_medihelp['orders_table']} (id PRIMARY KEY AUTO INCREMENT,medicine_name varchar(50))\"\n",
    "print(orders_query)                 \n",
    "#cursor.execute(orders_query)\n",
    "\n",
    "profit_query = f\"CREATE TABLE IF NOT EXIST {cfg.mysql_medihelp['profit_table']} (id PRIMARY KEY AUTO INCREMENT,medicine_name varchar(50))\"\n",
    "print(profit_query)                 \n",
    "#cursor.execute(profit_query)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.6.8"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
