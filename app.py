import streamlit as st
from deep_translator import GoogleTranslator
from gtts import gTTS
import pyttsx3
import tempfile
import os

# ---------------- Streamlit UI ----------------
st.set_page_config(page_title="Text → Speech + Translation", page_icon="🎙️")
st.title("🎙️ Text to Speech + Translation")

# Input text
text_input = st.text_area("Enter text:", "Welcome to Naresh Technology Data Science Programme!", height=120)

# Language selection (added Kannada, Malayalam, Tamil)
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

# Voice selection
voice_type = st.radio("Choose Voice:", ["Male", "Female"], horizontal=True)

# Note about male/female voices
st.info("⚠️ Male/Female voice selection is only applicable for English. For other languages, a default voice will be used.")

# Generate button
if st.button("Generate Audio"):
    # Translate
    translated_text = GoogleTranslator(source="auto", target=target_lang_code).translate(text_input)
    st.success("✅ Translated text")
    st.write(translated_text)

    # Audio generation
    audio_file = None
    temp_path = None
    try:
        if target_lang_code == "en":
            # English: use pyttsx3 for male/female voices
            engine = pyttsx3.init()
            voices = engine.getProperty('voices')
            if voice_type == "Male":
                engine.setProperty('voice', voices[0].id)
            else:
                engine.setProperty('voice', voices[1].id)
            engine.setProperty('rate', 150)

            with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as fp:
                temp_path = fp.name
            engine.save_to_file(translated_text, temp_path)
            engine.runAndWait()
            engine.stop()

            audio_file = open(temp_path, "rb").read()
        else:
            # Other languages: use gTTS (only one voice available)
            with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as fp:
                temp_path = fp.name
            tts = gTTS(text=translated_text, lang=target_lang_code)
            tts.save(temp_path)
            audio_file = open(temp_path, "rb").read()

        # Play and download
        st.audio(audio_file, format="audio/mp3")
        st.download_button("Download Audio", data=audio_file, file_name="speech.mp3", mime="audio/mp3")

    finally:
        if temp_path and os.path.exists(temp_path):
            os.remove(temp_path)
