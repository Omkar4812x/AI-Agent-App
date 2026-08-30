# 🤖 AI Agent App

> **Interactive AI Agent web application leveraging OpenRouter API multi-model completions (Mistral-7B, GPT, Llama) with Flask health monitoring and Markdown rendering.**

---

## ✨ Features

- 💬 **Multi-Model LLM Completions**
  - Connects to OpenRouter API allowing access to open-source models (Mistral-7B Instruct, Llama, Gemini, etc.).
- 🎨 **Modern Dark-Mode UI**
  - Responsive Bootstrap chat interface with Markdown parsing (`marked.js`).
- ⚡ **Flask Microservice Endpoint**
  - Python Flask backend service with automated health check endpoints (`/health`).

---

## 🛠️ Tech Stack

- **Frontend**: HTML5, JavaScript (ES6+), Bootstrap 5, `marked.js`
- **Backend**: Python 3, Flask, Requests
- **LLM Gateway**: OpenRouter API

---

## 🚀 Getting Started

1. **Clone the repository**:
   ```bash
   git clone https://github.com/Omkar4812x/AI-Agent-App.git
   cd AI-Agent-App
   ```

2. **Set your OpenRouter API Key**:
   Export your key in environment or set in `index2.html`:
   ```bash
   export OPENROUTER_API_KEY="your_api_key_here"
   ```

3. **Run Python Flask Service**:
   ```bash
   python app.py
   ```

4. **Launch Interface**:
   Open `index2.html` in your browser.

---

## 📄 License

Distributed under the MIT License.
