import os
import sys
sys.path.append('C:/xampp/htdocs/intp/python')
import pymysql as sql
import config as cfg
import warnings
warnings.filterwarnings("ignore")
conn =  sql.connect(host = cfg.mysql_medihelp['server'],user= cfg.mysql_medihelp['username'],
                    password = cfg.mysql_medihelp['password'],
                    cursorclass=sql.cursors.DictCursor)
cursor=conn.cursor()
cursor.execute('create database IF NOT EXISTS medihelp')
register_user = """
                CREATE TABLE IF NOT EXISTS `medihelp`.`registered_users`(`ID` INT NOT NULL AUTO_INCREMENT, 
                `name` TEXT NOT NULL , `mobile_number` INT(20) NOT NULL , 
                `shop_name` VARCHAR(30) NOT NULL , `shop_address` VARCHAR(100) NOT NULL ,
                `Email` VARCHAR(30) NOT NULL , `password` VARCHAR(100) NOT NULL ,
                `register_date` DATE NOT NULL DEFAULT CURRENT_TIMESTAMP ,
                PRIMARY KEY (`ID`)) ENGINE = InnoDB
                """

cursor.execute(register_user)


stocks_query = """
                CREATE TABLE `medihelp`.`stocks` ( `ID` INT NOT NULL AUTO_INCREMENT
                ,`CNick` VARCHAR(50) NOT NULL , `Vendor` VARCHAR(100) NOT NULL
                , `CUCode` INT(25) NOT NULL , `Customer` VARCHAR(50) NOT NULL
                , `Area` TEXT NULL , `City` TEXT NULL , `PinCode` INT(10) NULL
                , `InvNo` VARCHAR(40) NOT NULL , `InvDate` DATE NOT NULL 
                , `OrderNo` INT(50) NULL , `OrderDate` DATE NULL 
                , `Transport` VARCHAR(50) NULL , `Freight` VARCHAR(20) NULL 
                , `Paid` VARCHAR(20) NOT NULL ,`LRNo` VARCHAR(30) NULL
                ,`LRDate` DATE NULL , `CreditDays` INT(20) NULL ,`Ad` INT(10) NULL
                ,`Ls` INT(10) NULL , `Tx` INT(10) NOT NULL ,`InvAmt` INT(30) NOT NULL 
                ,`CNote` INT(10) NULL , `MfgrNick` VARCHAR(50) NOT NULL 
                ,`Manufacturer` VARCHAR(100) NOT NULL , `PrCode` INT(30) NOT NULL 
                ,`ProductDesc` VARCHAR(100) NOT NULL , `PPack` VARCHAR(10) NOT NULL 
                ,`MyType` VARCHAR(10) NOT NULL , `MyMode` VARCHAR(10) NULL 
                ,`BatchNo` VARCHAR(30) NOT NULL , `ExpDate` DATE NOT NULL 
                ,`Qty` INT(10) NOT NULL , `Free` INT(5) NULL , `SchQtyAdjlnAmt` INT(5) NULL
                ,`Rate` FLOAT(20) NOT NULL,`MRP` FLOAT(20) NOT NULL  
                ,`WPPer` INT(10) NULL ,`OctroiPer` INT(10) NULL , `SchRate` INT(10) NULL 
                ,`SchPer` INT(10) NULL , `CDPer` INT(10) NULL , `TDPer` INT(10) NULL
                ,`CSTPer` INT(10) NULL , `VATPer` INT(10) NULL ,`INetAmt` FLOAT(20) NOT NULL
                , `Remark` VARCHAR(100) NULL , `LOCA` VARCHAR(20) NOT NULL 
                ,`LOCN` VARCHAR(20) NOT NULL ,`KeepWatch` VARCHAR(30) NOT NULL  
                ,`DivNick` VARCHAR(30) NOT NULL , `MyTypeId` INT(10) NOT NULL 
                ,`MyItemNo` INT(10) NOT NULL,`PTS` FLOAT(30) NOT NULL 
                ,`Barcode` INT(30) NOT NULL , `VGSTIN` VARCHAR(50) NULL 
                ,`CGSTIN` VARCHAR(50) NULL , `HSNCode` VARCHAR(20) NOT NULL 
                ,`IGSTPer` INT(10) NULL,`IGSTAmt` INT(11) NULL ,`CGSTPer` INT(10) NULL
                ,`CGSTAmt` FLOAT(20) NULL, `SGSTPer` INT(10) NULL, `SGSTAmt` FLOAT(20) NULL
                ,`GCCESSPer` VARCHAR(10) NULL, `GCCESSAmt` FLOAT(20) NULL
                ,`UR` VARCHAR(20) NULL, `EWBN` VARCHAR(20) NULL 
                ,`MCode` INT(25) NOT NULL, `Available` INT(20) NOT NULL
                ,Date_Added` DATE NOT NULL DEFAULT CURRENT_TIMESTAMP
                ,PRIMARY KEY (`ID`)) ENGINE = InnoDB
                """
print(stocks_query)



 





cursor.close()
conn.close()
