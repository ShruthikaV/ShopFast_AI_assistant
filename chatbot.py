import joblib

# Load trained model
model = joblib.load("intent_model.pkl")

# Intent to response mapping
responses = {
    "Order Tracking": "Please share your order ID to help track your package.",
    "Return & Refund Policy": "You can return items within 30 days. Please visit our Return Center.",
    "Product Availability": "Let me check the availability for you. Which product are you looking for?",
    "Store Location/Hours": "Our stores are open from 10 AM to 9 PM. Please share your city for nearest location.",
    "General Greetings": "Hello! How can I assist you today?",
    "Unknown/Other": "I'm sorry, I didn’t understand that. Could you rephrase your question?"
}

context = {}

def update_context(user_input):
    keywords = ['Nike', 'iPhone', 'Samsung', 'jeans', 'shoes', 'tops', 'clothes']
    for word in keywords:
        if word.lower() in user_input.lower():
            context['product'] = word
            break

print("Welcome to ShopFast AI Assistant! Type 'exit' to quit.")
while True:
    user_input = input("You: ")
    if user_input.lower() == 'exit':
        break

    update_context(user_input)
    intent = model.predict([user_input])[0]
    proba = model.predict_proba([user_input])[0]
    confidence = max(proba)

    if confidence < 0.5:
        intent = "Unknown/Other"

    response = responses.get(intent, responses["Unknown/Other"])

    if 'product' in context and intent == "Product Availability":
        response += f" Previously, you mentioned {context['product']}. Would you like to check that again?"

    print("Bot:", response)
