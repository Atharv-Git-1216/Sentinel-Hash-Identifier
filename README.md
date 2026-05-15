# 🔏 Sentinel Phase 4: Forensic Hash Identifier

[![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Framework-Flask-lightgrey.svg)](https://flask.palletsprojects.com/)
[![Security](https://img.shields.io/badge/Security-Cryptography-red.svg)]()

## 🌌 The Sentinel Series (Phase 4)
This project is the **fourth module** of the **Sentinel Cyber AI** architecture. Moving beyond network scanning, Phase 4 brings Sentinel into the realm of **Digital Forensics and Cryptography**.

1. ✅ Password Strength & Security Logic 
2. ✅ Suspicious URL Detector (Machine Learning)
3. ✅ Phishing Email Analyzer (NLP/Zero-Shot)
4. 👉 **Forensic Hash Identifier** (Current)

---

## 📝 Project Overview
When databases are breached, passwords are rarely stored in plain text; they are stored as cryptographic hashes. This microservice acts as an automated forensic detective. It uses a custom Regular Expression (Regex) rule engine to analyze the mathematical "fingerprint" of an unknown hash and determine the algorithm used to create it.

### 🛡️ Core Features
* **Regex Rule Engine:** Built entirely from scratch without relying on external libraries to ensure high-speed, offline capability.
* **Algorithm Detection:** Accurately identifies Bcrypt, SHA-512, SHA-256, SHA-1, and MD5 hashes based on character length and structural prefixes.
* **Vulnerability Scoring:** Automatically flags obsolete hashes (like MD5 or SHA-1) that are vulnerable to collision attacks and rainbow tables.
* **RESTful Microservice:** Wrapped in a Flask API running on Port 5002, allowing seamless integration with the rest of the Sentinel architecture.

---

## 🚀 Getting Started

### Installation
1. **Clone the repository:**
   ```bash
   git clone [https://github.com/YOUR_USERNAME/sentinel-hash-identifier.git](https://github.com/YOUR_USERNAME/sentinel-hash-identifier.git)
   cd sentinel-hash-identifier