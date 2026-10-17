# Nihongo2Myanmar — Japanese to Myanmar translator (MVP)

This repository is a starter skeleton for Nihongo2Myanmar (Japanese→Myanmar translator & learning aid).

Goals
- Provide text, image (OCR), and voice input to translate Japanese to Myanmar
- Show readings, tokenization, JLPT/POS metadata where available
- Save translation history and vocabulary

Quick start (local, development)

1. Create a virtual environment and install dependencies

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

2. Copy .env.example to .env and edit as needed

3. Run the app

```bash
export FLASK_APP=run.py
flask run
```

The app uses SQLite by default (instance/app.db). NLP and translation services are stubbed — see app/services for implementation notes.

Configuration
- TRANSLATOR: "google" or "stub" (default "stub")
- GOOGLE_APPLICATION_CREDENTIALS: path to GCP credentials if you use Google Translate API

Next steps
- Implement concrete translator integration (Google/Azure or open models)
- Hook up MeCab/fugashi + jamdict for Japanese tokenization & dictionary lookup
- Add OCR (PaddleOCR/Tesseract) and voice input
- Implement history and saved words endpoints
