import hmac
import hashlib

# Sender Side
message = input("Enter the message: ")
secret_key = input("Enter the secret key: ")

# Generate MAC
mac = hmac.new(
    secret_key.encode(),
    message.encode(),
    hashlib.sha256
).hexdigest()

print("\nGenerated MAC:", mac)

# Receiver Side
print("\n--- Verification ---")
received_message = input("Enter received message: ")
received_key = input("Enter secret key: ")

new_mac = hmac.new(
    received_key.encode(),
    received_message.encode(),
    hashlib.sha256
).hexdigest()

print("Generated MAC at Receiver:", new_mac)

if hmac.compare_digest(mac, new_mac):
    print("MAC Verified: Message is Authentic and Unchanged.")
else:
    print("MAC Verification Failed: Message has been Modified or Key is Incorrect.")
