from flask import Flask, jsonify
import requests
import urllib3

urllib3.disable_warnings()

app = Flask(__name__)

@app.route("/api/ticketmaster", methods=["GET"])
def proxy():
    try:
        r = requests.get(
            "https://www.ticketmaster.co.il/wbtxapi/api/v1/bxcached/event/getAllTopEvent/iw",
            verify=False,
            timeout=10
        )
        return jsonify(r.json())
    except Exception as e:
        return jsonify({"error": str(e)}), 500
