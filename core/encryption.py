# encryption.py

from cryptography.fernet import Fernet
from django.conf import settings

# Uses the encryption key from the settings
cipher_suite = Fernet(settings.FIELD_ENCRYPTION_KEY)

# Encrypt data
def encrypt_data(data: str) -> str:
    return cipher_suite.encrypt(data.encode()).decode()

# Decrypt data
def decrypt_data(encrypted_data: str) -> str:
    return cipher_suite.decrypt(encrypted_data.encode()).decode()
