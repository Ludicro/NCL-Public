import base64
import json

# Example Base64-encoded payload (replace with your own)
encoded_payload = "eyJ1c2VybmFtZSI6InRlc3QyIiwic2lnbmF0dXJlIjoienE5ZVFJN3IzSDIvRWdhcDU4RmloaUFKUVhlWndrUVp4aVBjeWJtUG1oNDJHU2l6em8zVDNjUHUwZ0loYkxyZGdSdkVSMXQzeVlUUWFDTmNNREM2L0lMUHZBYUZDenFWcndSMkNab210clJaTGRLQVg1U0c2SzRzVUNraUJyTUZMWm0wMjZWYnozdGdueU9Zbmp3M0FVb0FaUTEwOThnSWZSeDV3dXRIYlZJPSJ9"

# Decode and modify the payload
def modify_payload(encoded_payload):
    try:
        # Decode the Base64 string
        decoded_bytes = base64.urlsafe_b64decode(encoded_payload + "==")  # Add padding if needed
        decoded_string = decoded_bytes.decode('utf-8')

        # Convert to JSON
        payload_data = json.loads(decoded_string)
        print("Original Payload:\n", payload_data)

        # Modify the username
        payload_data['username'] = 'charles'

        # Re-encode the modified payload
        modified_payload = base64.urlsafe_b64encode(json.dumps(payload_data).encode()).decode().rstrip("=")
        print("Modified Payload:\n", modified_payload)

        return modified_payload
    except Exception as e:
        return f"Error: {e}"

# Execute the function
modified_payload = modify_payload(encoded_payload)
print("Modified Payload:\n", modified_payload)
