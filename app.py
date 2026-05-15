from flask import Flask, request, jsonify
from analyzer import identify_hash

app = Flask(__name__)

@app.route('/api/analyze-hash', methods=['POST'])
def analyze_hash_endpoint():
    data = request.get_json()
    
    # Check if the user actually sent a hash
    if not data or 'hash' not in data:
        return jsonify({"error": "No hash provided in payload"}), 400
        
    hash_string = data['hash']
    
    # Send the hash to your forensic engine
    report = identify_hash(hash_string)
    
    return jsonify({
        "status": "success",
        "forensic_report": report
    }), 200

if __name__ == '__main__':
    print("👁️ Sentinel Forensic API is live on port 5002...")
    # Port 5002 ensures it doesn't collide with Phase 2 (5001)
    app.run(host='0.0.0.0', port=5002)