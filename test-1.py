import pandas as pd

# import os
# print(os.getcwd) # current working directory (cwd) ni ko'rsatib beradi

'''
| Date       | Product  | Quantity | Price |
| ---------- | -------- | -------- | ----- |
| 2025-01-01 | Laptop   | 3        | 700   |
| 2025-01-01 | Mouse    | 10       | 20    |
| 2025-01-02 | Keyboard | 5        | 50    |
| 2025-01-03 | Laptop   | 2        | 680   |
| 2025-01-03 | Monitor  | 1        | 200   |

Topshiriqlar:
1. Har bir mahsulotdan nechta sotilganini hisoblang.
2. Umumiy tushumni (Quantity * Price) hisoblang.
3. Eng ko‘p sotilgan mahsulotni toping.
'''
data={
    "Date":["2025-01-01", "2025-01-01", "2025-01-02", "2025-01-03", "2025-01-03"],
    "Product":["Laptop", "Mouse", "Keyboard", "Laptop", "Monitor"],
    "Quantity":["3", "10", "5", "2", "1"],
    "Price":["700", "20", "50", "680", "200"]
}

#1
df=pd.DataFrame(data)
# print(type(df))
# print()
df["Quantity"]=df["Quantity"].astype(int) # typeni int ga aylantiradi
df["Price"]=df["Price"].astype(int)       # typeni int ga aylantiradi
   
# df.to_csv("sales_dataaa.csv") ishlanayotgan mashq.py fileimiz joylashgan joyga, ya'ni cwd ga avtomatik joylab beradi
# sale_prod=df.groupby("Product")[["Quantity"]].sum().rename(columns={"Quantity":"total_Quantity"}) # [["Quantity"]].sum().rename() -ustunni nomladi
# print(type(sale_prod))   # o'zgaruvchining typeni ko'rsatadi
# sale_prod.rename(columns={"Quantity": "b"}, inplace=True)
# sale_prod.rename("ddd", inplace=True)   # bu faqat Seriesni nomini o'zgartiradi, ustunni emas
# print(sale_prod )

#2
# df['total_savdo']=df["Quantity"]*df["Price"]
# total_sale=df.groupby("Product").agg(
#     total_sav=('total_savdo', sum)
# ).reset_index()
# print(total_sale)

#3
# max_sale_prod=df.groupby("Product")["Quantity"].sum().idxmax()
# max_sale_quant=df.groupby("Product")["Quantity"].sum().max()
# print(max_sale_prod)
# print()
# print(max_sale_quant)

sale_summary=df.groupby('Product')['Quantity'].sum()
max_prod=sale_summary.idxmax()
max_quantity=sale_summary.max()

result=pd.DataFrame({
    "Product":[max_prod],
    "Quantity":[max_quantity]
})

print(result)

