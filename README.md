Discord Flask Project 🚀
A Web application based on Flask that enables sending messages to a Discord server via Webhooks, with real-time logging and history tracking using an SQLite database.

📋 About the Project
This project was developed as part of a hands-on learning process in Backend development and systems integration. The application allows users to send messages directly to a pre-defined Discord channel using Webhooks, while simultaneously storing all message history in a local database for monitoring and auditing.

🛠 Technologies Used
Python 3.x - Core development and logic.

Flask - Web framework for serving the application.

SQLite - Lightweight database for history management.

Discord Webhooks - API interface for sending data to external servers.

HTML & Jinja2 - Dynamic UI and data presentation.

📂 Project Structure
Plaintext
discord-flask-progect/
├── app.py              # Main server logic and routes
├── database.db         # Local database (generated automatically)
└── templates/          # Frontend interface templates
    ├── index.html      # Home page & message submission form
    └── history.html    # Message history display page
📸 Key Features
Direct Messaging Interface: Send text messages to a Discord channel at the click of a button.

Full Logging: Every sent message is saved, including content and exact timestamp.

History Viewer: A dedicated page displaying all previously sent messages in an organized list.

Filtering Mechanism: Option to view only messages sent within the last 30 minutes.

This project was created as part of a DevOps and Python development learning journey.




בעברית:

Discord Flask Project 🚀
אפליקציית Web מבוססת Flask לניהול תקשורת עם שרת Discord ותיעוד נתונים בזמן אמת.

📋 אודות הפרויקט
פרויקט זה פותח כחלק מתרגול מעשי של פיתוח Backend ואינטגרציה בין מערכות. האפליקציה מאפשרת למשתמש לשלוח הודעות ישירות לערוץ דיסקורד מוגדר מראש באמצעות Webhooks, ובמקביל שומרת את כל היסטוריית ההודעות בבסיס נתונים מקומי לצורך מעקב ובקרה.

🛠 טכנולוגיות בשימוש
Python 3.x - ליבת הפיתוח והלוגיקה.

Flask - תשתית ה-Web להגשת האפליקציה.

SQLite - בסיס נתונים קליל לניהול ההיסטוריה.

Discord Webhooks - ממשק API לשליחת מידע לשרת חיצוני.

HTML & Jinja2 - בניית ממשק משתמש דינמי ותצוגת נתונים.

📂 מבנה הפרויקט
Plaintext
discord-flask-progect/
├── app.py              # קובץ השרת והלוגיקה המרכזית
├── database.db         # בסיס נתונים (נוצר אוטומטית)
└── templates/          # תבניות הממשק (Frontend)
    ├── index.html      # דף הבית ושליחת ההודעות
    └── history.html    # דף היסטוריית ההודעות המוקלטות

קבצים עיקריים

app.py: קובץ זה מכיל את הלוגיקה המרכזית של השרת. כאן מתבצע ניהול הבקשות מהמשתמשים, שליחת ההודעות ל-Discord, ותיעוד ההודעות שנשלחו.

database.db: בסיס הנתונים שבו נשמרות ההודעות שנשלחו. בסיס הנתונים נוצר אוטומטית בעת הרצת האפליקציה.

templates/: תיקייה זו מכילה את תבניות ה-HTML של הממשק.

index.html: דף הבית שבו המשתמש יכול לשלוח הודעות.

history.html: דף המאפשר למשתמש לצפות בהיסטוריית ההודעות שנשלחו.


תכונות עיקריות
ממשק שליחה ישיר: שליחת הודעות טקסט לערוץ דיסקורד בלחיצת כפתור.

תיעוד מלא (Logging): שמירת כל הודעה שנשלחה, כולל תוכן ההודעה ושעת השליחה המדויקת.

צפייה בהיסטוריה: הצגת רשימת כל ההודעות שנשלחו בעבר בצורה מסודרת.

מנגנון סינון: אפשרות לצפות בהודעות מה-30 דקות האחרונות בלבד.

פרויקט זה נוצר כחלק מתהליך למידה והתמקצעות בתחום ה-DevOps והפיתוח ב-Python




