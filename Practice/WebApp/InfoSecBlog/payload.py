import base64
import json
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes

# Include the private key directly in the code
PRIVATE_KEY_PEM = b"""-----BEGIN RSA PRIVATE KEY-----
MIICXQIBAAKBgQDku/9mnwqcgB5IMQtKLoiGJqD2THVhFK2MBqiHjZ8wVum50vXy
e9yFmwBNCgdpMEFGxc+4Ajsv9ueQvhiR7e0qYO1cUdMoGMFkCvuYvGoSlbLIgQnF
q8FbZv7oteW8ITmYhkqikJ9qqC9jVErIGhB8cTlx5wpRm7V0AP/C1QksxQIDAQAB
AoGANrRnvulmpktV8roYEyPR7xOqB339zLwfTZACGnlaizseJx03SUkqUqHhjotJ
fnTWB9EjfsS51xzcARgV1EDtKXO9+QPlJsmYj1mL9fVdMd+GoNIjZVR2+hJ7D+fY
SJy6Qddhfrz5rpCQ8YV1uWFIQwFjag0GerL/PUFjM3CRe7kCQQD4zvJJjjhdlkpX
XbFJY5LoOoN5azW5m/vQSoqpLdjst9Clam1FJ+dJ6+/Q3Lzp2AucKUmCcYWkutwb
4mNqE6G/AkEA61iDi9frmmH+6gQnx2G2pFkRgO+MhK2+S4XHrN/c2fn7Ej6LXGF4
rroO9lOzmHZN+9zqKGsRx5UIMF5ldvcKewJBAM816mp/20l1xOwFx4RLPSnSsXQJ
aXDvC0RpEBndaO+cFlPs0pvpo6HYsJzNeTd3ChQ//kx4psiOJonCfPD28JkCQDjA
s5g5jXtBPnO4ZM9T5PNk9y+clMo6C7WyoSAzK9L00XLo2jqA1tVr0MfeD2Uowk2G
TIFKsJLsgXkIindRw5kCQQCclbh/dpchNHO+uZaD2OijzwZHBM5BgJ0fy4O7IMw/
aNMiboJ3a09LUqvOIp3r5QQuohcQog/IzxF1Leu2VHxu
-----END RSA PRIVATE KEY-----"""

# Load the private key from PEM format
private_key = serialization.load_pem_private_key(
    PRIVATE_KEY_PEM,
    password=None,
    backend=default_backend()
)

# Sign the data (username only)
def sign_data(private_key, data):
    signature = private_key.sign(
        data,
        padding.PKCS1v15(),
        hashes.SHA256()
    )
    return signature

# Create the new payload
username = 'charles'  # Change to 'charles' if needed
payload = {'username': username, 'signature': ''}

# Sign only the username
username_encoded = username.encode('utf-8')
signature = sign_data(private_key, username_encoded)
signature_base64 = base64.b64encode(signature).decode('utf-8')

# Update the payload with the new signature
payload['signature'] = signature_base64

# Convert the final payload to base64
final_payload_base64 = base64.b64encode(json.dumps(payload, separators=(',', ':')).encode('utf-8')).decode('utf-8')

# Output the final session key only if it matches the original token
print("New session key:\n", final_payload_base64)

