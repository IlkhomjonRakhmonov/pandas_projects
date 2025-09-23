import pandas as pd
from io import StringIO
'''
import pandas as pd
import numpy as np

df = pd.DataFrame({
    "A": [1, np.nan, 3, None, 5]
})

print("isna():")
print(df["A"].isna())

print("\nnotna():")
print(df["A"].notna())
'''
'''
Muhim jihatlar:
import pandas as pd
print(pd.__version__)
on='customer_id' → ikkita jadvalni qaysi ustun bo‘yicha bog‘lash kerakligini ko‘rsatadi.
how= parametri:
'inner' → faqat mos keladigan qatorlar (default)
'left' → chap jadval hammasi, o‘ngdagidan mos kelganlari
'right' → o‘ng jadval hammasi
'outer' → ikkala jadval to‘liq, mos bo‘lmagan joylarda NaN
'''
'''
customers = pd.DataFrame({
    'customer_id': [1, 2, 3],
    'name': ['Ali', 'Vali', 'Hasan']
})

# 2-jadval
orders = pd.DataFrame({
    'order_id': [101, 102, 103, 104],
    'customer_id': [1, 2, 2, 3],
    'amount': [250, 400, 300, 150]
})

merged=pd.merge(orders, customers, on='customer_id', how='inner', )
print(merged)
'''
data="""
customer_id,name,city
1,Ali,Tashkent
2,Vali,Samarkand
3,Hasan,Bukhara
4,Sara,Andijan
"""
customers=pd.read_csv(StringIO(data))
print(customers)

data2="""
order_id,customer_id,amount
101,1,250
102,2,400
103,2,300
104,3,150
105,5,500
"""
orders=pd.read_csv(StringIO(data2))
print(orders)

innerMerge=pd.merge(customers, orders, how="inner", on="customer_id")
# print(innerMerge)
leftMerge=pd.merge(customers, orders, how="left", on="customer_id")
# print(leftMerge)
rightMerge1=pd.merge(orders, customers,  how="right", on="customer_id")
# print(rightMerge1)
rightMerge2=pd.merge(customers,orders,  how="right", on="customer_id")
# print(rightMerge2)
outerMerge=pd.merge(customers, orders, how='outer', on='customer_id')
# print(outerMerge)
# nanMerge=pd.merge(customers, orders, how='outer', on='customer_id')
# nanCustomer=nanMerge.groupby('customer_id')
# print(nanMerge)
# nanValue=pd.merge(orders,  customers,  how='left', on='customer_id')
# natija=nanValue[nanValue['name'].notna()]
# print(natija)
# a=pd.merge(orders,  customers,  how='inner', on='customer_id')
# print(a)

# merged=pd.merge(customers, orders, how='left', on='customer_id')
# nan_customer=merged[merged['order_id'].isna()]
# print(nan_customer)
# nan_customer2=customers[~customers['customer_id'].isin(orders['customer_id'])]
# print(nan_customer2)
merging=pd.merge(customers, orders, how='left', on='customer_id')
buyurtma=merging.groupby('city')['amount'].sum()
print(buyurtma)



'''
Topshiriqlar
customers.csv va orders.csv fayllarini pd.read_csv() yordamida o‘qib oling.
Ikkala faylni customer_id bo‘yicha inner merge qiling.
 Faqat buyurtma qilgan mijozlar chiqadi.
left merge qiling: barcha customers jadvali saqlansin, buyurtmasi yo‘q bo‘lsa NaN chiqsin.
right merge qiling: barcha orders jadvali saqlansin, mijoz topilmasa NaN.
outer merge qiling: ikkala jadval ham to‘liq chiqsin.
Har bir mijozning jami buyurtma summasini hisoblang (groupby + sum).
city bo‘yicha jami buyurtmalarni toping.
Buyurtmasi yo‘q mijozlarni alohida jadval qilib chiqaring.
'''

