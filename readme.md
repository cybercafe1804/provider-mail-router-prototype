# Provider-Aware Mail Server (Python)

A simple client-server mail system built in Python, upgraded with provider-aware routing and logging.

---

## 🚀 Features

- Send messages between users
- Store messages locally in inbox folders
- List and read messages
- Detect email providers (Gmail, Yahoo, Outlook, etc.)
- Route emails based on provider domain
- Log provider routing decisions

---

## 🧠 Provider-Aware Routing

The system detects the recipient's email domain and maps it to its SMTP provider.

### Supported Providers

- Gmail → smtp.gmail.com
- Outlook/Hotmail → smtp-mail.outlook.com
- Yahoo Mail → smtp.mail.yahoo.com
- AT&T → smtp.mail.att.net (port 465)
- Comcast → smtp.comcast.net
- Verizon → smtp.verizon.net (port 465)

Routing logic is handled in:

---

## 📝 Logging

All provider routing decisions are saved in:

Example log:
[2026-05-03 18:17:15] FROM=user1@gmail.com
 TO=user2@yahoo.com
 PROVIDER=Yahoo Mail HOST=smtp.mail.yahoo.com PORT=587



---

## ⚙️ How to Run

### Start server (Terminal 1)

```bash
python3 server.py
