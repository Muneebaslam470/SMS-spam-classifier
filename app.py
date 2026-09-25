import streamlit as st 
import pickle
import nltk
import string
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer

ps = PorterStemmer()


def transform_text(text):
    text = text.lower()
    text = nltk.word_tokenize(text)

    y = []
    for i in text:
        if i.isalnum():
            y.append(i)

    text = y[:]
    y.clear()

    for i in text:
        if i not in stopwords.words('english') and string.punctuation:
            y.append(i)

    text = y[:]
    y.clear()

    for i in text:
        y.append(ps.stem(i))
    
    return " ".join(y)

tfidf = pickle.load(open('vectorized.pkl','rb'))
mnb = pickle.load(open('model.pkl','rb'))

st.title("SMS spam classifer/Detection")
input_sms = st.text_area("Enter Your Message here :")
if st.button('Predict'):

    transformed_sms = transform_text(input_sms)
    vectorized_input = tfidf.transform([transformed_sms])
    result = mnb.predict(vectorized_input)[0]

    if result == 1:
        st.header('spam')
    else:
        st.header('Not spam')    
