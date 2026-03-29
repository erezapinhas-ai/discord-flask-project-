from flask import Flask, request, render_template
import sqlite3
import requests

app = Flask(__name__)

URL = "YOUR_WEBHOOK_URL_HERE"

# פונקציה ליצירת הטבלה - מעודכנת לזמן מקומי
def init_db():
    conn = sqlite3.connect('massages.db')
    cursor = conn.cursor()
    # תיקון: הגדרת ברירת מחדל לזמן מקומי של המחשב (ישראל)
    cursor.execute('''CREATE TABLE IF NOT EXISTS webhook_massages (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        massage TEXT,
        timestamp DATETIME DEFAULT (DATETIME('now', 'localtime')));''')
    conn.commit()
    conn.close()

init_db()

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/input_text', methods=['POST'])
def webhook():
    user_text = request.form.get("text")
    if not user_text:
        return "Error: No text provided", 400

    # שמירה למסד נתונים
    try:
        conn = sqlite3.connect('massages.db')
        cursor = conn.cursor()
        cursor.execute('''INSERT INTO webhook_massages (massage) VALUES (?)''', (user_text,))
        conn.commit()
        conn.close()
    except Exception as e:
        print(f"Database error: {e}")

    # שליחה לדיסקורד
    payload = {"content": user_text}
    re = requests.post(URL, json=payload)

    if re.status_code in [200, 204]:
        return f"ההודעה '{user_text}' נשלחה ונשמרה בהצלחה! <br><a href='/'>חזרה</a> | <a href='/history'>להיסטוריה</a>"
    else:
        return f"שגיאה בדיסקורד: {re.status_code}", 500

@app.route('/history')
def show_history():
    conn = sqlite3.connect('massages.db')
    cursor = conn.cursor()

    # שאילתה מסוננת לפי זמן מקומי - 30 דקות אחרונות
    query = """
    SELECT massage, timestamp 
    FROM webhook_massages 
    WHERE timestamp >= DATETIME('now', '-30 minutes', 'localtime')
    ORDER BY timestamp DESC
    """

    cursor.execute(query)
    messages = cursor.fetchall()
    conn.close()

    return render_template("webhook_massages.html", messages=messages)

if __name__ == '__main__':
    app.run(debug=True)