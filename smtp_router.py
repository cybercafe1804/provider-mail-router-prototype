from config import SMTP_PROVIDERS
import os
from datetime import datetime


LOG_FOLDER = "logs"
LOG_FILE = os.path.join(LOG_FOLDER, "provider.log")


def detect_provider(email):
    domain = email.split("@")[-1].lower()

    if domain in SMTP_PROVIDERS:
        return SMTP_PROVIDERS[domain]

    return {
        "provider": "Unknown",
        "host": None,
        "port": None
    }


def write_provider_log(sender, recipient, provider_info):
    os.makedirs(LOG_FOLDER, exist_ok=True)

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    log_entry = (
        f"[{timestamp}] "
        f"FROM={sender} "
        f"TO={recipient} "
        f"PROVIDER={provider_info['provider']} "
        f"HOST={provider_info['host']} "
        f"PORT={provider_info['port']}\n"
    )

    with open(LOG_FILE, "a") as log_file:
        log_file.write(log_entry)


def route_email(sender, recipient, subject, body):
    provider_info = detect_provider(recipient)

    print("Provider routing decision:")
    print(f"From: {sender}")
    print(f"To: {recipient}")
    print(f"Provider: {provider_info['provider']}")
    print(f"SMTP Host: {provider_info['host']}")
    print(f"Port: {provider_info['port']}")

    write_provider_log(sender, recipient, provider_info)

    return provider_info
