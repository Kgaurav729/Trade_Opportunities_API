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
git clone https://github.com/Kgaurav729/Trade_Opportunities_API.git

```
---
### 2.Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 3. Set Environment Variables

```bash
export GEMINI_API_KEY=your_gemini_api_key_here
```
---

### 4.Running The App
```bash
uvicorn main:app --reload

```
---

## visit the swagger docs

http://localhost:8000/docs

----

### 5.Authentication

## Login to get the token

```bash

POST /login

Request:
{
  "username": "dummyusername",
  "password": "dummypassword"
}

Response:
{
  "access_token": "your_token_here",
  "token_type": "bearer"
}
```
 
## Use this token in all further requests:

```bash
Authorization: Bearer your_token_here
```


---

### 4. Analyze the sector

```bash
GET /analyze/{sector}
```

## Supported Sector

- pharmaceuticals
- technology
- agriculture

## Example

```bash
curl -H "Authorization: Bearer <token>" \
 http://localhost:8000/analyze/pharmaceuticals

```
---

### 5.Rate Limiting

-Max 5 requests per user per 60 seconds.
-Exceeding the limit returns HTTP 429.



