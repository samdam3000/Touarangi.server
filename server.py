
from flask import Flask, jsonify
from strike_queue import get_confirmed_strikes

app = Flask(__name__)

@app.route("/strikes/live", methods=["GET"])
def live_strikes():
    strikes = get_confirmed_strikes(within_minutes=5)
    return jsonify(strikes)

@app.route("/health", methods=["GET"])
def health_check():
    return jsonify({"status": "Touarangi server is running", "ok": True})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
