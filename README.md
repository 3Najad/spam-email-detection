# spam-email-detection
## 📌 Email Spam Detection - Exploratory Data Analysis & Modelling
🔍 Problem Statement
- The goal of this project is to classify emails as spam or ham using Natural Language Processing (NLP) and machine learning techniques. The motivation is to save users' time by filtering out unwanted (spam) emails.

## 📥 Step 1: Data Loading

The dataset enronSpam.csv was loaded using Pandas.
Unnecessary columns (Unnamed: 0, Unnamed: 0.1) were identified and later removed

## 🔍 Step 2: Understanding the Data
The dataset contains two key columns:

Body: The text of the email.
Label: Target variable — 1 for spam, 0 for ham.
Initial checks included:
Data types
Null values
Shape
Duplicates

🧹 Step 3: Data Cleaning

Dropped index-related columns.
Checked and confirmed absence of null values.
Removed duplicate entries based on the email body.

📊 Step 4: Data Visualization

Visualized class distribution using countplot.
Added basic numeric features:
BodyLength: Total characters in the email.
WordCount: Number of words.
Generated a correlation heatmap to analyze relationships.

⚖️ Step 5: Class Distribution  

Checked balance in the target labels (Label).
Confirmed that the dataset was slightly imbalanced, but still manageable.
✏️ Step 6: Text Vectorization

Used TF-IDF Vectorizer from sklearn to convert email text into numerical form.
Removed English stop words.
Used the top 5000 features.
No need for additional scaling due to TF-IDF properties.

🤖 Step 7: Model Building

Train-Test Split: 80% train, 20% test.
Two models trained:
Logistic Regression
Multinomial Naive Bayes

📈 Step 8: Model Evaluation

Evaluated both models using:
Accuracy
Precision
Recall
F1 Score

✅ Results:


Model	Accuracy	Precision	Recall	F1 Score
Logistic Regression	98.86%	98.14%	99.58%	High
Naive Bayes	Very Good (but slightly lower)			
📌 Logistic Regression was selected as the final model due to better overall metrics.

📃 Step 9: Final Report

The project effectively demonstrates the use of NLP and machine learning for spam detection:
Data Preprocessing: Clean and balanced
Feature Engineering: TF-IDF vectorization
Model Performance: Logistic Regression performed with high accuracy and F1 score
