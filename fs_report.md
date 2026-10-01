-e This file is a merged representation of the entire codebase, combined into a single document

## Purpose
This file contains a packed representation of the entire repository's contents.
It is designed to be easily consumable by AI systems for analysis, code review,
or other automated processes.

## File Format
The content is organized as follows:
1. This summary section
2. Repository information
3. Directory structure
4. Multiple file entries, each consisting of:
  a. A header with the file path (## File: path/to/file)
  b. The full contents of the file in a code block or first three lines for files with .csv extensions

## Usage Guidelines
- This file should be treated as read-only. Any changes should be made to the
  original repository files, not this packed version.
- When processing this file, use the file path to distinguish
  between different files in the repository.
- Be aware that this file may contain sensitive information. Handle it with
  the same level of security as you would the original repository.

## Notes
- This file includes only .ipynb and .csv file contents in full or partial form
- All other file types are represented only through the directory structure
- Binary files are not included in this packed representation. Please refer to the Repository Structure section for a complete list of file paths, including binary files

# Directory Structure

````
./
fs_report.md
main.py
online_retail.csv
````
-e 
# Files
-e 
## File: online_retail.csv
````
,InvoiceNo,StockCode,Description,Quantity,InvoiceDate,UnitPrice,CustomerID,Country
0,536370,22728,ALARM CLOCK BAKELIKE PINK,24,01.12.2010 08:45,3.75,12583.0,France
1,536370,22727,ALARM CLOCK BAKELIKE RED ,24,01.12.2010 08:45,3.75,12583.0,France
````
-e 
## File: main.py
````
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load subset for performance
df = pd.read_csv("online_retail.csv")

#print(df.head())
#print(df.info())
# В таблиці є пропущені дані в 2 стовпцях стовпцях, це опис товару та ID покупця, спочатку вивчимо пропуски по стовпцю Description
#print(df[df['Description'].isna()].head(20))
# Судячи з того що в переглянутих записах Quantity часто є від'ємною, все знаходится в межах UK, а ціна на всіх відповідних замовлення дорівнює 0, дуже схоже, що це не продаж а списання бракованого товару, або переміщення товару в середені підприємства, ці записи я видалю.
 
df_copy = df[df['Description'].notnull()]

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
stockcode_group = df_copy.groupby('StockCode')['Quantity'].sum().sort_values(ascending=False).reset_index().head(25)
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
df_copy['top_20'] = df['StockCode'].apply(lambda x:'Top' if x in top_20pct else '')
print(df_copy[df_copy['StockCode'] == 'Top'])
# Далі подивимось на сезонність покупок.

````
