# 📈 API Documentation: Trade Opportunities API

A FastAPI-based service that fetches current news about key Indian sectors, analyzes them using Gemini Pro (LLM), and returns a structured Markdown report with trade opportunities.

---

## Swagger Docs

For a more comprehensive and detailed version of the API documentation, please visit http://localhost:8000/docs. (Ensure the port number matches the one currently in use on your local environment.)

## Base URL

```bash


(Or `http://localhost:8000` for local)

---

## 🔐 Authentication

### 🔑 Login

**POST** `/login`

> Use this to obtain a JWT token.

#### Request Body

```json
{
  "username": "dummyusername",
  "password": "dummypassword"
}


```

```bash

{
  "access_token": "<JWT_TOKEN>",
  "token_type": "bearer"
}


```

---

## 🔐 Using the Token
Include the token in the Authorization header:

```bash
Authorization: Bearer <JWT_TOKEN>

```



## 🛠️ Analyze Sector

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

---