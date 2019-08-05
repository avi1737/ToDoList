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
                CREATE TABLE `medihelp`.`invoices` (
                                 `id` int(11) NOT NULL AUTO_INCREMENT,
                                 `Customer_code` int(20) NOT NULL,
                                 `Customer` varchar(30) NOT NULL,
                                 `InvNo` varchar(50) NOT NULL,
                                 `Vendor` varchar(50) NOT NULL,
                                 `InvDate` varchar(50) NOT NULL,
                                 `InvAmt` int(20) NOT NULL,
                                 `total_medicine` int(10) NOT NULL,
                                 `total_medicine_amount` int(10) NOT NULL,
                                 `total_MRP_amount` int(10) NOT NULL,
                                 `Date_added` date NOT NULL DEFAULT current_timestamp(),
                                 PRIMARY KEY (`id`)
                                ) ENGINE=InnoDB DEFAULT CHARSET=latin1
                                """
                                
cursor.execute(invoice_query)                                

stocks_query = """
                CREATE TABLE `medihelp`.`stocks` (
                     `ID` int(11) NOT NULL AUTO_INCREMENT,
                     `CNick` varchar(50) NOT NULL,
                     `Vendor` varchar(100) NOT NULL,
                     `CUCode` int(25) NOT NULL,
                     `Customer` varchar(50) NOT NULL,
                     `Area` text DEFAULT NULL,
                     `City` text DEFAULT NULL,
                     `PinCode` int(10) DEFAULT NULL,
                     `InvNo` varchar(40) NOT NULL,
                     `InvDate` varchar(30) NOT NULL,
                     `OrderNo` int(50) DEFAULT NULL,
                     `OrderDate` varchar(30) DEFAULT NULL,
                     `Transport` varchar(50) DEFAULT NULL,
                     `Freight` varchar(20) DEFAULT NULL,
                     `Paid` varchar(20) NOT NULL,
                     `LRNo` varchar(30) DEFAULT NULL,
                     `LRDate` varchar(30) DEFAULT NULL,
                     `CreditDays` int(20) DEFAULT NULL,
                     `Ad` int(10) DEFAULT NULL,
                     `Ls` int(10) DEFAULT NULL,
                     `Tx` int(10) NOT NULL,
                     `InvAmt` int(30) NOT NULL,
                     `CNote` int(10) DEFAULT NULL,
                     `MfgrNick` varchar(50) NOT NULL,
                     `Manufacturer` varchar(100) NOT NULL,
                     `PrCode` int(30) NOT NULL,
                     `ProductDesc` varchar(100) NOT NULL,
                     `PPack` varchar(10) NOT NULL,
                     `MyType` varchar(10) NOT NULL,
                     `MyMode` varchar(10) DEFAULT NULL,
                     `BatchNo` varchar(30) NOT NULL,
                     `ExpDate` varchar(30) NOT NULL,
                     `Qty` int(10) NOT NULL,
                     `Free` int(5) DEFAULT NULL,
                     `SchQtyAdjInAmt` int(5) DEFAULT NULL,
                     `Rate` float NOT NULL,
                     `GrsAmt` float NOT NULL,
                     `PTR` float NOT NULL,
                     `MRP` float NOT NULL,
                     `WPPer` int(10) DEFAULT NULL,
                     `OctroiPer` int(10) DEFAULT NULL,
                     `SchRate` int(10) DEFAULT NULL,
                     `SchPer` int(10) DEFAULT NULL,
                     `CDPer` int(10) DEFAULT NULL,
                     `TDPer` int(10) DEFAULT NULL,
                     `CSTPer` int(10) DEFAULT NULL,
                     `VATPer` int(10) DEFAULT NULL,
                     `INetAmt` float NOT NULL,
                     `Remark` varchar(100) DEFAULT NULL,
                     `LOCA` varchar(20) NOT NULL,
                     `LOCN` varchar(20) NOT NULL,
                     `KeepWatch` varchar(30) NOT NULL,
                     `DivNick` varchar(30) NOT NULL,
                     `MyTypeId` int(10) NOT NULL,
                     `MyItemNo` int(10) NOT NULL,
                     `PTS` double NOT NULL,
                     `Barcode` int(30) NOT NULL,
                     `VGSTIN` varchar(50) DEFAULT NULL,
                     `CGSTIN` varchar(50) DEFAULT NULL,
                     `HSNCode` varchar(20) NOT NULL,
                     `IGSTPer` int(10) DEFAULT NULL,
                     `IGSTAmt` int(11) DEFAULT NULL,
                     `CGSTPer` int(10) DEFAULT NULL,
                     `CGSTAmt` float DEFAULT NULL,
                     `SGSTPer` int(10) DEFAULT NULL,
                     `SGSTAmt` float DEFAULT NULL,
                     `GCCESSPer` varchar(10) DEFAULT NULL,
                     `GCCESSAmt` float DEFAULT NULL,
                     `UR` varchar(20) DEFAULT NULL,
                     `EWBN` varchar(20) DEFAULT NULL,
                     `MCode` int(25) NOT NULL,
                     `Available` int(20) NOT NULL,
                     `Date_Added` date NOT NULL,
                     PRIMARY KEY (`ID`),
                     UNIQUE KEY `unique` (`BatchNo`)
                    )
                """

cursor.execute(stocks_query)


invoices_trigger_query="""
                        CREATE TRIGGER invoices_insert AFTER INSERT ON `medihelp`.`stocks` FOR EACH ROW
                        BEGIN
                        DECLARE CUSTOMER_CODE INT;
                        DECLARE CUSTOMER VARCHAR(30);
                        DECLARE INVDATE VARCHAR(30);
                        DECLARE INVAMT INT;
                        DECLARE TOTAL_MEDICINE INT;
                        DECLARE TOTAL_MEDICINE_AMT INT;
                        DECLARE TOTAL_MRP_AMT INT; 
                        
                        SET CUSTOMER_CODE = (SELECT DISTINCT(CUCode) FROM `medihelp`.`stocks`);
                        SET CUSTOMER = (SELECT DISTINCT(Customer) FROM `medihelp`.`stocks`);
                        SET INVDATE = (SELECT DISTINCT(InvDate) FROM `medihelp`.`stocks`);
                        SET INVAMT = (SELECT DISTINCT(InvAmt) FROM `medihelp`.`stocks`);
                        SET TOTAL_MEDICINE = (SELECT SUm(Qty) FROM `medihelp`.`stocks`);
                        SET TOTAL_MEDICINE_AMT = (SELECT SUM(INetAmt) FROM `medihelp`.`stocks`);
                        SET TOTAL_MRP_AMT = (SELECT SUM(MRP) FROM `medihelp`.`stocks`);
                        
                        
                        INSERT INTO `medihelp`.`invoices` (Customer_code,Customer,
                                             InvNo,Vendor,InvDate,InvAmt,total_medicine,
                                            total_medicine_amount,total_MRP_amount)
                        VALUES (CUSTOMER_CODE,CUSTOMER,INVDATE,INVAMT,TOTAL_MEDICINE,
                                  TOTAL_MEDICINE_AMT,TOTAL_MRP_AMT);
                        END;
                        """
cursor.execute(invoices_trigger_query)
    

cursor.close()
conn.close()
