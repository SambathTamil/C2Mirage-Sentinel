from flask import Flask, render_template
from database.alert_store import get_alerts

app = Flask(__name__)

@app.route("/")
def dashboard():

    alerts = get_alerts()

    total = len(alerts)
    high = len([a for a in alerts if a["severity"] == "High"])
    medium = len([a for a in alerts if a["severity"] == "Medium"])
    low = len([a for a in alerts if a["severity"] == "Low"])

    return render_template(
        "dashboard.html",
        alerts=alerts,
        total=total,
        high=high,
        medium=medium,
        low=low
    )

if __name__ == "__main__":
    app.run(port=5000)