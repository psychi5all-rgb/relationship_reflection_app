import streamlit as st
import joblib

from signal_extraction import extract_signals
from suggestions import get_suggestion

model = joblib.load("pattern_classifier.pkl")
vectorizer = joblib.load("vectorizer.pkl")

st.title("Relationship Communication Reflection Tool")

st.markdown(
"""
:red[IMPORTANT NOTICE]

If a relationship involves physical harm, threats, or intimidation,
do not rely on this application. Seek help from trusted individuals
or appropriate authorities.
"""
)

relationship = st.selectbox(
"Relationship type",
[
"Spouse / Partner",
"Romantic partner",
"Parent",
"Sibling",
"Cousin",
"Uncle / Aunt",
"Friend",
"Other family member"
]
)

text = st.text_area("Describe what happened during the interaction")

if st.button("Analyze communication pattern"):

    if len(text) < 5:
        st.warning("Please describe the situation.")
    
    else:

        signals = extract_signals(text)

        X = vectorizer.transform([text])

        prediction = model.predict(X)[0]

        st.subheader("Possible communication pattern")

        st.write(prediction)

        st.subheader("Explanation and suggestion")

        st.write(get_suggestion(prediction))

        st.subheader("Signal extraction summary")

        st.write(signals)

        feedback = st.radio(
        "Does this interpretation seem accurate?",
        ["Yes","Partly","No","Not sure"]
        )

        st.write("Feedback recorded:", feedback)