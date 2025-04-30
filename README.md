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

---

## 💬 Sample Test Conversations

Below are example conversations and how the chatbot responds:

### 🔁 Return & Refund (Multi-turn)
