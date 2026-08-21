"""OMEGA Platform - Backend API"""
from flask import Flask, jsonify, request
from flask_cors import CORS
import json
from datetime import datetime

app = Flask(__name__)
CORS(app)

IOC_DATA = {
    "total_ioc": 782207,
    "apt_groups": 13,
    "zero_days": 5,
    "blocked_ips": [
        "13.248.169.48", "76.223.54.146", "104.238.61.237",
        "45.56.162.192", "61.11.162.213", "124.185.144.63"
    ],
    "c2_domains": ["backup.malicious.net", "awsglobalaccelerator.com"],
}

@app.route('/api/status')
def status():
    return jsonify({
        "status": "ALIVE",
        "timestamp": datetime.now().isoformat(),
        "system": "OMEGA Platform v1.0",
        "dna": "KH-SYNC-VERIFIED",
    })

@app.route('/api/threats/summary')
def threats():
    return jsonify(IOC_DATA)

@app.route('/api/threats/c2')
def c2():
    return jsonify({
        "c2_ips": IOC_DATA["blocked_ips"],
        "domains": IOC_DATA["c2_domains"],
        "status": "BLOCKED"
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
