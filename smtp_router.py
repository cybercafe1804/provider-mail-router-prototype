import smtplib
from email.message import EmailMessage
from config import SMTP_PROVIDERS, GMAIL_USER, GMAIL_APP_PASSWORD, SMTP_MODE


def get_provider(email):
    domain = email.split("@")[-1].lower()
    return SMTP_PROVIDERS.get(domain, {
        "provider": "Unknown",
        "host": None,
        "port": None
    })


def route_email(sender, receiver):
    provider_info = get_provider(receiver)

    return {
        "from": sender,
        "to": receiver,
        "provider": provider_info["provider"],
        "host": provider_info["host"],
        "port": provider_info["port"]
    }


def send_email(sender, receiver, subject, body):
    routing = route_email(sender, receiver)

    if SMTP_MODE == "test":
        return f"""
TEST MODE - Email not actually sent.

Provider routing decision:
From: {sender}
To: {receiver}
Provider: {routing['provider']}
SMTP Host: {routing['host']}
Port: {routing['port']}
Subject: {subject}
Message: {body}
"""

    if not GMAIL_USER or not GMAIL_APP_PASSWORD:
        return "Error: Gmail credentials are missing in .env file."

    msg = EmailMessage()
    msg["From"] = GMAIL_USER
    msg["To"] = receiver
    msg["Subject"] = subject
    msg.set_content(body)

    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
            smtp.starttls()
            smtp.login(GMAIL_USER, GMAIL_APP_PASSWORD)
            smtp.send_message(msg)

        return f"Email sent successfully to {receiver}"

    except Exception as e:
        return f"SMTP send failed: {e}"
