import json
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ALERT_FILE = os.path.join(BASE_DIR, "alerts.json")


def add_alert(ip, time, rule, severity):

    if not os.path.exists(ALERT_FILE):
        with open(ALERT_FILE, "w") as f:
            json.dump([], f)

    with open(ALERT_FILE, "r") as f:
        alerts = json.load(f)

    alert = {
        "ip": ip,
        "time": time,
        "rule": rule,
        "severity": severity
    }

    alerts.append(alert)

    with open(ALERT_FILE, "w") as f:
        json.dump(alerts, f, indent=4)


def get_alerts():

    if not os.path.exists(ALERT_FILE):
        return []

    with open(ALERT_FILE, "r") as f:
        alerts = json.load(f)

    return alerts