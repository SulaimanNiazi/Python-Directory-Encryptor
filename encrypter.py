import os
from cryptography.fernet import Fernet

# Folder to encrypt/decrypt
FOLDER_PATH = "Dummy folder"

# Key file location
KEY_FILE = "encryption.key"

def generate_key():
    """
    Generate and save encryption key.
    """
    key = Fernet.generate_key()
    with open(KEY_FILE, "wb") as key_file:
        key_file.write(key)
    print("Encryption key generated and saved.")

def load_key():
    """
    Load the encryption key.
    """
    return open(KEY_FILE, "rb").read()

def encrypt_folder(path, key):
    """
    Encrypt files in the specified folder.
    """
    fernet = Fernet(key)

    for root, _, files in os.walk(path):
        for file in files:
            file_path = os.path.join(root, file)
            
            # Skip encryption of the key file itself
            if file == os.path.basename(KEY_FILE):
                continue

            with open(file_path, "rb") as f:
                data = f.read()

            encrypted = fernet.encrypt(data)

            with open(file_path, "wb") as f:
                f.write(encrypted)

            print(f"Encrypted: {file_path}")

def decrypt_folder(path, key):
    """
    Decrypt files in the specified folder.
    """
    fernet = Fernet(key)

    for root, _, files in os.walk(path):
        for file in files:
            file_path = os.path.join(root, file)
            
            # Skip decryption of the key file itself
            if file == os.path.basename(KEY_FILE):
                continue

            with open(file_path, "rb") as f:
                data = f.read()

            try:
                decrypted = fernet.decrypt(data)
                with open(file_path, "wb") as f:
                    f.write(decrypted)

                print(f"Decrypted: {file_path}")

            except Exception as e:
                print(f"Failed to decrypt {file_path}: {e}")

if __name__ == "__main__":
    print("\n--- Encryption/Decryption Demo ---")
    print("1. Generate encryption key")
    print("2. Encrypt folder")
    print("3. Decrypt folder")
    choice = input("Select an option (1/2/3): ")

    if choice == "1":
        generate_key()
    elif choice == "2":
        if not os.path.exists(KEY_FILE):
            print("Key file not found. Generate it first.")
        else:
            encrypt_folder(FOLDER_PATH, load_key())
    elif choice == "3":
        if not os.path.exists(KEY_FILE):
            print("Key file not found. Generate it first.")
        else:
            decrypt_folder(FOLDER_PATH, load_key())
    else:
        print("Invalid choice!")
