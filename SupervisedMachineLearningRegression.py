# Description: This program predicts if a person can buy a house
# using a Supevised classification prediction
# Developed by Jonathan Espedal 2 June 2022 CS379-2203A-1

#Import pandas for data processing
import pandas as pd

#Import the dataset
df = pd.read_csv("C:\\Users\\BigDickJ\\Desktop\\CS379_JonathanEspedal_IP2\\realtor-dataset-100k.csv")

#Import machine learning models, trainers, and metrics
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error

# Filter and drop rows with missing values(axis=0 rows, axis=1 columns)
df = df.dropna(axis=0)
# Choose target(price) and features(Most influential to price)
y = df.price
features = ['bed', 'bath', 'acre_lot', 'house_size']
X = df[features]

train_X, val_X, train_y, val_y = train_test_split(X, y,random_state = 0)

#Random forest regression model used as the supervision algorithm
forest_model = RandomForestRegressor(random_state=1)
forest_model.fit(train_X, train_y)
melb_preds = forest_model.predict(val_X)
print(mean_absolute_error(val_y, melb_preds))