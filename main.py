import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load subset for performance
df = pd.read_csv("online_retail.csv")

print(df.head())
#print(df.info())
# В таблиці є пропущені дані в 2 стовпцях стовпцях, це опис товару та ID покупця, спочатку вивчимо пропуски по стовпцю Description
#print(df[df['Description'].isna()].head(20))
# Судячи з того що в переглянутих записах Quantity часто є від'ємною, все знаходится в межах UK, а ціна на всіх відповідних замовлення дорівнює 0, дуже схоже, що це не продаж а списання бракованого товару, або переміщення товару в середені підприємства, ці записи я видалю.
 
df_copy = df[df['Description'].notnull()].copy()

counts_invoices = df_copy['InvoiceNo'].nunique()
counts_invoice_not_CustomerID = df_copy[df_copy['CustomerID'].isna()]['InvoiceNo'].nunique()
print(f"Counts_invoice_not_CustomerID, %: {round((counts_invoice_not_CustomerID/counts_invoices*100), 2)}")

# Є 15603 замовлення з яких у 1125 не вказан CustomerID, що становить 7,21%, це забагато щоб видалити, ці замовлення (можливо це не зареєстровані покупці)
# Тому я буду використовувати їх для виявлення подальшого аналізу. Спершу порівняємо країни за рівнем доходу, для нашої компанії
df_copy['Revenue'] = df_copy['Quantity']*df_copy['UnitPrice']
country_groups = df_copy.groupby(['Country'])['Revenue'].sum().sort_values(ascending=False)
country_groups = country_groups.reset_index()
#print(country_groups)

plt.figure(figsize=(18, 12))
plt.barh(country_groups['Country'], country_groups['Revenue']/1000)
plt.title('Revenue from the country in GBP')
plt.xlabel('k GBP')
plt.ylabel('Country')
plt.yticks(fontsize=10)
plt.show()
# Як видно найбільший дохід нам надає торгівля в Великій Британії (з великим відривом), на другому місці Нідерланди та на третьому Ірландія.
# Далі виявимо найпопулярніші товари для продажу.
total_products_assortment = df_copy['StockCode'].nunique()
print(f"Total assortment: {total_products_assortment}")
stockcode_group = df_copy.groupby('StockCode')['Quantity'].sum().sort_values(ascending=False).reset_index().head(25).copy()
print(stockcode_group)

plt.figure(figsize=(18, 12))
plt.bar(stockcode_group['StockCode'], stockcode_group['Quantity'])
plt.title('Top-25 products')
plt.xlabel('StockCode')
plt.xticks(rotation=45)
plt.ylabel('Quantitly')
plt.show()
# У цього магазину є явний фаворит за кількість продажу, далі хочу подивитися топ 20% всіх продаж.
limit = stockcode_group['Quantity'].quantile(0.8)
top_20pct_quantity_sales = stockcode_group[stockcode_group['Quantity'] >= limit]
print(top_20pct_quantity_sales.head())

plt.figure(figsize=(18, 12))
plt.bar(top_20pct_quantity_sales['StockCode'], top_20pct_quantity_sales['Quantity'])
plt.title('top_20pct_quantity_sales')
plt.xlabel('StockCode')
plt.xticks(rotation=45)
plt.ylabel('Quantitly')
plt.show()

top_20pct = list(top_20pct_quantity_sales['StockCode'])
print(top_20pct)
df_copy['top_20'] = df_copy['StockCode'].apply(lambda x:'Top' if x in top_20pct else '')
description_20pct=df_copy[df_copy['top_20'] == 'Top']
print(description_20pct[['StockCode', 'Description']].drop_duplicates())
# Далі подивимось на сезонність покупок.
df_copy['InvoiceDate'] = pd.to_datetime(df_copy['InvoiceDate'], format="%d.%m.%Y %H:%M")
df_copy['Month'] = df_copy['InvoiceDate'].dt.month
print(f"First invoice date: {df_copy['InvoiceDate'].min()}")
print(f"Last invoice date: {df_copy['InvoiceDate'].max()}")
# Замовлення дані з 01.12.2010 року по 09.12.2011, зроблю зріз рівно за рік, щоб зменшити вірогідність зміщення доходоності. 
df_date = df_copy[df_copy['InvoiceDate'] <= '30.11.2011']
seasons = df_date.groupby('Month')['Revenue'].sum().reset_index()
#print(seasons)
sns.set_theme(style="darkgrid")
plt.plot(seasons['Month'], seasons['Revenue']/1000)
plt.title('Seasonal yield')
plt.xlabel('Month')
plt.ylabel('k GBP')
plt.xticks([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], 
           ['Січень', 'Лютий', 'Березень', 'Квітень', 'Травень', 'Червень', 'Липень', 'Серпень', 'Вересень', 'Жовтень', 'Листопад', 'Грудень'], rotation=45)
plt.show()
