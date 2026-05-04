from config import SMTP_PROVIDERS


def detect_provider(email):
    domain = email.split("@")[-1].lower()

    if domain in SMTP_PROVIDERS:
        return SMTP_PROVIDERS[domain]

    return {
        "provider": "Unknown",
        "host": None,
        "port": None
    }


def route_email(sender, recipient, subject, body):
    provider_info = detect_provider(recipient)

    print("Provider routing decision:")
    print(f"From: {sender}")
    print(f"To: {recipient}")
    print(f"Provider: {provider_info['provider']}")
    print(f"SMTP Host: {provider_info['host']}")
    print(f"Port: {provider_info['port']}")

    return provider_info
