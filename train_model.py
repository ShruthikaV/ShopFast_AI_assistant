import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import make_pipeline
import joblib

# Load expanded training data
data = pd.read_csv('mock_intents.csv')

# Create and train the model pipeline
model = make_pipeline(TfidfVectorizer(), LogisticRegression())
model.fit(data['User_Query'], data['Intent'])

# Save model
joblib.dump(model, 'intent_model.pkl')
print("✅ Model saved to intent_model.pkl")