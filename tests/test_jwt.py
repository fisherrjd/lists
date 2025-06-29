from auth.security import create_access_token, decode_access_token
from datetime import timedelta
import jwt

# Test data
data = {"sub": "testuser", "role": "tester"}

print("--- JWT Creation Test ---")
token = create_access_token(data, expires_delta=timedelta(minutes=1))
print("Token:", token)

print("\n--- JWT Decode Test ---")
payload = decode_access_token(token)
print("Payload:", payload)

print("\n--- JWT Invalid Token Test ---")
try:
    decode_access_token(token + "corrupted")
except Exception as e:
    print("Expected error:", e)
