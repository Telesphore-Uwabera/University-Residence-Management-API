# anonymization.py

def anonymize_data(email: str) -> str:
    name, domain = email.split('@')
    return f'{name[:2]}***@{domain}'
