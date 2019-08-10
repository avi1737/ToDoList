import os
import sys
sys.path.append('C:/xampp/htdocs/intp/python')
import pymysql as sql
import config as cfg
import warnings
warnings.filterwarnings("ignore")
conn =  sql.connect(host = cfg.mysql_medihelp['server'],user= cfg.mysql_medihelp['username'],
                    password = cfg.mysql_medihelp['password'],db= cfg.mysql_medihelp['database']
                    ,cursorclass=sql.cursors.DictCursor)
cursor=conn.cursor()
cursor.execute('create database IF NOT EXISTS medihelp')


product_key ="""
                CREATE TABLE IF NOT EXISTS `medihelp`.`product_key` ( `id` INT NOT NULL AUTO_INCREMENT 
                , `name` TEXT NULL , `email` VARCHAR(100) NULL 
                , `product_key` VARCHAR(100) NOT NULL 
                , PRIMARY KEY (`id`)) 
                """

cursor.execute(product_key)

register_user = """
                CREATE TABLE IF NOT EXISTS `medihelp`.`registered_users`(`ID` INT NOT NULL AUTO_INCREMENT, 
                `name` TEXT NOT NULL , `mobile_number` INT(20) NOT NULL , 
                `shop_name` VARCHAR(30) NOT NULL , `shop_address` VARCHAR(100) NOT NULL ,
                `Email` VARCHAR(30) NOT NULL , `password` VARCHAR(100) NOT NULL ,
                `register_date` DATE NOT NULL DEFAULT CURRENT_TIMESTAMP ,
                PRIMARY KEY (`ID`))
                """

cursor.execute(register_user)

invoice_query = """
                CREATE TABLE `invoices` (
                 `id` int(11) NOT NULL AUTO_INCREMENT,
                 `Vendor` text DEFAULT NULL,
                 `CUCode` bigint(20) DEFAULT NULL,
                 `Customer` text DEFAULT NULL,
                 `InvNo` text DEFAULT NULL,
                 `InvDate` text DEFAULT NULL,
                 `InvAmt` int(60) NOT NULL,
                 `CreditDays` bigint(20) DEFAULT NULL,
                 `total_medicine` bigint(20) DEFAULT NULL,
                 `paid` varchar(60) NOT NULL,
                 `Date_added` date NOT NULL DEFAULT current_timestamp(),
                 PRIMARY KEY (`id`)
                ) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1                              
                """
                                
cursor.execute(invoice_query)                                

medicine_info = """
                CREATE TABLE `medicine_info` (
                 `id` int(11) NOT NULL AUTO_INCREMENT,
                 `medicine_name` text DEFAULT NULL,
                 `Company_Name` text DEFAULT NULL,
                 `Packaging_of_Product` text DEFAULT NULL,
                 `Compositions` text DEFAULT NULL,
                 `Type_Of_Medicine` text DEFAULT NULL,
                 `Alchohol_Interaction` text DEFAULT NULL,
                 `Pregnancy_Interaction` text DEFAULT NULL,
                 `Lactation_Interaction` text DEFAULT NULL,
                 `uses` text DEFAULT NULL,
                 `How_to_Use` text DEFAULT NULL,
                 `Dosage` text DEFAULT NULL,
                 `Common_Side_Effect` text DEFAULT NULL,
                 PRIMARY KEY (`id`)
                ) ENGINE=InnoDB AUTO_INCREMENT=26 DEFAULT CHARSET=latin1           
                """  

cursor.execute(medicine_info)

stocks_query = """
                CREATE TABLE `stocks` (
                 `id` int(11) NOT NULL AUTO_INCREMENT,
                 `InvId` int(62) NOT NULL,
                 `Manufacturer` text DEFAULT NULL,
                 `PrCode` bigint(20) DEFAULT NULL,
                 `ProductDesc` text DEFAULT NULL,
                 `PPack` text DEFAULT NULL,
                 `BatchNo` text DEFAULT NULL,
                 `ExpDate` text DEFAULT NULL,
                 `Qty` bigint(20) DEFAULT NULL,
                 `Free` bigint(20) DEFAULT NULL,
                 `Rate` double DEFAULT NULL,
                 `GrsAmt` double DEFAULT NULL,
                 `MRP` double DEFAULT NULL,
                 `Barcode` bigint(20) DEFAULT NULL,
                 `HSNCode` bigint(20) DEFAULT NULL,
                 `IGSTPer` double DEFAULT NULL,
                 `CGSTPer` double DEFAULT NULL,
                 `SGSTPer` double DEFAULT NULL,
                 `Available` bigint(20) DEFAULT NULL,
                 `Date_Added` date NOT NULL,
                 PRIMARY KEY (`id`)
                ) ENGINE=InnoDB AUTO_INCREMENT=19 DEFAULT CHARSET=latin1
                """

cursor.execute(stocks_query)    

cursor.close()
conn.close()
