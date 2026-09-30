import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load subset for performance
df = pd.read_csv("online_retail.csv")

print(df.info())
df['Revenue'] = df['Quantity']*df['UnitPrice']
country_groups = df.groupby(['Country'])['Revenue'].sum().sort_values(ascending=False)
country_groups = country_groups.reset_index()
print(country_groups)

plt.figure(figsize=(18, 12))
plt.barh(country_groups['Country'], country_groups['Revenue']/1000)
plt.title('Revenue from the country in GBP')
plt.xlabel('k GBP')
plt.ylabel('Country')
plt.yticks(fontsize=10)
plt.show()

stockcode_group = df.groupby('StockCode')['Quantity'].sum().sort_values(ascending=False).reset_index().head(50)
print(stockcode_group)

plt.figure(figsize=(18, 12))
plt.bar(stockcode_group['StockCode'], stockcode_group['Quantity'])
plt.title('Top-50 products')
plt.xlabel('StockCode')
plt.xticks(rotation=45)
plt.ylabel('Quantitly')
plt.show()

limit = stockcode_group['Quantity'].quantile(0.8)
top_20pct_quantity_sales = stockcode_group[stockcode_group['Quantity'] > limit]
print(top_20pct_quantity_sales.head())

plt.figure(figsize=(18, 12))
plt.bar(top_20pct_quantity_sales['StockCode'], top_20pct_quantity_sales['Quantity'])
plt.title('top_10pct_quantity_sales')
plt.xlabel('StockCode')
plt.xticks(rotation=45)
plt.ylabel('Quantitly')
plt.show()
