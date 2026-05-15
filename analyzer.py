import re

print("🔍 Booting up Sentinel Phase 4: Forensic Hash Identifier...")

def identify_hash(hash_string):
    """
    Analyzes a hash string's length and character patterns to determine its algorithm.
    """
    # Strip any accidental whitespace from the user input
    hash_string = hash_string.strip()
    length = len(hash_string)
    
    # Check if the string contains ONLY valid hexadecimal characters (0-9, a-f)
    is_hex = bool(re.match(r"^[a-fA-F0-9]+$", hash_string))
    
    possible_algorithms = []
    vulnerability_level = "Unknown"

    # --- FORENSIC RULE ENGINE ---
    
    # 1. Bcrypt (Modern, highly secure)
    if hash_string.startswith(("$2a$", "$2b$", "$2y$")) and length == 60:
        possible_algorithms.append("Bcrypt")
        vulnerability_level = "LOW (Highly Secure - Salted & Key Stretched)"
        
    # 2. MD5 (Very old, easily cracked)
    elif length == 32 and is_hex:
        possible_algorithms.append("MD5")
        possible_algorithms.append("NTLM (Windows Password)")
        vulnerability_level = "CRITICAL (Obsolete - Highly vulnerable to collision/rainbow tables)"
        
    # 3. SHA-1 (Older, mostly deprecated)
    elif length == 40 and is_hex:
        possible_algorithms.append("SHA-1")
        vulnerability_level = "HIGH (Deprecated - Vulnerable to collision attacks)"
        
    # 4. SHA-256 (Modern standard)
    elif length == 64 and is_hex:
        possible_algorithms.append("SHA-256")
        vulnerability_level = "LOW (Currently safe standard)"
        
    # 5. SHA-512 (Very secure)
    elif length == 128 and is_hex:
        possible_algorithms.append("SHA-512")
        vulnerability_level = "VERY LOW (Military-grade hashing)"

    # --- PREPARE THE REPORT ---
    if not possible_algorithms:
        return {
            "hash": hash_string,
            "status": "Unknown Format",
            "length": length,
            "algorithms": ["Unrecognized or Custom Hash"],
            "vulnerability": "N/A"
        }

    return {
        "hash": hash_string,
        "status": "Identified",
        "length": length,
        "is_hexadecimal": is_hex,
        "algorithms": possible_algorithms,
        "vulnerability": vulnerability_level
    }

if __name__ == "__main__":
    print("\n" + "="*50)
    print("🛡️ Sentinel Forensic Hash Analyzer")
    print("="*50)
    
    while True:
        test_hash = input("\nPaste a hash string (or type 'exit' to quit): ")
        if test_hash.lower() == 'exit':
            break
            
        report = identify_hash(test_hash)
        
        print("\n📊 --- FORENSIC REPORT ---")
        print(f"Status    : {report['status']}")
        print(f"Length    : {report['length']} characters")
        if report['status'] == "Identified":
            print(f"Matches   : {', '.join(report['algorithms'])}")
            print(f"Risk Level: {report['vulnerability']}")