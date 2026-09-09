# ⚡ Cyb3rShare

A fast and private local file transfer system for sending files from an Android phone to a Windows laptop over Wi-Fi.

No cloud.  
No cables.  
No Bluetooth.  
No third-party storage.

## 🚀 Current Version

**Cyb3rShare V1**

Current direction:

**PHONE → LAPTOP**

The laptop runs a lightweight Python server. The phone connects to the laptop through a browser using the laptop's local network address.

## ✨ Features

- 📱 Android phone → Windows laptop
- ⚡ Fast local-network transfers
- 🔒 Files remain on the local network
- ☁️ No cloud storage
- 🔌 No USB cable required
- 📡 Works over Wi-Fi or phone hotspot
- 📁 Controlled receiving directory
- 🛡️ Basic filename/path protection
- 🎥 Successfully tested with large files, including an 80 MB video

## 🛠️ Tech Stack

- Python
- HTTP Server
- HTML
- CSS
- JavaScript
- python-multipart

## 📂 Project Structure

```text
Cyb3rShare/
├── server.py
├── README.md
├── .gitignore
├── web/
│   ├── index.html
│   ├── style.css
│   └── script.js
└── received/

## ▶️ How To Run

### 1. Clone the repository
git clone https://github.com/Bigg-jxy/Cyb3rShare.git

2. Enter the project folder
cd Cyb3rShare

3. Install the required package
pip install python-multipart

4. Start the server
python server.py

The server will run on port 8080.

5. Connect your phone

Make sure the phone and laptop are connected to the same Wi-Fi network or phone hotspot.

Find the laptop's local IP address and open:

http://YOUR-LAPTOP-IP:8080

on the phone.

6. Send a file

Choose a file on the phone and press:

SEND FILE

The file will be saved inside:

received/
🗺️ Roadmap
 V1 — Phone → Laptop transfer
 V1.1 — Transfer progress, speed and ETA
 V1.2 — Improved file information
 V1.3 — Multiple file transfers
 V1.4 — Transfer history
 V2 — Laptop → Phone
 V3 — Automatic device discovery
 V4 — Multi-file transfer improvements
 V5 — Advanced transfer monitoring
 V6 — Android application
 V7 — Clipboard, text and link sharing
 V8 — Pairing and stronger security
🎯 Goal

Cyb3rShare is being built as a simple alternative to cloud-based file sharing for situations where devices are connected to the same local network.

The goal is simple:

Connect → Choose → Send.

👨‍💻 Author

John Joshua Ikpong

Built as a personal learning and development project.
