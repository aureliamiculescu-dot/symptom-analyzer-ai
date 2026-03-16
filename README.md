# 🩺 Symptom Analyzer AI

An AI-powered application that analyzes user symptoms and provides general health information using **Retrieval-Augmented Generation (RAG)**.

The application retrieves relevant medical information from a local knowledge base and uses the OpenAI API to generate informative responses.  
The user interface is built with Streamlit.

⚠️ **Disclaimer:** This application does not provide medical diagnosis and should not replace professional medical advice.

---

# 📌 Features

- Symptom analysis based on user input
- Retrieval of relevant medical documents (RAG)
- AI-generated health information
- Portuguese (PT-PT) responses
- Simple and lightweight architecture

---

# 🧠 How It Works

The system uses a **Retrieval-Augmented Generation (RAG)** architecture:

1. The user enters symptoms.
2. The application converts the input into embeddings.
3. A vector search retrieves the most relevant medical documents.
4. The retrieved context is sent to the OpenAI model.
5. The model generates an informative response.

Architecture flow:

```
User Symptoms
      ↓
Embedding Generation
      ↓
Vector Search (FAISS)
      ↓
Relevant Medical Documents
      ↓
OpenAI Model
      ↓
Generated Health Information
```

---

# 🏗 Project Structure

```
symptom-analyzer-ai
│
├── app.py
├── rag_simple.py
├── documentos_medicos
│   ├── gripe.txt
│   ├── pneumonia.txt
│   ├── diabetes_tipo2.txt
│   ├── hipertensao.txt
│   ├── ansiedade.txt
│   └── infeccao_urinaria.txt
│
├── requirements.txt
├── .env.example
└── README.md
```

---

# 🚀 Installation

Clone the repository:

```bash
git clone https://github.com/aureliamiculescu-dot/symptom-analyzer-ai.git
```

Go to the project directory:

```bash
cd symptom-analyzer-ai
```

---

# 🐍 Create a Virtual Environment

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### macOS / Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

---

# 📦 Install Dependencies

If a `requirements.txt` file exists:

```bash
pip install -r requirements.txt
```

If not, install manually:

```bash
pip install streamlit openai faiss-cpu numpy python-dotenv
```

---

# 🔑 Configure the OpenAI API Key

Create a file called:

```
.env
```

Add your API key:

```
OPENAI_API_KEY=your_api_key_here
```

---

# ▶️ Run the Application

Start the application:

```bash
streamlit run app.py
```

Then open your browser at:

```
http://localhost:8501
```

---

# 📚 Medical Knowledge Base

The system uses a local folder containing simple medical information files.

Example:

```
documentos_medicos
│
├── gripe.txt
├── pneumonia.txt
├── diabetes_tipo2.txt
├── hipertensao.txt
├── ansiedade.txt
└── infeccao_urinaria.txt
```

These documents are used as **context for the RAG system**.

---

# ⚠️ Disclaimer

This project is intended **for educational and research purposes only**.

The system:
- does **not provide medical diagnosis**
- should **not replace professional medical consultation**

Always consult a qualified healthcare professional for medical advice.

---

# 🛠 Technologies Used

- Python
- Streamlit
- OpenAI API
- FAISS
- NumPy

---

# 👩‍💻 Author

**Aurelia Miculescu**

GitHub:  
https://github.com/aureliamiculescu-dot

---

# 📄 License

This project is released for **educational purposes**.