import numpy as np
import pandas as pd
from sklearn.preprocessing import OrdinalEncoder, OneHotEncoder

# Creating a dataset
data = pd.DataFrame({
    'Age': [25, np.nan, 30, 35, np.nan],
    'City': ['New York', 'London', 'Paris', 'Berlin', 'London'],
    'Income': ['Low', 'Middle', 'High', 'High', 'Middle']
})

# Write your code below
data['Age'] = data['Age'].apply(lambda x: data['Age'].mean() if np.isnan(x) else x)

city_encoder = OneHotEncoder(drop='first')
city_encoded = city_encoder.fit_transform(data[['City']])
city_encoded_df = pd.DataFrame(city_encoded.toarray(), columns=city_encoder.categories_[0][1:])

income_encoder = OrdinalEncoder(categories=[['Low', 'Middle', 'High']])
data['Income'] = income_encoder.fit_transform(data[['Income']])

# Combining the encoded columns with the original data
data = pd.concat([data, city_encoded_df], axis=1)
data.drop('City', axis=1, inplace=True)

# Testing the result
print(data)