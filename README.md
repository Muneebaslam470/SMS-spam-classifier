#  SMS Spam Classifier

An end-to-end Machine Learning web application designed to classify SMS messages as **Spam** or **Ham** (Not Spam). The project covers complete data preprocessing, exploratory data analysis (EDA), model training using Naive Bayes algorithms, and an interactive frontend built with **Streamlit**.

---

## 🚀 Key Features

- **Text Cleaning & Preprocessing:**
  - Lowercasing text
  - Tokenization
  - Removing special characters, punctuation, and stopwords
  - Stemming using NLTK's PorterStemmer
- **Exploratory Data Analysis (EDA):**
  - Character, word, and sentence counts analysis
  - Class distribution and correlation analysis
  - Spam vs. Ham word patterns visualization
- **Model Training & Evaluation:**
  - Feature extraction using `TfidfVectorizer` / `CountVectorizer`
  - Comparison of Naive Bayes classifiers (MultinomialNB, GaussianNB, BernoulliNB)
  - Evaluated on Accuracy and Precision (optimizing for high precision to prevent false positives)
- **Interactive UI:**
  - Real-time text prediction built with Streamlit

---

## 🛠️ Tech Stack & Libraries

- **Language:** Python
- **Data Handling & EDA:** Pandas, NumPy, Matplotlib, Seaborn
- **NLP Toolkit:** NLTK
- **Machine Learning:** Scikit-Learn (Multinomial Naive Bayes)
- **Web Interface:** Streamlit
- **Model Serialization:** Pickle
