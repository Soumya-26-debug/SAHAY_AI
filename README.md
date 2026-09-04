# SahayAI

# A Unified AI-Powered Accessibility Assistant for Persons with Disabilities

SahayAI is an AI-powered accessibility assistant designed to provide
personalized assistance to Persons with Disabilities (PwDs) through a
unified platform.

The system combines Large Language Models (LLMs), Retrieval-Augmented
Generation (RAG), Computer Vision, Optical Character Recognition (OCR),
Speech-to-Text (STT), and Text-to-Speech (TTS) technologies to support
different accessibility requirements.

---

# Project Overview
Assistive technologies are often distributed across different applications
and services. Users may need separate tools for reading text, converting
speech to text, obtaining information, or accessing accessibility-related
resources.

SahayAI aims to bring these capabilities together into a single
AI-powered accessibility assistant.

The assistant is designed around three primary user groups:

- Blind / visually impaired users
- Deaf / hard-of-hearing users
- Non-speaking users

The system provides different interaction methods based on the user's
accessibility requirements.

---

## Objectives

The major objectives of SahayAI are:

- Provide a unified accessibility assistant.
- Support voice and text-based interaction.
- Convert speech into text using Speech-to-Text technology.
- Convert AI-generated responses into speech using Text-to-Speech.
- Extract text from images using OCR.
- Provide AI-powered responses using an LLM.
- Improve reliability using Retrieval-Augmented Generation.
- Provide information related to disability rights, government schemes,
  education, UDID services and assistive resources.
- Provide personalized responses according to the user's accessibility
  requirements.
- Create an accessible and simple user interface.

---

# Key Features

# 1. AI Assistant

SahayAI uses a Large Language Model to understand user queries and generate
natural-language responses.

Users can interact with the assistant through supported input methods such
as text and voice.

---

# 2. Retrieval-Augmented Generation (RAG)

The RAG module provides a knowledge-grounding layer for the AI assistant.

Relevant information is retrieved from a curated knowledge base before
generating the final response.

The knowledge base contains documents related to:

- Government schemes
- Disability rights
- Education and scholarships
- UDID
- Assistive resources
- Accessibility-related information

Basic RAG pipeline:


User Query
    ↓
Query Processing
    ↓
Embedding
    ↓
Vector Similarity Search
    ↓
Relevant Document Chunks
    ↓
LLM + Retrieved Context
    ↓
Grounded Response

Sahay-AI An AI-powered accessibility assistant for persons with disabilities, built using Flutter, Java (Android) and Python FastAPI. One accessibility companion that adapts itself to the user's disability, communicates in their preferred language and modality, and lets them operate the phone/application with minimal physical interaction.

Key Features: SOS Emergency: Instant alert with GPS location to 5 emergency contacts and police. Voice Navigation: Control the entire app using voice commands ("Sahay, open schemes"). Government Schemes (RAG): Ask any question about welfare schemes and get dynamic, up-to-date answers. Talk with Me: AI companion for conversation, mental well-being, and engagement. Sign Language Detection: Camera detects ASL signs and converts them to text/speech. Dyslexia Assistance: OCR + spell correction for reading images, PDFs, and documents. Health Reminder: Medicine scheduling with voice notifications. Accessible Notifications: Reads all phone notifications aloud automatically.

Technology Stack: | Frontend | Flutter (Dart) | | Background Services | Native Java (Android) | | Backend / API | Python FastAPI | | AI/ML | TensorFlow Lite, MediaPipe, Tesseract OCR, Vosk (STT) | | RAG Pipeline | LangChain, FAISS, Sentence-Transformers | | State Management | Provider | | Local Storage | SharedPreferences, SQLite |
