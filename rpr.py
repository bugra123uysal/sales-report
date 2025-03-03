import pyodbc  # pypyodbc yerine pyodbc kullan
import pandas as pd

server='DESKTOP-MKSKA1L'
database='salesDB'


# Bağlantıyı oluştur
conn = pyodbc.connect(
    f'DRIVER={{SQL Server}};'
    f'SERVER={server};'
    f'DATABASE={database};'
    f'Trusted_Connection=yes;'
)

quary='SELECT * FROM train'

aa=pd.read_sql(quary, conn)

conn.close()

print(aa.head())
print(aa.describe())

