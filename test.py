# def is_power_of_two_division(n: int) -> bool:
#     if n <= 0:
#         return False
#     while n % 2 == 0:
#         n = n // 2
#     return n == 1

# # Sinov
# for i in range(1, 21):
#     print(i, is_power_of_two_division(i))

import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random

random.seed(42)
np.random.seed(42)

n = 250
start_date = datetime(2024, 1, 1)
dates = [start_date + timedelta(days=int(x)) for x in np.random.randint(0, 600, size=n)]

product_catalog = [
    ("Wireless Mouse", "Electronics"),
    ("USB-C Cable", "Electronics"),
    ("Coffee Mug", "Home"),
    ("Notebook A5", "Stationery"),
    ("Ballpoint Pen", "Stationery"),
    ("Running Shoes", "Fashion"),
    ("T-Shirt", "Fashion"),
    ("Office Chair", "Furniture"),
    ("Desk Lamp", "Home"),
    ("Water Bottle", "Home"),
    ("Backpack", "Fashion"),
    ("Headphones", "Electronics")
]

cities = ["Toshkent", "Samarqand", "Buxoro", "Fargʻona", "Namangan", "Andijon", "Nukus"]
payment_methods = ["Card", "Cash", "Online", "Bank Transfer"]

rows = []
for i in range(1, n+1):
    prod, cat = random.choice(product_catalog)
    qty = int(np.random.poisson(1.8)) + 1
    price_base = {
        "Electronics": np.random.choice([15, 20, 25, 35, 50, 80, 120]),
        "Home": np.random.choice([5, 10, 15, 20, 30]),
        "Stationery": np.random.choice([1, 2, 3, 5]),
        "Fashion": np.random.choice([10, 15, 25, 40, 60]),
        "Furniture": np.random.choice([40, 80, 120, 200])
    }[cat]
    price = round(price_base * (1 + np.random.normal(0, 0.08)), 2)
    customer_id = f"C{np.random.randint(1000, 1100)}"
    city = random.choice(cities)
    payment = random.choice(payment_methods)
    returned = np.random.rand() < 0.06
    discount = 0
    if np.random.rand() < 0.12:
        discount = round(np.random.choice([5,10,15,20]), 2)
    total = round(qty * price * (1 - discount/100), 2)
    rows.append({
        "order_id": f"O{i:05d}",
        "order_date": dates[i-1].strftime("%Y-%m-%d"),
        "customer_id": customer_id,
        "product": prod,
        "category": cat,
        "quantity": qty,
        "unit_price": price,
        "discount_pct": discount,
        "total_amount": total,
        "city": city,
        "payment_method": payment,
        "returned": returned
    })
# df = pd.DataFrame(rows)
# print("✅ Fayl yaratildi: sales_transactions.csv")

pd.set_option("display.max_columns",None)

# df.to_csv("sales_transactions.csv", index=False)
# df.to_csv("sales_transactions.csv", sep=";", encoding="utf-8", index=False, float_format="%.2f")
# df=pd.read_csv(r"C:\Users\Abubakir\pandas_projects\sales_transactions.csv", sep=";", encoding='utf-8-sig',on_bad_lines='skip')
# df=pd.read_csv(r"C:\Users\Abubakir\pandas_projects\sales_transactions.csv", encoding='utf-8')

#1
# print(df.info())
# print(df.dtypes)  ustun turini tekshirish
# print(df['order_date'])
#2
# df['orderdatetime']=pd.to_datetime(df["order_date"], format='%d.%m.%Y' )   #dayfirst=True qo'ysa xam bo'ladi
# # print(df['orderdatetime'])
# print()
# # df['datetime']
# str_datetime=df['orderdatetime'].dt.strftime("%d-%m-%Y")
# # print(str_datetime)

# df['year']=df["orderdatetime"].dt.year
# df["month"]=df["orderdatetime"].dt.month
# df["day"]=df["orderdatetime"].dt.day
# df["date"]=df["orderdatetime"].dt.date
# print(df["year"], df["month"], df["date"], df["day"])
# print(df[["year", "month", "date", "day"]])
# print(df[['orderdatetime', 'year', 'month']].head())
# print(df.head())
'''
#column larni oddiy va ustun shaklida ko'rish
print(df.head())
# sss=pd.DataFrame(df.columns, columns=['columns'])
# sss.index=sss.index+1
# sss.index.name="index"
# print(sss)

# 3/1
# df['total_amount']=pd.to_numeric(df['total_amount'], errors="coerce")
# total_sum=df.groupby(['month'])['total_amount'].sum()
# print(total_sum)
#3/2
# total_sum2=df.groupby('category')['total_amount'].sum()
# print(total_sum2)

# pivot_table=pd.pivot_table(
#     df,
#     values="total_amount",
#     index="month",
#     columns="category",
#     aggfunc=sum,
#     fill_value=0
# )
# print(pivot_table)

# prod_by_sale=df.groupby('product')['quantity'].sum().sort_values(ascending=False).head(5)
# print(prod_by_sale)
print()
# max_sale_prod=df.groupby('product')['quantity'].sum().sort_values(ascending=False).head(5)
# print(max_sale_prod)

sales=df.groupby('product')['quantity'].sum().sort_values(ascending=False)
# print(sales)
top5_values1 = pd.unique(sales.sort_values(ascending=True).values)[:5]
top5_values2 = pd.unique(sales.sort_values(ascending=False).values)[:5]
print(top5_values1)
print(top5_values2)

prod_by_sale2=sales[sales.isin(top5_values2)]
print(prod_by_sale2)'''

import csv
with open("sales_transactions.csv", encoding="utf-8") as f:
    dialect = csv.Sniffer().sniff(f.read(2000))
    print("Ajratgich:", dialect.delimiter)


















'''
Faylni pandas bilan yuklang va ustun turlarini tekshiring.
order_date ustunini datetime ga aylantiring va year hamda month ustunlarini yarating.
Umumiy savdo (total_amount) bo‘yicha:
Oyga va kategoriya bo‘yicha jami summa (pivot jadval yoki groupby).
Eng ko‘p sotilgan 5 ta mahsulotni toping (quantity bo‘yicha).
Mijozlar bo‘yicha tahlil:
Har bir customer_id uchun jami buyurtma soni va o‘rtacha chek (average_order_value).  
Top 10 eng katta mijozlarni aniqlang (jami sarf bo‘yicha).
Qaytargan buyurtmalar (returned=True) tahlili:
Qaytarish foizi umumiy buyurtmalarga nisbatan.
Qaytarishlar qaysi kategoriyalarda ko‘proq kuzatiladi?
To‘lov usuli bo‘yicha:
Har bir payment_method uchun jami summa va o‘rtacha chek.
Kichik bonus: discount_pct mavjud bo‘lgan buyurtmalarni toping va ular savdiga (total_amount) qanday ta'sir qilganini qisqacha tahlil qiling.
'''

