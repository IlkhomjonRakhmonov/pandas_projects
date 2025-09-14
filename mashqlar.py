import pandas as pd
'''
Muhim jihatlar:
on='customer_id' → ikkita jadvalni qaysi ustun bo‘yicha bog‘lash kerakligini ko‘rsatadi.
how= parametri:
'inner' → faqat mos keladigan qatorlar (default)
'left' → chap jadval hammasi, o‘ngdagidan mos kelganlari
'right' → o‘ng jadval hammasi
'outer' → ikkala jadval to‘liq, mos bo‘lmagan joylarda NaN
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