import pyodbc  # pypyodbc yerine pyodbc kullan
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
server='DESKTOP-MKSKA1L'
database='salesDB'


# Bağlantıyı oluştur
conn = pyodbc.connect(
    f'DRIVER={{SQL Server}};'
    f'SERVER={server};'
    f'DATABASE={database};'
    f'Trusted_Connection=yes;'
)

quary=' SELECT STORE, MAX(WEEKLY_SALES) AS MAXPRİCE FROM train GROUP BY STORE '
DAATE='SELECT YEAR(date) AS YIL, MONTH(date) AS AY, SUM(WEEKLY_SALES) AS TOTAL_SALES FROM train GROUP BY YEAR(date), MONTH(date) ORDER BY YIL, AY ASC'


aa=pd.read_sql(quary, conn)
bb=pd.read_sql(DAATE, conn)


conn.close()
""" tarih sütünu  ay ve yılı birleştirme """
bb['tarih']= bb["YIL"].astype(str) + '-' + bb["AY"].astype(str)

print(aa.head())
print(aa.describe())
print(aa.info())
print(aa)
sns.barplot(x=aa["STORE"], y=aa["MAXPRİCE"])
plt.grid(True)
plt.xticks(rotation=90)
plt.show()

plt.figure(figsize=(10, 5))
plt.plot(bb["tarih"], bb["TOTAL_SALES"])
plt.grid(True)
plt.xticks(rotation=90)
plt.show()

plt.bar(bb['YIL'], bb['TOTAL_SALES'] )
plt.xticks(rotation=90)
plt.title("years")
plt.show()


plt.bar(bb['AY'], bb['TOTAL_SALES'])
plt.xticks(rotation=90)
plt.title("mount")
plt.show()
