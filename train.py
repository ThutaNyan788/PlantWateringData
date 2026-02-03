import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import joblib

data = pd.read_csv("./data/plant_data.csv")

# Rename columns to ML-friendly names
data = data.rename(columns={
    "Soil Moisture": "soil",
    "Temperature": "temperature",
    "Air Humidity": "humidity",
    "Pump Data": "pump"
})

X = data[['soil', 'temperature', 'humidity']]
y = data['pump']

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = DecisionTreeClassifier(max_depth=4)
model.fit(X_train, y_train)

print("Accuracy:", accuracy_score(y_test, model.predict(X_test)))

joblib.dump(model, "pump_model.pkl")
print("✅ Model trained successfully")
