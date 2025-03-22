import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

# Load dataset
data = pd.read_csv("plastic_data.csv")

# Encode product names into numbers
data['product'] = data['product'].astype('category').cat.codes

# Features (X) and Target (y)
X = data[['product', 'quantity', 'total_plastic_waste']]
y = data['production_allowed']

# Split into training & testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train Random Forest Classifier
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Save the model
pickle.dump(model, open("ai_model.pkl", "wb"))

print("AI model trained and saved!")
