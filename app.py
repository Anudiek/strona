from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Strona główna z logowaniem i linkami
@app.route('/')
def index():
    return render_template('index.html')

# Strona dostępna po zalogowaniu
@app.route('/logged_in')
def logged_in():
    return render_template('logged_in.html')

# Obsługa logowania
@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')
    if username and password:  # Proste sprawdzenie, brak zaawansowanej walidacji
        return redirect(url_for('logged_in'))
    return redirect(url_for('index'))

# Obsługa formularza
@app.route('/submit', methods=['POST'])
def submit():
    name = request.form.get('name')
    email = request.form.get('email')
    with open('submissions.txt', 'a') as file:
        file.write(f"Name: {name}, Email: {email}\n")
    return render_template('success.html', name=name)

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)


