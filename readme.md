# YouTube Audio Transcriber and Sentiment Analyzer

This is a Python application that transcribes audio from YouTube videos and performs sentiment analysis on the text using the AssemblyAI API.

The project is structured into modular components for clarity and reusability, following best practices for a clean codebase.

## 🚀 Features

- Extracts Audio: Downloads the audio stream from any public YouTube video.
- Transcribes Audio: Converts the audio into written text using the AssemblyAI API.
- Analyzes Sentiment: Identifies the sentiment (positive, neutral, negative) of the transcribed text.
- Modular Design: Separates logic for YouTube, AssemblyAI, and the main application workflow into different files.
- Secure API Key Handling: Uses environment variables to keep your API key secure.

## 🛠️ Requirements

to run this project, you need the following:
- Python 3.6+
- A free AssemblyAI API key. You can get one from the AssemblyAI website.

## 📦 Installation

1.  Clone the repository:
    ```bash
    git clone [https://github.com/your-username/your-repo-name.git](https://github.com/your-username/your-repo-name.git)
    ```
2.  Navigate to the project directory:
    ```bash
    cd your-repo-name
    ```
3.  Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## ▶️ Usage

To run the application, execute the main.py file from your terminal:

```bash
python main.py
```
## 📂 File Structure
```bash
.
├── .env                  # Your secret API key
├── main.py               # Main application entry point
├── requirements.txt      # List of dependencies
├── transcriber.py        # Functions for interacting with the AssemblyAI API
└── youtube_downloader.py # Functions for handling YouTube audio downloads
```
