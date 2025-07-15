# 🤖 Voice-Activated AI Assistant – J.A.R.V.I.S.

A simple Python-based voice assistant that performs tasks like opening applications/websites, telling the current time/date, playing music, and answering AI-powered queries using Google's Generative AI. Inspired by J.A.R.V.I.S. from the Iron Man series.

## 🔥 Features

- 🎙️ Converts your **speech to text** using `speech_recognition`
- 🗣️ Speaks responses using `pyttsx3` TTS engine
- 🌐 Opens popular **websites** and **Windows apps**
- 🎵 Plays local **music files**
- 🕒 Tells current **day, date, and time**
- 🤖 Generates intelligent responses using **Google Generative AI (Gemini)**

## 📁 Project Structure

```
Voice-activated-AI-assistant/
│
├── main.py                   # Main script to run J.A.R.V.I.S.
├── datasets/                 # (Optional) Folder for AI input/output
└── OpenAI_Response/          # Folder to store generative AI responses
```

## 🧠 Tech Stack

| Component              | Library                     |
|------------------------|-----------------------------|
| Voice Recognition      | `speech_recognition`        |
| Text-to-Speech         | `pyttsx3`                   |
| Browser & App Control  | `webbrowser`, `os`, `subprocess` |
| Date & Time Handling   | `datetime`                  |
| Generative AI          | `google.generativeai` (Gemini) |

## 🛠️ Installation

```bash
# Clone the repository
git clone https://github.com/your-username/Voice-activated-AI-assistant.git
cd Voice-activated-AI-assistant

# Create virtual environment (optional but recommended)
python -m venv venv
venv\Scripts\activate     # On Windows

# Install dependencies
pip install -r requirements.txt
```

<details>
<summary>📦 Dependencies</summary>

```txt
speechrecognition
pyttsx3
google-generativeai
pyaudio        # For microphone access
```
</details>

## 🚀 How to Use

1. Make sure your microphone is connected.
2. Run the assistant:
   ```bash
   python main.py
   ```
3. Speak one of the following commands:
   - "Open YouTube"
   - "Open Notepad application"
   - "Play music"
   - "What's the time it is?"
   - "Tell me something using artificial intelligence"

## 🧪 Example Commands

| Command                              | Action                                 |
|--------------------------------------|----------------------------------------|
| `Open Google`                        | Opens [google.com](https://google.com) |
| `Open calculator application`        | Opens Windows calculator               |
| `Play music`                         | Plays `Wiz_Khalifa.mp3` in WMP         |
| `What's the time it is?`            | Speaks current time, date, day         |
| `Tell me about black holes using artificial intelligence` | AI-powered answer using Gemini |

## 🔐 API Key Notice

This project uses **Google Generative AI API**. Replace your actual API key here in the code:

```python
genai.configure(api_key="YOUR_API_KEY_HERE")
```

Keep your API key **private**. Never push it to public repositories.

## ⚠️ Disclaimer

- This is a **beginner-level project** intended for learning.
- Works only on **Windows OS** (due to hardcoded app paths).
- Make sure your system has **audio drivers** and **Python 3.8+** installed.

## 💡 To Improve

- Add GUI using `Tkinter` or `PyQt`
- Support for Linux/macOS
- Use `dotenv` to securely store API keys
- Add fallback to GPT-3.5 / Llama as AI backend
- Better NLP for complex commands

## 🧑‍💻 Author

**Tanmoy Patra**  
*Final Year Student, Passionate about AI and Voice Technology*

## 📜 License

This project is licensed under the MIT License.