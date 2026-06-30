# 🛡️ C2Mirage-Sentinel

A deception-based Command & Control (C2) detection framework built with Flask and YARA to help detect suspicious files, monitor activity, and send real-time Telegram alerts.

---

## 📚 Table of Contents

- About
- Features
- Technologies Used
- Installation
- Usage
- Project Structure
- Future Improvements
- License

---

## ℹ️ About

C2Mirage-Sentinel is a cybersecurity project that explores how Command & Control (C2) attacks can be detected using deception techniques and YARA-based malware scanning.

The project provides a simple web interface where users can upload files, scan them against YARA rules, and receive Telegram alerts whenever suspicious activity is detected. Detection history is stored locally using SQLite, making it easy to review previous scans.

This project was built as part of my cybersecurity learning journey and helped me gain practical experience with malware detection, Flask development, and security automation.

---

## ✨ Features

- 🛡️ Scan files using YARA rules
- 📁 Upload files through a web interface
- 🚨 Real-time Telegram notifications
- 📊 View previous scan history
- 💾 SQLite database integration
- 🌐 Simple Flask dashboard
- 🔍 Lightweight and easy to understand

---

## 🛠️ Technologies Used

- Python
- Flask
- YARA
- SQLite
- HTML
- CSS
- JavaScript
- Telegram Bot API

---

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/SambathTamil/C2Mirage-Sentinel.git
cd C2Mirage-Sentinel
```

Install the required packages:

```bash
pip install -r requirements.txt
```

If you want Telegram alerts, create a `.env` file and add your bot credentials.

Start the application:

```bash
python app.py
```

---

## 🚀 Usage

Open your browser and visit:

```
http://127.0.0.1:5000
```

From the dashboard you can:

- Upload files for scanning
- Detect malware using YARA rules
- View previous scan history
- Receive Telegram alerts
- Review detection results

---

## 📂 Project Structure

```
C2Mirage-Sentinel/
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
├── templates/
├── static/
├── uploads/
├── yara_rules/
└── database/
```

---

## 🚧 Future Improvements

- AI-assisted threat detection
- Elasticsearch integration
- Kibana dashboard
- Multi-user authentication
- Email notifications
- MITRE ATT&CK mapping

---

## 🤝 Contributing

Contributions, suggestions, and feedback are always welcome. Feel free to fork the repository, open an issue, or submit a pull request.

---

## 📄 License

This project is licensed under the MIT License.
