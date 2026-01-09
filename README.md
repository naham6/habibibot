# Habibi Voice Assistant
![Python](https://img.shields.io/badge/Python-3.8%2B-blue?style=for-the-badge&logo=python&logoColor=white)
![Status](https://img.shields.io/badge/Status-Active-success?style=for-the-badge)

**Habibi** is a Python-based virtual desktop assistant designed to automate daily tasks using voice commands. It listens for the wake word "Habibi" and can perform actions like playing music, searching the web, telling jokes, and fetching real-time information.

## ⚡ Features

* **Voice Activation:** continuously listens for the wake word "Habibi".
* **Media Automation:** Plays songs directly on YouTube (`pywhatkit`).
* **Web Navigation:** Opens Facebook, YouTube, and performs Google searches.
* **Knowledge Retrieval:** Fetches summaries from Wikipedia instantly.
* **Entertainment:** Tells jokes (`pyjokes`) and recites poetry.
* **Personality:** Responds with a unique personality and localized humor.

## 🛠️ Prerequisites

Before running the project, ensure you have **Python** installed. You may also need to install `PyAudio` dependencies if you are on Linux:

* **Windows:** Usually installs automatically.
* **Linux (Ubuntu/Debian):** Run `sudo apt-get install python3-pyaudio` first.

## 📦 Installation

1.  **Clone the repository**
    ```bash
    git clone [https://github.com/YOUR_USERNAME/habibi-voice-assistant.git](https://github.com/YOUR_USERNAME/habibi-voice-assistant.git)
    cd habibi-voice-assistant
    ```

2.  **Install dependencies**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Run the Assistant**
    ```bash
    python main.py
    ```

## 🗣️ Usage / Example Commands

Run the script and wait for the "Listening..." prompt. Then say **"Habibi"** followed by a command:

* *"Habibi, play Believer by Imagine Dragons"*
* *"Habibi, tell me about John Cena"*
* *"Habibi, what time is it?"*
* *"Habibi, tell me a joke"*
* *"Habibi, open Facebook"*
* *"Habibi, who are you?"*

## 📂 Project Structure

```text
├── main.py            # Core script containing the assistant logic
├── requirements.txt   # List of Python libraries required
└── README.md          # Documentation
