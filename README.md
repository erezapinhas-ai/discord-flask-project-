🚀 Discord Webhook Manager (Full-Stack Web App)
A professional, easy-to-use desktop application designed to streamline sending messages to Discord channels via Webhooks. Built with Python and Flask, this project features a local database for message history and an automated standalone executable (EXE) for end-users.

✨ Features
User-Friendly Web Interface: Clean HTML/CSS interface for message input and configuration.

Discord Integration: Instant communication with Discord using Webhook URLs.

Local Database Storage: Uses SQLite to log and display a history of sent messages.

Automated Desktop Experience: A standalone .exe version that automatically launches your default web browser to the app's address.

Message Persistence: Review your past activity through a dedicated history page.

🛠️ Technology Stack
Backend: Python 3.x, Flask

Database: SQLite3

Networking: Requests (HTTP Library)

Frontend: HTML5, CSS3

Distribution: PyInstaller (Standalone Executable)

📂 Project Structure
Plaintext
.
├── project_webhook.py      # Main application logic & Flask server
├── messages.db             # SQLite database (generated on first run)
├── templates/              # Frontend UI folder
│   ├── index.html          # Main control panel
│   └── history.html        # Message history viewer
└── dist/                   # Contains the portable .exe version
🚀 Getting Started
Option 1: Running the Executable (Recommended for Users)
Navigate to the dist/ folder.

Run project_webhook.exe.

A terminal window will open, and your web browser will automatically launch at http://127.0.0.1:5000.

Option 2: Running from Source (For Developers)
Clone the repository:

Bash
git clone https://github.com/erezapinhas-ai/discord-flask-project.git
Install dependencies:

Bash
pip install -r requirements.txt
Run the application:

Bash
python project_webhook.py
🛠️ Build Process (DevOps Notes)
To package this application into a standalone EXE, the following command was used:

Bash
python -m PyInstaller --clean --onefile --hidden-import="requests" --add-data "templates/*;templates" project_webhook.py
🛡️ Important Note on Security
When running the .exe for the first time, Windows SmartScreen may display a warning.

Click "More Info"

Select "Run Anyway"
This occurs because the application is a custom-built tool and is not digitally signed by a commercial CA.

Developed as part of a DevOps engineering journey. 💻🌐