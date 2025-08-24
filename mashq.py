# ...Quyidagi CSV faylni Pandas yordamida yuklang va quyidagi vazifalarni bajaring:

# 1. Har bir product uchun total_sale ustunini yarating (quantity * price)
# 2. Har bir category bo‘yicha jami total_sale ni hisoblang
# 3. Eng ko‘p daromad keltirgan categoryni toping
# 4. Natijani chiroyli chop eting...

#    product_id product_name category   sale_date  quantity  price  total_sale
# 0         101        Mouse     Tech  2025-07-01         5    100         500
# 1         102     Keyboard     Tech  2025-07-01         3    200         600
# 2         103   Coffee Mug  Kitchen  2025-07-02        10     50         500
# 3         104          Pen   Office  2025-07-02        20     30         600
# 4         105     Notebook   Office  2025-07-03        15     70        1050
# 5         106      Monitor     Tech  2025-07-03         2    500        1000
# 6         107        Chair   Office  2025-07-04         7    100         700 
from datetime import datetime
import pandas as pd
#pd.set_option('display.max_rows', 5)
# pd.set_option('display.max_columns', 3)
#pd.describe_option()

df=pd.read_csv(r"C:\Users\Abubakir\Downloads\sales_data_task.csv") #, index_col=0)
#print(df)
print(df.points.describe())

# print(df.loc[~df.category.isin(['Office','Tech'])]) # ~ belgisi boolean ifodani teskarisiga o'giradi, isin - bormi degani

# df['izoh']='yaxshi'
# print(df['izoh'])
df['index_backwards']=range(len(df), 0, -1)
#print(df['index_backwards'])

#print(df.head(3))

# print(df.tail(2))

# print(df.mean(numeric_only=True))
# print(df['quantity'].mean())
# print(df['price'].mean())

#print(pd.DataFrame(df['category'].unique(), columns=['category']))

# print(df['category'].value_counts(ascending=True))
# print(df['category'].value_counts(normalize=True)*100)

df['total_sale'] = df['quantity'] * df['price']
# print(df.loc[2,'category'])
# print(df.iloc[2,2])

# print(df.iloc[:,1])
# print()
# print(df.loc[2:,'category'])

# print(df.iloc[[-1],1])
#print(df.iloc[-2:])
# print()
# print(df.loc[2:,'category'])

# print(df['product_name'][2])
# print(df.set_index('price'))

# print(df.product_name[0])

# print(df.category=='Tech')
# print()
# print(df.loc[df.category=='Tech'])

# print(df.loc[(df.category=='Tech')&(df.price>=200) ])


# print()

# print(df.loc[(df.category=="Tech")|(df.price>=100)])

#now=datetime.now()
now = datetime.now()
timeStamp=now.strftime("%Y-%m-%d_%H-%M-%S")

result= df.groupby('category').agg(
    total_sales=('total_sale', 'sum'),
    average_price=('price', 'mean'),
    total_quantity=('quantity', 'sum'),
).reset_index()

# print(result)

# max_cat=result.loc[result['total_sales'].idxmax(),'category']
# max_r=result['total_sales'].max()

# print(f"Eng ko'p daromad keltirgan kategoriya: {max_cat} ({max_r})")
# #df.to_csv(r"C:\Users\Abubakir\Downloads\sales_data_task_with_totall.csv", index=False)
# file_path=fr"C:\Users\Abubakir\Downloads\sales_data_task_category_totals_{timeStamp}.csv"
# result.to_csv(file_path, index=False)
# print(f"📁 Fayl saqlandi: {file_path}")

# print(df.head(3))
# print(df.shape)

