import pandas as pd

data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'Los Angeles', 'Chicago']
}

df = pd.DataFrame(data)


# print(df)
# df= pd.read_csv(r"C:\Users\Abubakir\Downloads\sales_data.csv")
print(df)

# df['total_sale'] = df['quantity'] * df['price']
# total_sale=df['total_sale']

# result=df.groupby('category').agg(
#                    total_sales=('total_sale', 'sum'),
#                    max_category=('total_sales', 'max'))
# print(result)

# df['total_sale'] = df['quantity'] * df['price']


# 2. Category bo‘yicha jami savdo summasini hisoblash
# result = df.groupby('category').agg(
#     total_sales=('total_sale', 'sum')  # Faqat bitta agg qiling!
# ).reset_index()

# print(result)

# max_cat=result.loc[result['total_sales'].idxmax(), 'category']

# max_r=result['total_sales'].max()

# max_R =result.loc[result['total_sales'].idxmax(), 'total_sales'] 

# print(f"Eng ko'p savdo qilingan kategoriya: {max_R} natija bilan {max_cat} egalladi")
# print()
# print(f"Eng ko'p savdo qilingan kategoriya: {max_
# r} natija bilan {max_cat} egalladi")













