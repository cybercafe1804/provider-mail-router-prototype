def get_smtp_provider(email):
    domain = email.split("@")[1].lower()

    providers = {
        "gmail.com": {
            "provider": "Gmail",
            "host": "smtp.gmail.com",
            "port": 587
        },
        "outlook.com": {
            "provider": "Outlook",
            "host": "smtp-mail.outlook.com",
            "port": 587
        },
        "hotmail.com": {
            "provider": "Hotmail",
            "host": "smtp-mail.outlook.com",
            "port": 587
        },
        "yahoo.com": {
            "provider": "Yahoo",
            "host": "smtp.mail.yahoo.com",
            "port": 587
        }
    }

    return providers.get(domain, {
        "provider": "Unknown",
        "host": "unknown",
        "port": "unknown"
    })
