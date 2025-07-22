# JEDI-AI

JEDI-AI is a Star Wars-themed generative assistant that responds in the style of Jedi characters using large language models. It combines language generation, speech synthesis, and optional Retrieval-Augmented Generation (RAG) to create character-driven AI interactions.

This project is built with Python, Flask, LangChain, and supports integration with models like Gemini and text-to-speech APIs like ElevenLabs.

---

## Project Overview

The assistant takes user input and processes it through a configured language model (like Gemini). If RAG is enabled, it pulls relevant content from a provided `.txt` file. The model's response is then optionally synthesized into speech using ElevenLabs and presented with a video backdrop simulating a Jedi character.

---

## Requirements

Python 3.10 or higher

### Install dependencies:

```bash
pip install -r requirements.txt


REQUIREMENTS :
flask
langchain
google-generativeai
openai
requests
python-dotenv
faiss-cpu
sentence-transformers
pyttsx3



DIRECTORY STRUCTURE:
├── app.py                  # Flask backend
├── templates/
│   └── index.html          # Frontend interface
├── static/
│   ├── video/              # Background video clips
│   └── audio/              # Synthesized speech output
├── gemini_handler.py       # Gemini API logic
├── elevenlabs_handler.py   # ElevenLabs voice synthesis logic
├── rag_handler.py          # Handles text-based RAG
├── data/
│   └── knowledge.txt       # Custom RAG content
├── .env                    # API keys
└── README.md


SETUP API KEYS IN :

GEMINI_API_KEY=your_gemini_key IN gemini_handler file
ELEVENLABS_API_KEY=your_elevenlabs_key  IN tts_handler file


SUMMARY OF WORKFLOW:
User Input
   ↓
[Optional] RAG from knowledge.txt
   ↓
Prompt sent to Gemini/OpenAI
   ↓
LLM generates Jedi-style response
   ↓
Response passed to ElevenLabs → output.mp3
   ↓
Frontend plays looping video + output.mp3


