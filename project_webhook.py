from flask import Flask, request, render_template, redirect, url_for
import sqlite3
import requests
import webbrowser    #כדי שהפרויקט ייפתח ישר בדפדפן כשמריצים התוכנית

app = Flask(__name__)


# פונקציה ליצירת הטבלאות - כולל טבלת הגדרות חדשה
def init_db():
    conn = sqlite3.connect('massages.db')
    cursor = conn.cursor()
    # טבלת הודעות קיימת
    cursor.execute('''CREATE TABLE IF NOT EXISTS webhook_massages (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        massage TEXT,
        timestamp DATETIME DEFAULT (DATETIME('now', 'localtime')));''')

    # טבלה חדשה לשמירת ה-URL של המשתמש
    cursor.execute('''CREATE TABLE IF NOT EXISTS settings 
                      (key TEXT PRIMARY KEY, value TEXT)''')
    conn.commit()
    conn.close()


init_db()


# פונקציית עזר לשליפת ה-URL הנוכחי מהדאטה-בייס
def get_current_webhook():
    conn = sqlite3.connect('massages.db')
    cursor = conn.cursor()
    cursor.execute("SELECT value FROM settings WHERE key = 'discord_url'")
    row = cursor.fetchone()
    conn.close()
    return row[0] if row else None


@app.route('/')
def index():
    # שולחים לדף הבית את ה-URL הנוכחי כדי שהמשתמש יראה מה מוגדר
    current_url = get_current_webhook()
    return render_template("index.html", current_url=current_url)


@app.route('/update_settings', methods=['POST'])
def update_settings():
    new_url = request.form.get("discord_url")
    if new_url:
        conn = sqlite3.connect('massages.db')
        cursor = conn.cursor()
        # INSERT OR REPLACE דואג שאם כבר יש ערך, הוא פשוט יתעדכן
        cursor.execute("INSERT OR REPLACE INTO settings (key, value) VALUES ('discord_url', ?)", (new_url,))
        conn.commit()
        conn.close()
    return redirect(url_for('index'))


@app.route('/input_text', methods=['POST'])
def webhook():
    user_text = request.form.get("text")
    # שולפים את ה-URL שהמשתמש הגדיר
    target_url = get_current_webhook()

    if not target_url:
        return "שגיאה: לא הגדרת כתובת Webhook! חזרי לדף הבית והגדירי אחת.", 400

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

    # שליחה לדיסקורד עם הכתובת הדינמית
    payload = {"content": user_text}
    try:
        re = requests.post(target_url, json=payload)
        if re.status_code in [200, 204]:
            return f"ההודעה '{user_text}' נשלחה לדיסקורד ונשמרה! <br><a href='/'>חזרה</a> | <a href='/history'>להיסטוריה</a>"
        else:
            return f"שגיאה בדיסקורד: {re.status_code}", 500
    except Exception as e:
        return f"שגיאה בשליחה: וודאי שהכתובת שהזנת תקינה. ({e})", 500


@app.route('/history')
def show_history():
    conn = sqlite3.connect('massages.db')
    cursor = conn.cursor()
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
    # פתיחת הדפדפן רק פעם אחת
    webbrowser.open("http://127.0.0.1:5000")

    # ב-EXE עדיף לכבות את ה-debug כדי שהחלון לא יקפוץ פעמיים
    app.run(host='127.0.0.1', port=5000, debug=False)