import re
import os
import hashlib

print("🔍 Booting up Sentinel Phase 4: Forensic Hash Identifier (v2.0)...")

def crack_hash_offline(target_hash, algorithm):
    """
    Performs a local dictionary attack using rockyou.txt.
    Hashes millions of words offline to find a mathematical match.
    """
    dictionary_file = "rockyou.txt"
    
    # 1. Check if the user actually downloaded the file
    if not os.path.exists(dictionary_file):
        return {
            "is_compromised": False,
            "cracked_plaintext": "N/A",
            "database_source": "⚠️ ERROR: rockyou.txt not found in folder. Please download it."
        }

    # We skip Bcrypt for dictionary attacks because it is intentionally too slow to brute-force easily
    if "Bcrypt" in algorithm:
        return {
            "is_compromised": False,
            "cracked_plaintext": "N/A",
            "database_source": "Bcrypt is highly resistant to standard dictionary attacks."
        }

    print(f"🗄️ Initiating offline dictionary attack using {dictionary_file}...")
    print("⏳ (Depending on password complexity, this may take a few seconds...)")

    try:
        # We use latin-1 encoding because rockyou.txt contains many weird characters
        with open(dictionary_file, 'r', encoding='latin-1') as file:
            for line in file:
                # Remove spaces and newlines from the word
                word = line.strip()
                
                # 2. Hash the dictionary word using the matching algorithm
                if "MD5" in algorithm:
                    hashed_word = hashlib.md5(word.encode('utf-8')).hexdigest()
                elif "SHA-1" in algorithm:
                    hashed_word = hashlib.sha1(word.encode('utf-8')).hexdigest()
                elif "SHA-256" in algorithm:
                    hashed_word = hashlib.sha256(word.encode('utf-8')).hexdigest()
                else:
                    break # Failsafe for unknown algorithms

                # 3. THE CRACK: Do the hashes match?
                if hashed_word == target_hash:
                    return {
                        "is_compromised": True,
                        "cracked_plaintext": word,
                        "database_source": "Local rockyou.txt Dictionary Attack"
                    }
                    
    except Exception as e:
        print(f"⚠️ Cracking Engine Error: {e}")

    # If the loop finishes all 14 million words and finds nothing
    return {
        "is_compromised": False,
        "cracked_plaintext": "N/A",
        "database_source": "Target hash not found in 14.3 million word dictionary."
    }

def identify_hash(hash_string):
    hash_string = hash_string.strip()
    length = len(hash_string)
    is_hex = bool(re.match(r"^[a-fA-F0-9]+$", hash_string))
    
    possible_algorithms = []
    vulnerability_level = "Unknown"

    # --- FORENSIC RULE ENGINE ---
    if hash_string.startswith(("$2a$", "$2b$", "$2y$")) and length == 60:
        possible_algorithms.append("Bcrypt")
        vulnerability_level = "LOW (Highly Secure)"
        
    elif length == 32 and is_hex:
        possible_algorithms.append("MD5")
        vulnerability_level = "CRITICAL (Obsolete)"
        
    elif length == 40 and is_hex:
        possible_algorithms.append("SHA-1")
        vulnerability_level = "HIGH (Deprecated)"
        
    elif length == 64 and is_hex:
        possible_algorithms.append("SHA-256")
        vulnerability_level = "LOW (Current standard)"
        
    elif length == 128 and is_hex:
        possible_algorithms.append("SHA-512")
        vulnerability_level = "VERY LOW (Military-grade)"

    if not possible_algorithms:
        return {
            "hash": hash_string,
            "status": "Unknown Format",
            "algorithms": ["Unrecognized"],
            "vulnerability": "N/A",
            "threat_intel": {"is_compromised": False}
        }

    # --- THREAT INTEL CHECK ---
    # We pass the first matched algorithm to the database checker
    threat_intel_report = crack_hash_offline(hash_string, possible_algorithms[0])

    return {
        "hash": hash_string,
        "status": "Identified",
        "length": length,
        "algorithms": possible_algorithms,
        "vulnerability": vulnerability_level,
        "threat_intel": threat_intel_report
    }

if __name__ == "__main__":
    print("\n" + "="*60)
    print("🛡️ Sentinel Forensic Hash Analyzer & Threat Intel")
    print("="*60)
    
    while True:
        test_hash = input("\nPaste a hash string (or type 'exit' to quit): ")
        if test_hash.lower() == 'exit':
            break
            
        report = identify_hash(test_hash)
        
        print("\n📊 --- FORENSIC REPORT ---")
        print(f"Status       : {report['status']}")
        if report['status'] == "Identified":
            print(f"Matches      : {', '.join(report['algorithms'])}")
            print(f"Risk Level   : {report['vulnerability']}")
            
            print("\n🚨 --- THREAT INTELLIGENCE ---")
            if report['threat_intel']['is_compromised']:
                print(f"WARNING      : HASH CRACKED!")
                print(f"Plain Text   : -> {report['threat_intel']['cracked_plaintext']} <-")
                print(f"Source       : {report['threat_intel']['database_source']}")
            else:
                print("Clear        : Hash not found in known Rainbow Tables.")