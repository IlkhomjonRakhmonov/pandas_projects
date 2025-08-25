import pandas as pd

# 🔽 CSV faylni yuklash
df = pd.read_csv(r"C:\Users\Abubakir\Downloads\sales_data_task.csv")

# 🔢 Har bir mahsulot uchun umumiy daromad (quantity * price)
df['total_sale'] = df['quantity'] * df['price']

# 📊 Kategoriya bo‘yicha umumiy daromadlar
result = df.groupby('category').agg(
    total_sales=('total_sale', 'sum')
).reset_index()

# 🔝 Eng ko‘p daromad keltirgan kategoriya
max_cat = result.loc[result['total_sales'].idxmax(), 'category']
max_r = result['total_sales'].max()

# 🖨️ Natijani chiqarish
print("🔍 Barcha kategoriyalar bo‘yicha umumiy daromad:")
print(result.to_string(index=False))
print(f"\n🏆 Eng ko‘p daromad keltirgan kategoriya: {max_cat} ({max_r})")
