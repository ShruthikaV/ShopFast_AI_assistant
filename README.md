# ShopFast_AI_assistant

ShopFast AI Assistant: A Chatbot for E-Commerce Assistance

The ShopFast Virtual Assistant project welcomes you!

This small AI chatbot was created to mimic a simple e-commerce platform customer support agent. Without depending on any third-party or paid APIs like OpenAI or Google Dialogflow, it assists users with basic questions like order tracking, refunds, product availability, and store details.

---

## Overview of the Approach

The project is built as a rule-enhanced NLP assistant with the following capabilities:

- **Intent Classification:** User queries are classified into one of 6 predefined intents:  
  `Order Tracking`, `Return & Refund Policy`, `Product Availability`, `Store Location/Hours`, `General Greetings`, or `Unknown/Other`.

- **Machine Learning + Rule-based System:**  
  We use a traditional ML model to detect intents, supported by a fallback mechanism and rule-based enhancements for multi-turn conversations and keyword detection.

- **Multi-turn Conversation Flow:**  
  Especially for return requests, the assistant engages the user through multiple follow-up questions like:
  - Order number
  - Item description
  - Purchase date
  - Receipt confirmation  
  This creates a human-like flow without complex dialogue state management.

- **Keyword Context Handling:**  
  If a user mentions a product (e.g., “Nike shoes”), the bot remembers the keyword and can refer back to it during product availability checks.

- **Simple and Friendly Interface:**  
  Built with Streamlit to simulate a terminal-style web assistant interface.

---

## Libraries Used

The project uses open-source libraries only:

| Library         | Purpose                                        |
|----------------|------------------------------------------------|
| `scikit-learn`  | Machine learning model (TF-IDF + Logistic Regression) |
| `pandas`        | Data handling and CSV manipulation            |
| `joblib`        | Saving/loading trained ML model               |
| `Streamlit`     | Building the interactive web chatbot UI       |

---

## Model Architecture

We used a **TF-IDF vectorizer + Logistic Regression classifier** from `scikit-learn`.

- **Vectorizer:** `TfidfVectorizer()` transforms text queries into numerical features.
- **Classifier:** `LogisticRegression()` predicts the intent from these features.
- **Training Data:** A CSV (`mock_intents.csv`) containing real-like e-commerce queries mapped to one of the six intent classes.

This approach is lightweight, explainable, and effective for small to medium-scale NLP use cases.

To run the Streamlit chatbot:
```bash
pip install -r requirements.txt
python train_model.py
streamlit run app.py
```

---

## 💬 Sample Test Conversations

Below are example conversations and how the chatbot responds:

### 👋 Greetings
You: Hello
Bot: Hello! Welcome to ShopFast! How can I assist you today? We offer a wide range of clothing, electronics, and accessories.

### 📦 Order Tracking
You: Where is my order?
Bot: Please share your order ID to help track your package.

### 🔁 Return & Refund (Multi-turn)
You: I want to return my Nike shoes
Bot: Sure, I can help you return your item. Could you please share your order number?

You: 23413
Bot: Got it. Could you also tell me the name or description of the item you want to return?

You: Nike Air Max
Bot: Thanks. When did you purchase the item? (e.g., March 12, 2024)

You: March 1, 2024
Bot: And lastly, do you still have the bill or receipt? (Yes/No)

You: Yes
Bot: Thank you. Your return request for Nike Air Max (Order #23413) from March 1, 2024 has been initiated. Receipt Available: Yes. Our team will reach out shortly.

![image](https://github.com/user-attachments/assets/6a8852cf-ebf7-4fa1-a3ce-cddca375b5fd)

