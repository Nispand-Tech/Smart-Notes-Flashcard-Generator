# 🗃️ Smart Notes Flashcard Generator

> Generate intelligent flashcards automatically from study notes using **Natural Language Processing (NLP)**.

![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-Web%20App-red?logo=streamlit)
![NLTK](https://img.shields.io/badge/NLTK-NLP-green)
![Scikit--learn](https://img.shields.io/badge/Scikit--learn-TF--IDF-orange)
![License](https://img.shields.io/badge/License-MIT-yellow)

---

# 📖 Project Overview

Smart Notes Flashcard Generator is an NLP-based web application that automatically converts study notes into intelligent flashcards.

Instead of manually preparing question-answer pairs, the application processes textual notes using Natural Language Processing techniques such as sentence tokenization, text cleaning, and TF-IDF keyword extraction to generate meaningful flashcards.

The application provides an easy-to-use Streamlit interface and supports exporting generated flashcards into multiple formats.

---

# ✨ Features

✅ Paste notes directly into the application

✅ Upload `.txt` files

✅ Sentence Tokenization

✅ Text Cleaning

✅ TF-IDF Keyword Extraction

✅ Automatic Flashcard Generation

✅ Interactive Streamlit Interface

✅ Expandable Flashcards

✅ Processing Statistics Dashboard

✅ TXT Export

✅ CSV Export

✅ PDF Export *(if enabled)*

---

# 🛠 Technologies Used

## Programming Language

- Python 3

## Frontend

- Streamlit

## NLP Libraries

- NLTK
- Scikit-learn

## PDF Generation

- ReportLab

## Data Handling

- CSV
- IO

---

# 🧠 NLP Pipeline

The application follows the following Natural Language Processing workflow:

```
Input Notes
      │
      ▼
Sentence Tokenization
      │
      ▼
Text Cleaning
      │
      ▼
TF-IDF Keyword Extraction
      │
      ▼
Flashcard Generation
      │
      ▼
Display Results
      │
      ▼
Export (TXT / CSV / PDF)
```

---

# 📂 Project Structure

```
Smart-Notes-Flashcard-Generator/

│
├── app.py
│
├── requirements.txt
│
├── README.md
│
├── src/
│   ├── file_handler.py
│   ├── text_cleaner.py
│   ├── tfidf_keywords.py
│   └── flashcard_generator.py
│
├── data/
│   └── sample_notes.txt
│
└── screenshots/
```

---

# ⚙️ Installation

## Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/Smart-Notes-Flashcard-Generator.git
```

---

## Move into Project

```bash
cd Smart-Notes-Flashcard-Generator
```

---

## Create Virtual Environment

Windows

```bash
python -m venv venv
```

Activate

```bash
venv\Scripts\activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Run Application

```bash
streamlit run app.py
```

---

# 💻 Application Workflow

### Step 1

Paste your notes

**OR**

Upload a `.txt` file.

↓

### Step 2

Click

```
Generate Flashcards
```

↓

### Step 3

The application performs

- Sentence Tokenization
- Text Cleaning
- TF-IDF Keyword Extraction

↓

### Step 4

Flashcards are generated automatically.

↓

### Step 5

Download as

- TXT
- CSV
- PDF

---

# 📊 Processing Summary

The application displays

- Number of Sentences
- Number of Flashcards
- Total Keywords

---

# 📥 Export Formats

| Format | Supported |
|---------|-----------|
| TXT | ✅ |
| CSV | ✅ |
| PDF | ✅ |

---

# 📸 Screenshots

## Home Page

```
Add screenshot here
```

Example:

```
screenshots/home.png
```

---

## Generated Flashcards

```
Add screenshot here
```

Example:

```
screenshots/flashcards.png
```

---

## Download Section

```
Add screenshot here
```

Example:

```
screenshots/download.png
```

---

# 🔍 Example

## Input

```
Python is a high-level programming language.

It is widely used in Artificial Intelligence.

Python supports object-oriented programming.
```

---

## Output

### Flashcard 1

**Question**

What is Python?

**Answer**

Python is a high-level programming language.

**Keywords**

Python, programming, language

---

# 🚀 Future Improvements

- Support PDF uploads
- Automatic Question Generation using LLMs
- Speech-to-Text Notes
- Voice-based Flashcards
- Image OCR Support
- Flashcard Difficulty Levels
- Dark Mode
- Cloud Storage Integration
- Quiz Mode
- Mobile Responsive UI

---

# 🎯 Learning Outcomes

Through this project, the following concepts were implemented:

- Python Programming
- Streamlit
- NLP Fundamentals
- Sentence Tokenization
- Text Cleaning
- TF-IDF
- Modular Programming
- File Handling
- CSV Handling
- PDF Generation
- Interactive Web Applications

---

# 👨‍💻 Author

**Nispand**

Computer Science Engineering Student

Built with ❤️ using Python & Streamlit

GitHub:

```
https://github.com/Nispand-Tech
```

---

# ⭐ If you like this project

Please consider giving the repository a ⭐ on GitHub.

---

# 📜 License

This project is intended for educational and learning purposes.

MIT License.
