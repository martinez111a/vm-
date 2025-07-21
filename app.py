rom flask import Flask, render_template
import sqlite3

app = Flask(__name__)

@app.route('/')
def home():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS visitas (id INTEGER PRIMARY KEY AUTOINCREMENT)")
    cursor.execute("INSERT INTO visitas DEFAULT VALUES")
    conn.commit()
    total = cursor.execute("SELECT COUNT(*) FROM visitas").fetchone()[0]
    conn.close()
    return render_template('index.html', total=total)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
