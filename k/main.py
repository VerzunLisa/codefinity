from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler
import pandas as pd
from sklearn.model_selection import GridSearchCV

df = pd.read_csv('https://codefinity-content-media.s3.eu-west-1.amazonaws.com/b71ff7ac-3932-41d2-a4d8-060e24b00129/starwars_binary.csv')

X = df.drop('StarWars6', axis=1)
y = df['StarWars6']

scaler = StandardScaler()
X = scaler.fit_transform(X)

knn = KNeighborsClassifier()

# Write your code below
param_grid = {'n_neighbors': [3, 9, 18, 27]}
grid_search = GridSearchCV(estimator=knn,param_grid=param_grid, cv=4)
grid_search.fit(X, y)
best_model = grid_search.best_estimator_
best_score = grid_search.best_score_

print(best_model)
print(best_score)