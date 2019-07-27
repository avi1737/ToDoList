import sys
import os
sys.path.append(os.getcwd())
import pandas as pd
try:
	import pdfplumber
except :
	os.system("pip3 install pdfplumber")
	import pdfplumber
import config as cfg
pdf_file = sys.argv[-1]
pdf = pdfplumber.open(pdf_file)
pages= pdf.pages[0]
table = pages.extract_tables()
df = pd.DataFrame(table[1:], columns=table[0])

#df.to_sql('buying_medicine' , conn , if_exists = append)
