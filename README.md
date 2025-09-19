# 🎙️ Text to Speech + Translation App

This is a **Streamlit app** that allows you to:

* Translate text into multiple languages 🌍
* Convert translated text into **speech (audio)** 🔊
* Play the audio inside the app 🎧
* Download the generated audio as an MP3 📥

---

## 🚀 Features

* Input text in any language
* Choose from multiple target languages (English, Hindi, Telugu, Kannada, Malayalam, Tamil, French, Spanish)
* Real-time translation using **Google Translator**
* Speech synthesis using **gTTS (Google Text-to-Speech)**
* Instant audio playback
* Option to **download the audio** for offline use

---

## 🛠️ Tech Stack

* [Streamlit](https://streamlit.io/) - Frontend
* [Deep Translator](https://pypi.org/project/deep-translator/) - Translation
* [gTTS](https://pypi.org/project/gTTS/) - Text-to-Speech
* Python standard libraries (`tempfile`, `os`)

---

## 📦 Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/your-username/text-to-speech-translation.git
   cd text-to-speech-translation
   ```

2. Create a virtual environment (recommended):

   ```bash
   python -m venv venv
   source venv/bin/activate   # On Linux/Mac
   venv\Scripts\activate      # On Windows
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

---

## ▶️ Usage

Run the app with:

```bash
streamlit run app.py
```

Then open the link in your browser (default: [http://localhost:8501](http://localhost:8501)).

---

## 📂 Requirements

`requirements.txt`

```txt
streamlit
deep-translator
gTTS
```

---

## 🎯 Example

Input:

```
Welcome to my github HARSHAVINJAMURI!
```

Target Language: **Telugu**

👉 Output: Translated Telugu text will be displayed, and you can listen or download the generated Telugu audio.

---

## ⚠️ Notes

* **Male/Female voice selection is not available in gTTS.**
* For **English (offline use)**, you can integrate `pyttsx3` to choose male/female voices, but it won’t support other languages.

---

## 📜 License

This project is licensed under the **MIT License**.

---

💡 Made with ❤️ using Streamlit
