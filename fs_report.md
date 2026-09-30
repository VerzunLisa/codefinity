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

total_quantily_sales = df['Quantity'].sum()

print(total_quantily_sales)````
