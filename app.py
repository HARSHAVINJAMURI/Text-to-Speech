import streamlit as st
from deep_translator import GoogleTranslator
from gtts import gTTS
import tempfile
import os

st.set_page_config(page_title="Text → Speech + Translation", page_icon="🎙️")
st.title("🎙️ Text to Speech + Translation")

# Input text
text_input = st.text_area("Enter text:", "Welcome to Naresh Technology Data Science Programme!", height=120)

# Language selection
languages = {
    "English": "en",
    "Hindi": "hi",
    "Telugu": "te",
    "Kannada": "kn",
    "Malayalam": "ml",
    "Tamil": "ta",
    "French": "fr",
    "Spanish": "es"
}
target_lang_name = st.selectbox("Translate To:", list(languages.keys()))
target_lang_code = languages[target_lang_name]

# Note about male/female voice
#st.info("⚠️ Male/Female voice is not available online. For English, offline pyttsx3 can use male/female locally.")

# Generate button
if st.button("Generate Audio"):
    # Translate
    translated_text = GoogleTranslator(source="auto", target=target_lang_code).translate(text_input)
    st.success("✅ Translated text")
    st.write(translated_text)

    # Generate audio with gTTS (works online for all languages)
    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as fp:
        temp_path = fp.name
    tts = gTTS(text=translated_text, lang=target_lang_code)
    tts.save(temp_path)
    audio_file = open(temp_path, "rb").read()

    # Play and download
    st.audio(audio_file, format="audio/mp3")
    st.download_button("Download Audio", data=audio_file, file_name="speech.mp3", mime="audio/mp3")

    # Cleanup
    if os.path.exists(temp_path):
        os.remove(temp_path)

