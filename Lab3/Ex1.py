from cryptography.fernet import Fernet

key = Fernet.generate_key()
cipher_suite = Fernet(key)

# Basic version of the code that allows for encoding a message
encoded_text = cipher_suite.encrypt(b"This is a really secret message")
print(f"Encoded text: {encoded_text}")

# Better version of the code that allows for encoding and decoding a message
message = "This is a really secret message"
encoded_text = cipher_suite.encrypt(message.encode("utf-8"))
print(f"Encoded text: {encoded_text}")

# Use the cryptography library to encode and decode a message
decoded_text = cipher_suite.decrypt(encoded_text)
print(f"Decoded text: {decoded_text.decode('utf-8')}")
