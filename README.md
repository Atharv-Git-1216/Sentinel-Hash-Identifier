# 🔏 Sentinel Phase 4: Forensic Hash Identifier & Offline Cracking Engine

[![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Framework-Flask-lightgrey.svg)](https://flask.palletsprojects.com/)
[![Security](https://img.shields.io/badge/Security-Cryptography-red.svg)]()

## 🌌 The Sentinel Series (Phase 4)
This project is the **fourth module** of the **Sentinel Cyber AI** architecture. Moving beyond network scanning, Phase 4 brings Sentinel into the realm of **Digital Forensics and Cryptography**.

1. ✅ Password Strength & Security Logic 
2. ✅ Suspicious URL Detector (Machine Learning)
3. ✅ Phishing Email Analyzer (NLP/Zero-Shot)
4. 👉 **Forensic Hash Identifier & Cracking Engine** (Current)

---

## 📝 Project Overview
When databases are breached, passwords are rarely stored in plain text; they are stored as cryptographic hashes. This microservice acts as an automated forensic detective. 

It uses a custom Regular Expression (Regex) rule engine to analyze the mathematical "fingerprint" of an unknown hash, determines the algorithm used to create it, and then executes a **local offline dictionary attack** using the infamous `rockyou.txt` database to crack the hash back into plain text.

### 🛡️ Core Features
* **Regex Rule Engine:** Built entirely from scratch to accurately identify Bcrypt, SHA-512, SHA-256, SHA-1, and MD5 hashes based on character length and structural prefixes.
* **Offline Dictionary Cracking:** Bypasses third-party Threat Intel APIs by utilizing Python's `hashlib` to hash and compare up to 14.3 million words locally.
* **Vulnerability Scoring:** Automatically flags obsolete hashes (like MD5 or SHA-1) that are vulnerable to collision attacks and rainbow tables.
* **RESTful Microservice:** Wrapped in a Flask API running on Port 5002.

---

## 🚀 Getting Started

### Installation
1. **Clone the repository:**
   ```bash
   git clone [https://github.com/YOUR_USERNAME/sentinel-hash-identifier.git](https://github.com/YOUR_USERNAME/sentinel-hash-identifier.git)
   cd sentinel-hash-identifier