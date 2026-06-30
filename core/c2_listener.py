from flask import Flask, request
from datetime import datetime
from core.yara_scanner import scan_file
from notifications.telegram_notifier import send_alert
from database.alert_store import add_alert

app = Flask(__name__)

@app.route("/")
def home():

    source_ip = request.remote_addr
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    print(f"[+] Connection detected from {source_ip} at {timestamp}")

    detected = scan_file("samples/test_malware.txt")

    if detected:

        rule = "Suspicious_Command"
        severity = "High"

        # Save alert for dashboard
        add_alert(source_ip, timestamp, rule, severity)

        alert = f"""
🚨 C2Mirage Sentinel Alert

Suspicious interaction detected

Source IP: {source_ip}
Time: {timestamp}
"""

        send_alert(alert)

    return "C2Mirage Sentinel Server Running"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)