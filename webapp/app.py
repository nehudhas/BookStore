from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'supersecretkey'

# Sample user data
users = {
    'validUser': 'validPassword123'
}

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        if username in users and users[username] == password:
            flash(f"Welcome {username}")
            return redirect(url_for('login'))
        else:
            flash("Invalid credentials")
            return redirect(url_for('login'))
    
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        confirm_password = request.form['confirm_password']
        
        # Simple validation
        if username in users:
            flash("Username already exists")
        elif password != confirm_password:
            flash("Passwords do not match")
        else:
            users[username] = password
            flash("Registration successful")
            return redirect(url_for('login'))
    
    return render_template('register.html')

if __name__ == '__main__':
    app.run(debug=True)
