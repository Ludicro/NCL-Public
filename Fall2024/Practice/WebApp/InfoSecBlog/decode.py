import base64
import json
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes

# Example Base64-encoded payload (replace with your own)
encoded_payload = "eyJ1c2VybmFtZSI6ImNoYXJsZXMiLCJzaWduYXR1cmUiOiJwUkZCazNJalp0clY3MDN4Skg3d2J0RUpLME4vK0UyOWlucHVGUndjcVFsWGpGZVBIUTBMQ3NNS1Nkd2RjQjYrbjFQc3UzNTdaeC9CTGhlbXNqR2h6aVE2OGpiNVgyN29PaUZZR0lDU1ZyM1VzNXZkdUw0Ym9MVms5ZWRBaTFCdE82VUZvbW9XY0xMODlqcjFjbFMyWkVEMjFIVWRUZkl1cGUrcWdGL0g4Vzg9In0="

# Decode the payload
decoded_bytes = base64.urlsafe_b64decode(encoded_payload + "==")  # Add padding if needed
decoded_string = decoded_bytes.decode('utf-8')

# Convert to JSON
payload_data = json.loads(decoded_string)
print("Payload:\n", payload_data)

# Extract the username and signature
username = payload_data.get('username')
signature_b64 = payload_data.get('signature')  # The Base64 encoded signature

# Load the RSA public key
public_key_pem = b"""
-----BEGIN PUBLIC KEY-----
MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQDku/9mnwqcgB5IMQtKLoiGJqD2
THVhFK2MBqiHjZ8wVum50vXye9yFmwBNCgdpMEFGxc+4Ajsv9ueQvhiR7e0qYO1c
UdMoGMFkCvuYvGoSlbLIgQnFq8FbZv7oteW8ITmYhkqikJ9qqC9jVErIGhB8cTlx
5wpRm7V0AP/C1QksxQIDAQAB
-----END PUBLIC KEY-----
"""

# Decode the Base64 signature
signature = base64.b64decode(signature_b64)

# Use the username as the message to verify
message = username.encode('utf-8')

# Load the public key
public_key = serialization.load_pem_public_key(public_key_pem, backend=default_backend())

# # Verify the signature
try:
    public_key.verify(
        signature,
        message,
        padding.PKCS1v15(),
        hashes.SHA256()
    )
    print("Signature is valid.")
except Exception as e:
    print("Signature verification failed:", str(e))

# # If you want to print the username without the byte string prefix:
print("Username used for verification:", username)
