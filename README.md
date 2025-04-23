# Python Directory Encryptor 🔐

A simple yet effective Python program designed to protect your sensitive files by encrypting and decrypting the contents of a specified directory.

---

## 📌 Overview

The **Python Directory Encryptor** is a user-friendly tool that allows you to securely encrypt and decrypt files within a specified folder. It generates a unique encryption key, providing robust security for your personal or professional data.

---

## 🎯 Purpose & Applications

This tool is particularly useful for:

- **Securing confidential documents**: Protect your financial records, personal documents, and other sensitive information from unauthorized access.
- **Safe file sharing**: Encrypt files before sharing over insecure channels such as emails or cloud storage.
- **Preventing unauthorized access**: Ideal for workplaces, educational institutions, or personal computers to ensure only intended users can access sensitive files.

---

## ⚙️ Features

- **Easy-to-use interface**: Simple command-line prompts guide you through the encryption and decryption processes.
- **Key management**: Automatically generates and manages encryption keys securely.
- **Recursive encryption/decryption**: Automatically applies encryption or decryption to all files and subfolders within the specified directory.

---

## 🚀 Quick Start Guide

### Step 1: Generate Encryption Key

```bash
python encryptor.py
```
- Choose option `1` to generate your encryption key.  

### Step 2: Encrypt Directory

- Run the script again and select option `2` to encrypt your files.

### Step 3: Decrypt Directory

- To decrypt, run the script and select option `3`.  

**Note:** Keep your generated `encryption.key` file safe, as it is required to decrypt your files later.

---

## ✅ Requirements

- Python 3.6 or newer
- `cryptography` library (install via `python -m pip install cryptography`)

---

## ⚠️ Caution

**Important**: If you lose your `encryption.key`, the encrypted data will become permanently inaccessible. Store your key securely and consider making secure backups.

---

## 📃 License

This project is open-source. Feel free to modify and use according to your needs.

---

Happy encrypting! 🔒
