import pandas as pd
from some_thing import read_csv_auto
# import matplotlib as plt
# import matplotlib.pyplot as plt

# df=read_csv_auto(r"C:\Users\Abubakir\Downloads\sales_data_sample.csv")
# print(df.head())

# pd.set_option('display.max_rows', 100)
# pd.set_option('display.max_rows', None)   # barcha qatorlarni ko‘rsatadi
# pd.set_option('display.max_columns', None)  # barcha ustunlarni ko‘rsatadi
# df=pd.read_csv(r"C:\Users\Abubakir\Downloads\sales_data_sample.csv", encoding='latin1', sep=';')
# print(df)
#1
# print(df.head(10))
# uniqe_Stores=df.groupby('CITY')['SALES'].sum().to_frame().rename(columns={'a':'a'})
# print(uniqe_Stores)

#3
# total_Stores=df.groupby('CITY')['SALES'].sum().sort_values(ascending=False).reset_index(name="total_sales")
# total_Stores.index=total_Stores.index+1
# print(total_Stores)

#2 
# uniqeStores=df['CITY'].unique()
# print(uniqeStores)

# for i, z in enumerate(uniqeStores, start=1):
#     print(i, z)

#4
# top_Prod=df.groupby('CITY')['SALES'].sum().sort_values(ascending=False).head(5).reset_index(name='sale')
# top_Prod.index=top_Prod.index+1
# print(top_Prod)

# #5
# df['ORDERDATE']=pd.to_datetime(df['ORDERDATE'])
# df['MONTH']=df['ORDERDATE'].dt.month
# # print(df['MONTH'])
# sales_by_month=df.groupby('MONTH')['SALES'].sum()
# print(sales_by_month)

# chiziqli grfik
# plt.figure(figsize=(8, 5))
# plt.plot(sales_by_month.index, sales_by_month.values, marker='o', linestyle='-', color='b')
# plt.title("Oylar bo‘yicha umumiy savdo")
# plt.xlabel("Oy")
# plt.ylabel("Umumiy savdo summasi")
# plt.grid(True)
# plt.show()


# Bar chart chizish
# plt.figure(figsize=(5,5))
# plt.bar(sales_by_month.index, sales_by_month.values, color='skyblue', edgecolor='black')
# plt.title("Oylar bo‘yicha umumiy savdo (Bar Chart)")
# plt.xlabel("Oy")
# plt.ylabel("Umumiy savdo summasi")
# plt.xticks(sales_by_month.index)   # oy raqamlari ko‘rinib turishi uchun
# plt.show()


# for i, z in enumerate(df['MONTH'].head(10)):
    # print(i, z)



# 1 Dataset’ni pandas orqali yuklash va birinchi 10 qatorini ko‘rsatish.
# 2 Nechta noyob do‘kon (Store) borligini aniqlash.
# 3 Har bir do‘kon bo‘yicha umumiy savdo summasini (Total) hisoblash.
# 4 Eng ko‘p sotilgan top 5 mahsulot ro‘yxatini tuzish (Quantity bo‘yicha).
# 5 Oylar bo‘yicha umumiy savdoni hisoblash va grafik chizish (Matplotlib yoki Seaborn bilan).
# 6 Eng yuqori savdo qilgan oy va eng past savdo qilgan oyni aniqlash.
# 7 Har bir kategoriya bo‘yicha o‘rtacha narxni (Price) hisoblash.
# 8 Eng qimmat mahsulot va eng arzon mahsulotni topish.
# 9 Faqat 500$ dan ortiq bo‘lgan buyurtmalarni filtrlab chiqarish.
# 10 Natijalarni CSV faylga saqlash (results.csv)

# df['ORDERDATE']=pd.to_datetime(df['ORDERDATE'])
# df['MONTH']=df['ORDERDATE'].dt.month
# # # print(df['MONTH'])
# # sales_by_month=df.groupby(df['MONTH'])['SALES'].sum().head(5).sort_values(ascending=False)
# # print(sales_by_month)
# sales_by_month=df.groupby(df['MONTH'])['SALES'].sum()

# a=sales_by_month
# print("eng katta savdo bo'lgan oy ",a.idxmax(),"- oy bo'lib, bu oyda ", a.max(), " miqdorida savdo bo'ldi")

# df['ORDERDATE']=pd.to_datetime(df['ORDERDATE'])
# df['MONTH']=df['ORDERDATE'].dt.month
# df['MONTH_NAME']= df['ORDERDATE'].dt.month_name()
# sales_by_month=df.groupby(['MONTH','MONTH_NAME'])['SALES'].sum().reset_index()
# s_b_m=sales_by_month['SALES'].idxmax()
# best_month=sales_by_month.loc[s_b_m,'SALES']
# best_month_name=sales_by_month.loc[s_b_m, 'MONTH_NAME']
# print("Eng katta savdo bo'lgan oy ",best_month_name," bo'lib, bu oyda ",best_month, " miqdorida savdo bo'ldi" )