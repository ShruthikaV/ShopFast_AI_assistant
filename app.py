# === FINALIZED app.py with Improved Intent Flow and Accurate Turn Handling ===
import streamlit as st
import joblib

# Load trained model
model = joblib.load("intent_model.pkl")

# Intent to response mapping (default/fallback responses)
responses = {
    "Order Tracking": "Please share your order ID to help track your package.",
    "Return & Refund Policy": "Sure, I can help you return your item. Could you please share your order number?",
    "Product Availability": "Let me check the availability for you. Which product are you looking for?",
    "Store Location/Hours": "Our stores are open from 10 AM to 9 PM. Please share your city for nearest location.",
    "General Greetings": "Hello! Welcome to ShopFast! How can I assist you today? We offer a wide range of clothing, electronics, and accessories.",
    "Unknown/Other": "I'm sorry, I didn’t understand that. Could you rephrase your question?"
}

# Mock product catalog for keyword-based product search
product_catalog = {
    "Nike": "Nike running shoes, Nike Air Max",
    "iPhone": "iPhone 14, iPhone cases",
    "Samsung": "Samsung Galaxy phones, Samsung smartwatches",
    "jeans": "Slim-fit jeans, straight-cut jeans",
    "shoes": "Formal shoes, sneakers",
    "tops": "Women’s tops, crop tops",
    "clothes": "Men and women clothing section"
}

# Session state setup
if "context" not in st.session_state:
    st.session_state.context = {}
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []
if "return_step" not in st.session_state:
    st.session_state.return_step = 0
if "active_intent" not in st.session_state:
    st.session_state.active_intent = None

# Keyword-based context updater
def update_context(user_input):
    for keyword in product_catalog:
        if keyword.lower() in user_input.lower():
            st.session_state.context['product'] = keyword
            break

# Streamlit page config
st.set_page_config(page_title="ShopFast AI Assistant", page_icon="🛍️")
st.title("🛍️ ShopFast AI Assistant")
st.image("shop_fast.png", width=200)

st.markdown("""
Welcome to **ShopFast's Virtual Assistant**!  
This is a **multi-turn AI chatbot** designed to simulate e-commerce customer support.  
Built using **TF-IDF + Logistic Regression**, with local memory and no external APIs.
""")

st.markdown("""
💬 **Supported Query Types**:
- Order Tracking  
- Return & Refund Policy  
- Product Availability  
- Store Location / Hours  
- Greetings  
- Others (Fallback)
""")

user_input = st.chat_input("You:")
if user_input:
    update_context(user_input)
    intent = model.predict([user_input])[0]
    proba = model.predict_proba([user_input])[0]
    confidence = max(proba)

    known_low_confidence_ok = ["General Greetings", "Return & Refund Policy", "Order Tracking"]
    if confidence < 0.35 and intent not in known_low_confidence_ok:
        intent = "Unknown/Other"

    # Start a new intent or continue multi-turn if in return flow
    if st.session_state.return_step > 0:
        intent = "Return & Refund Policy"

    st.session_state.active_intent = intent
    response = responses.get(intent, responses["Unknown/Other"])

    # Multi-turn return process
    if intent == "Return & Refund Policy":
        step = st.session_state.return_step

        if step == 0:
            response = "Sure, I can help you return your item. Could you please share your order number?"
            st.session_state.return_step += 1
        elif step == 1:
            st.session_state.context['order_number'] = user_input
            response = "Got it. Could you also tell me the name or description of the item you want to return?"
            st.session_state.return_step += 1
        elif step == 2:
            st.session_state.context['item'] = user_input
            response = "Thanks. When did you purchase the item? (e.g., March 12, 2024)"
            st.session_state.return_step += 1
        elif step == 3:
            st.session_state.context['purchase_date'] = user_input
            response = "And lastly, do you still have the bill or receipt? (Yes/No)"
            st.session_state.return_step += 1
        elif step == 4:
            st.session_state.context['has_receipt'] = user_input
            order = st.session_state.context.get('order_number', 'N/A')
            item = st.session_state.context.get('item', 'the item')
            date = st.session_state.context.get('purchase_date', 'an unknown date')
            receipt = st.session_state.context.get('has_receipt', 'Unknown')
            response = f"Thank you. Your return request for {item} (Order #{order}) from {date} has been initiated. Receipt Available: {receipt}. Our team will reach out shortly."
            st.session_state.return_step = 0
            st.session_state.active_intent = None

    elif intent == "Product Availability":
        product = st.session_state.context.get("product")
        if product and product in product_catalog:
            response += f"\nHere are some popular options for {product}: {product_catalog[product]}"
        else:
            response += "\nCould you please specify the product you're looking for?"

    elif intent == "Order Tracking":
        response = responses["Order Tracking"]

    # Log and show chat with confidence
    response += f"\n\n🧠 (Confidence: {confidence:.2f})"
    st.session_state.chat_history.append(("user", user_input))
    st.session_state.chat_history.append(("bot", response))

# Render chat history
for speaker, message in st.session_state.chat_history:
    with st.chat_message(name="user" if speaker == "user" else "assistant"):
        st.markdown(message)

# Clear chat
if st.button("Clear Chat"):
    st.session_state.chat_history = []
    st.session_state.context = {}
    st.session_state.return_step = 0
    st.session_state.active_intent = None
    st.experimental_rerun()

st.markdown("""
---
🔧 *Built using scikit-learn and Streamlit.*  
🧠 *Intent classification with TF-IDF + Logistic Regression.*  
💡 *Supports multi-turn memory, return workflow, and intent continuity.*
""")