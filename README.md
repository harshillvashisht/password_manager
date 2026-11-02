# 🔐 Encrypted Command-Line Password Manager

A secure, command-line password manager built in Python as an academic cybersecurity project. It demonstrates modern cryptographic principles, secure key derivation, authenticated encryption, and safe file-handling practices.

---

## 📌 Project Overview

This project implements a local credential vault designed around two main security goals:
1. **Confidentiality & Integrity:** Credentials are encrypted locally using **AES-256-GCM** with key derivation handled by **Argon2id**.
2. **Data Safety:** Atomic write operations prevent data corruption or half-written states during saving.

> **Note:** Developed for academic demonstration and college presentation purposes.

---

## ✨ Key Features

- **Master Password Security:** Derives a 32-byte key using **Argon2id** (OWASP-recommended parameters).
- **Authenticated Encryption:** Uses **AES-256-GCM** to ensure both privacy and tamper-detection.
- **Atomic File Storage:** Prevents vault corruption during power loss or unexpected exits via atomic renames (`os.replace`) and `fsync`.
- **Password Generator:** Cryptographically secure generator using Python’s `secrets` module and a Fisher-Yates shuffle.
- **Safe Password Handling:** Master passwords are never passed as command-line flags (to prevent leaking into shell history/process lists) and use hidden terminal prompts (`getpass`).
- **Interactive UI:** Clean terminal presentation using `rich` tables and formatted panels.

---

## 🛠️ Requirements

- **Python 3.13+**
- Dependencies: `argon2-cffi`, `cryptography`, `rich`

---

## 🚀 Quick Start

### 1. Installation

Clone or extract the repository, navigate into the directory, and install dependencies:

```bash
pip install -r requirements.txt
```

### 2. Usage Examples

```bash
# Create a new vault
python -m password_manager init

# Add a credential
python -m password_manager add github

# Retrieve a credential
python -m password_manager get github

# List all stored entry names
python -m password_manager list

# Generate a strong 24-character password
python -m password_manager gen 24

# Rotate master password
python -m password_manager change-password
```

---

## 🛡️ Security Architecture

| Security Threat | Technical Solution |
| :--- | :--- |
| **Brute-Force Attacks** | **Argon2id** key derivation (64 MiB memory, 3 passes) makes automated guessing extremely slow (~0.5s per guess). |
| **Vault Tampering** | **AES-256-GCM** authentication tag validation ensures tampered files fail decryption gracefully. |
| **Race Conditions / Interruptions** | Atomic write pipeline (`tmp file` ➔ `fsync` ➔ `os.replace`) guarantees all-or-nothing file updates. |
| **Insecure Randomness** | Python `secrets` module used exclusively for random salts, nonces, and password generation. |
| **Process Inspection Leakage** | `getpass` prompts hide inputs from process viewers (`ps aux`) and shell history. |

---

## 📁 Repository Structure

```text
.
├── src/
│   └── password_manager/   # Main application source code
├── tests/                  # Pytest test suite
├── learn/                  # Educational modules on cryptography & architecture
└── requirements.txt        # Python package dependencies
```