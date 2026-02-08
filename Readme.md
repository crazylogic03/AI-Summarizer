# 📄 AI Document Summarizer

A simple web-based document summarization service built with **Streamlit** and **Groq LLM API**.  
The application allows users to upload PDF files or paste text and generate summaries in different styles such as **Brief**, **Detailed**, or **Bullet Points**.

---

## Features

- Upload PDF documents or paste raw text
- Multiple summarization styles:
  - Brief
  - Detailed
  - Bullet Points
- Powered by Groq’s LLaMA 3.1 model
- Graceful error handling for API and file issues
- Basic input validation

---

## 🛠️ Tech Stack

- Python
- Streamlit – Web interface
- Groq API – LLM inference
- PyPDF2 – PDF text extraction

---

## 📁 Project Structure

```text
.
├── app.py
├── requirements.txt
├── .env
└── README.md



⚙️ Setup Instructions
1. Clone the Repository

git clone https://github.com/your-username/ai-document-summarizer.git
cd ai-document-summarizer


2. Create and Activate a Virtual Environment 

python -m venv venv
source venv/binactivate


3. Install Dependencies
pip install -r requirements.txt


4️. Set Up Environment Variables

Create a .env file in the root directory:
GROQ_API_KEY=your_groq_api_key_here

Get your API key from: https://console.groq.com/


▶️ Running the Application
streamlit run app.py