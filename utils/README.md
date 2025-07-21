# 📈 Trade Opportunities API (India Sector Insights)

A FastAPI-based service that fetches current news about key Indian sectors, analyzes them using Gemini Pro (LLM), and returns a structured Markdown report with trade opportunities.

---

## 🚀 Features

- 🔐 JWT-based login and token authentication
- 🚦 Per-user rate limiting (e.g., 5 requests/min)
- 🌐 Real-time market data via DuckDuckGo search API
- 🤖 Google Gemini LLM integration for sector analysis
- 📄 Clean, structured Markdown reports
- 📦 In-memory storage only — no database required

---

## 🛠️ Tech Stack

- FastAPI (Python 3.9+)
- JWT Authentication (`python-jose`)
- DuckDuckGo Search (`duckduckgo-search`)
- Google Gemini API (`google-generativeai`)
- Uvicorn (ASGI server)

---

## 🧑‍💻 Setup Instructions

### 1. 📂 Clone the Repo

```bash
git clone https://github.com/yourusername/trade-opportunities-api.git
cd trade-opportunities-api
