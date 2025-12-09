import os
import time
from flask import Flask, jsonify
import redis

app = Flask(__name__)

# Koneksi ke Redis (nama host 'db' ini nanti diset di docker-compose)
r = redis.Redis(host='db', port=6379, decode_responses=True)

@app.route('/')
def home():
    try:
        r.ping()
        db_status = "Connected"
    except Exception:
        db_status = "Disconnected"

    return jsonify({
        "status": "Alive",
        "message": "Aplikasi Python berjalan normal",
        "database": db_status
    })

# --- FITUR PENTING: KILL SWITCH ---
@app.route('/kill')
def kill_process():
    # Tambahkan flush=True biar teksnya dipaksa keluar ke log
    print("!!! KILL SIGNAL DITERIMA !!!", flush=True) 
    print("Mematikan proses secara paksa...", flush=True)
    
    time.sleep(1) # Kasih napas 1 detik biar log sempet ke-print (Optional tapi bagus)
    os._exit(1)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)