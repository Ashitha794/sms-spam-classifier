import pandas as pd
import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st

# Set NLTK data path
nltk.data.path.append('D:/Users/HP/Downloads/proog/nltk_data')

# Ensure NLTK data is downloaded
nltk.download('punkt_tab', quiet=True)
nltk.download('stopwords', quiet=True)

# Load the dataset
def load_data():
    data = pd.read_csv('spam.csv', encoding='latin-1')
    data = data[['label', 'message']]  # Use correct column names
    data.columns = ['label', 'message']
    return data

# Preprocess the text
def preprocess_text(text):
    ps = PorterStemmer()
    stop_words = set(stopwords.words('english'))

    # Lowercase the text
    text = text.lower()

    # Split into words (simpler alternative to word_tokenize)
    tokens = text.split()

    # Remove punctuation and stopwords
    tokens = [word for word in tokens if word.isalnum()]
    tokens = [word for word in tokens if word not in stop_words]

    # Apply stemming
    tokens = [ps.stem(word) for word in tokens]

    return ' '.join(tokens)

# Load and prepare the data
data = load_data()
data['processed_message'] = data['message'].apply(preprocess_text)

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    data['processed_message'], data['label'], test_size=0.2, random_state=42
)

# Create the TF-IDF vectorizer
tfidf = TfidfVectorizer()
X_train_tfidf = tfidf.fit_transform(X_train)
X_test_tfidf = tfidf.transform(X_test)

# Train the Logistic Regression model
lr_model = LogisticRegression()
lr_model.fit(X_train_tfidf, y_train)
lr_predictions = lr_model.predict(X_test_tfidf)
lr_accuracy = accuracy_score(y_test, lr_predictions)

# Train the Random Forest model
rf_model = RandomForestClassifier()
rf_model.fit(X_train_tfidf, y_train)
rf_predictions = rf_model.predict(X_test_tfidf)
rf_accuracy = accuracy_score(y_test, rf_predictions)

# Train the Naive Bayes model
nb_model = MultinomialNB()
nb_model.fit(X_train_tfidf, y_train)
nb_predictions = nb_model.predict(X_test_tfidf)
nb_accuracy = accuracy_score(y_test, nb_predictions)

# Cross-validation for all models
lr_cv_scores = cross_val_score(lr_model, X_train_tfidf, y_train, cv=5)
rf_cv_scores = cross_val_score(rf_model, X_train_tfidf, y_train, cv=5)
nb_cv_scores = cross_val_score(nb_model, X_train_tfidf, y_train, cv=5)

# Streamlit web interface
st.title("SMS Spam Classifier")

# User input for the message
input_sms = st.text_area("Enter the message")

def plot_confusion_matrix(cm, model_name):
    plt.figure(figsize=(6, 5))
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', cbar=False,
                xticklabels=['Not Spam', 'Spam'], yticklabels=['Not Spam', 'Spam'])
    plt.title(f'Confusion Matrix for {model_name}')
    plt.xlabel('Predicted Label')
    plt.ylabel('True Label')
    st.pyplot(plt)

if st.button('Predict'):
    # Preprocess the input SMS
    transformed_sms = preprocess_text(input_sms)
    
    # Vectorize the input SMS
    vector_input = tfidf.transform([transformed_sms])

    # Predictions from all models
    lr_result = lr_model.predict(vector_input)[0]
    rf_result = rf_model.predict(vector_input)[0]
    nb_result = nb_model.predict(vector_input)[0]

    # Display the results
    st.subheader("Predictions:")
    st.write(f"Logistic Regression Prediction: {'Spam' if lr_result == 'spam' else 'Not Spam'} (Accuracy: {lr_accuracy:.2f}, Cross-Validation: {lr_cv_scores.mean():.2f})")
    st.write(f"Random Forest Prediction: {'Spam' if rf_result == 'spam' else 'Not Spam'} (Accuracy: {rf_accuracy:.2f}, Cross-Validation: {rf_cv_scores.mean():.2f})")
    st.write(f"Naive Bayes Prediction: {'Spam' if nb_result == 'spam' else 'Not Spam'} (Accuracy: {nb_accuracy:.2f}, Cross-Validation: {nb_cv_scores.mean():.2f})")

    # Show the classification report
    st.subheader("Classification Reports:")
    st.text("Logistic Regression:")
    st.text(classification_report(y_test, lr_predictions))
    
    st.text("Random Forest:")
    st.text(classification_report(y_test, rf_predictions))
    
    st.text("Naive Bayes:")
    st.text(classification_report(y_test, nb_predictions))

    # Plot confusion matrices
    st.subheader("Confusion Matrix (Logistic Regression):")
    lr_cm = confusion_matrix(y_test, lr_predictions)
    plot_confusion_matrix(lr_cm, "Logistic Regression")

    st.subheader("Confusion Matrix (Random Forest):")
    rf_cm = confusion_matrix(y_test, rf_predictions)
    plot_confusion_matrix(rf_cm, "Random Forest")

    st.subheader("Confusion Matrix (Naive Bayes):")
    nb_cm = confusion_matrix(y_test, nb_predictions)
    plot_confusion_matrix(nb_cm, "Naive Bayes")