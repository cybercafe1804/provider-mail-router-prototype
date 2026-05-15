from dotenv import load_dotenv
import os

load_dotenv()

GMAIL_USER = os.getenv("GMAIL_USER")
GMAIL_APP_PASSWORD = os.getenv("GMAIL_APP_PASSWORD")
SMTP_MODE = os.getenv("SMTP_MODE", "test")

SMTP_PROVIDERS = {
    "gmail.com": {
        "provider": "Gmail",
        "host": "smtp.gmail.com",
        "port": 587
    },
    "outlook.com": {
        "provider": "Outlook/Hotmail",
        "host": "smtp-mail.outlook.com",
        "port": 587
    },
    "hotmail.com": {
        "provider": "Outlook/Hotmail",
        "host": "smtp-mail.outlook.com",
        "port": 587
    },
    "yahoo.com": {
        "provider": "Yahoo Mail",
        "host": "smtp.mail.yahoo.com",
        "port": 587
    },
    "att.net": {
        "provider": "AT&T",
        "host": "smtp.mail.att.net",
        "port": 465
    },
    "comcast.net": {
        "provider": "Comcast",
        "host": "smtp.comcast.net",
        "port": 587
    },
    "verizon.net": {
        "provider": "Verizon",
        "host": "smtp.verizon.net",
        "port": 465
    }
}
