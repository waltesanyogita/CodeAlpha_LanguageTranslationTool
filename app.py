import streamlit as st
from deep_translator import GoogleTranslator

st.set_page_config(
    page_title="Language Translation Tool",
    page_icon="🌍",
    layout="centered"
)

# Custom CSS
st.markdown("""
<style>

.main {
    background-color: #f5f7ff;
}

.title-box {
    background: linear-gradient(90deg,#6a11cb,#2575fc);
    padding: 25px;
    border-radius: 15px;
    text-align: center;
    color: white;
    margin-bottom: 20px;
}

.stButton > button {
    width: 100%;
    background: linear-gradient(90deg,#6a11cb,#2575fc);
    color: white;
    border-radius: 10px;
    border: none;
    height: 3em;
    font-size: 18px;
    font-weight: bold;
}

.result-box {
    background-color: #e8fff1;
    padding: 20px;
    border-radius: 10px;
    border-left: 5px solid green;
    font-size: 22px;
}

.footer {
    text-align: center;
    color: gray;
    margin-top: 20px;
}

</style>
""", unsafe_allow_html=True)

# Header
st.markdown("""
<div class="title-box">
<h1>🌍 Language Translation Tool</h1>
<h4>Translate Text Between Multiple Languages Instantly</h4>
</div>
""", unsafe_allow_html=True)

# Languages
languages = {
    "English": "en",
    "Hindi": "hi",
    "French": "fr",
    "German": "de",
    "Spanish": "es",
    "Japanese": "ja",
    "Chinese": "zh-CN",
    "Arabic": "ar"
}

# Text Input
text = st.text_area(
    "✍️ Enter Your Text",
    height=180,
    placeholder="Type something here..."
)

# Language Selection
col1, col2 = st.columns(2)

with col1:
    source = st.selectbox(
        "🌐 Source Language",
        list(languages.keys())
    )

with col2:
    target = st.selectbox(
        "🎯 Target Language",
        list(languages.keys())
    )

# Translate Button
if st.button("✨ Translate"):

    if text.strip() == "":
        st.warning("Please enter some text.")
    else:
        translated = GoogleTranslator(
            source=languages[source],
            target=languages[target]
        ).translate(text)

        st.markdown("### ✅ Translated Text")

        st.markdown(
            f"""
            <div class="result-box">
            {translated}
            </div>
            """,
            unsafe_allow_html=True
        )

        st.success("Translation completed successfully!")

# Footer
st.markdown("""
<div class="footer">
💜 Made for CodeAlpha AI Internship
</div>
""", unsafe_allow_html=True)