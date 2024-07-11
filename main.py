
from flask import Flask, render_template, request

app = Flask(__name__)
connection = sqlite3.connect('health_fitness.db')
cursor = connection.cursor()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    data = request.form.to_dict()
    cursor.execute('INSERT INTO data (activity, sleep, heart) VALUES (?, ?, ?)',
        (data['activity'], data['sleep'], data['heart']))
    connection.commit()
    return redirect('/dashboard')

@app.route('/dashboard')
def dashboard():
    data = cursor.execute('SELECT * FROM data').fetchall()
    return render_template('dashboard.html', data=data)

@app.route('/insights')
def insights():
    return render_template('insights.html')

@app.route('/goals')
def goals():
    return render_template('goals.html')

if __name__ == '__main__':
    app.run(debug=True)
