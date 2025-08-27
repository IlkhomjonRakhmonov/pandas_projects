import pandas as pd
import matplotlib.pyplot as plt

# 1. CSV faylni o‘qish
df = pd.read_csv(r"C:\Users\Abubakir\Downloads\sales_data_task.csv")

# 2. Umumiy savdo ustunini hisoblash
df['total_sale'] = df['quantity'] * df['price']

# 3. Kategoriya bo‘yicha jami savdo
result = df.groupby('category').agg(
    total_sales=('total_sale', 'sum')
).reset_index()

# 4. Eng katta savdoga ega kategoriya
max_cat = result.loc[result['total_sales'].idxmax(), 'category']
max_val = result['total_sales'].max()

print(result)
print(f"Eng ko'p daromad keltirgan kategoriya: {max_cat} ({max_val})")

# 5. 📊 Grafikni chizish
plt.figure(figsize=(8, 5))
plt.bar(result['category'], result['total_sales'])

# Grafikga yozuvlar
plt.title('Kategoriya bo‘yicha umumiy savdo')
plt.xlabel('Kategoriya')
plt.ylabel('Umumiy savdo')

# Grafikni ko‘rsatish ...
plt.tight_layout()
# plt.show()
#bu gitga 27.08.2025 yil kuni yuklandi
