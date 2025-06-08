from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__, template_folder='templates')

@app.route('/')
def index():
    now = datetime.now()
    return render_template('index.html', 
        current_time=now.strftime("%H:%M:%S"),
        current_date=now.strftime("%Y-%m-%d")
    )

if __name__ == '__main__':
    app.run(debug=True)
