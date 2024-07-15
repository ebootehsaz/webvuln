from flask import Flask, request, redirect, url_for, render_template_string, session, flash


app = Flask(__name__)
app.secret_key = 'bvfdhfvla'  # Use a strong, random value in production
app.config.update(
    SESSION_COOKIE_SAMESITE='Lax',
)


users = {
    'admin': {
        'username': 'admin',
        'password': 'adminpass'  # In a real application, use hashed passwords
    }
}


HTML_TEMPLATE = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Profile Management Service</title>
    <style>
        body { font-family: Arial, sans-serif; padding: 40px; }
        input, button { padding: 10px; margin-top: 10px; }
        form { margin-bottom: 20px; }
        .message { color: red; margin-bottom: 20px; }
    </style>
</head>
<body>
    {% with messages = get_flashed_messages() %}
        {% if messages %}
            <div class="message">
                {% for message in messages %}
                    <p>{{ message }}</p>
                {% endfor %}
            </div>
        {% endif %}
    {% endwith %}
    {{content|safe}}
</body>
</html>
'''

@app.route('/welcome')
def welcome():
    if 'authenticated' in session:
        content_html = f'''
            <h1>Welcome, {users['admin']['username']}</h1>
            '''
        return render_template_string(HTML_TEMPLATE, content=content_html)
    else:
        return render_template_string(HTML_TEMPLATE, content='''
        <h1>Login</h1>
        <form action="/login" method="POST">
            <input type="text" name="password" placeholder="Password">
            <button type="submit">Login as Admin</button>
        </form>
        ''')

@app.route('/')
def index():
    if 'authenticated' in session:
        content_html = f'''
            <h1>Welcome!</h1>
            <a href="/welcome" class="button-style">HomePage</a>
            <p>Change your password or username below:</p>
            <form action="/update-password" method="POST">
                <input type="text" name="new_password" placeholder="Enter new password">
                <button type="submit">Update Password</button>
            </form>
            
            <form action="/update-username" method="POST">
                <input type="text" name="new_username" placeholder="Enter new username">
                <button type="submit">Change Username</button>
            </form>
            <a href="/logout">Logout</a>
        '''
        return render_template_string(HTML_TEMPLATE, content=content_html)
    else:
        return render_template_string(HTML_TEMPLATE, content='''
        <h1>Login</h1>
        <form action="/login" method="POST">
            <input type="text" name="password" placeholder="Password">
            <button type="submit">Login as Admin</button>
        </form>
        ''')


@app.route('/login', methods=['POST'])
def login():
    password = request.form['password']
    if password == users['admin']['password']:
        session['authenticated'] = True
        return redirect(url_for('index'))
    flash('Login failed. Incorrect password.')
    return redirect(url_for('index'))


@app.route('/logout')
def logout():
    session.pop('authenticated', None)
    return redirect(url_for('index'))

# Legacy sites may use GET requests to update user data
@app.route('/update-password', methods=['GET', 'POST'])
def update_password():
    if 'authenticated' not in session:
        flash('Update failed. You are not authenticated.')
        return redirect(url_for('index'))
    
    if request.method == 'POST':
        # Access form data for POST requests
        new_password = request.form.get('new_password', '')
    else:
        # Access query parameters for GET requests
        new_password = request.args.get('new_password', '')
    
    if new_password:
        users['admin']['password'] = new_password
        print(f"New password: {new_password}")
        flash('Password changed successfully.')
    else:
        flash('Update failed. No password provided.')
    return redirect(url_for('index'))
    

@app.route('/update-username', methods=['GET', 'POST'])
def update_username():
    if 'authenticated' not in session:
        return redirect(url_for('index'))
    
    if request.method == 'POST':
        # Access form data for POST requests
        new_username = request.form.get('new_username', '')
    else:
        # Access query parameters for GET requests
        new_username = request.args.get('new_username', '')
    
    users['admin']['username'] = new_username
    return redirect(url_for('welcome'))

if __name__ == '__main__':
    app.run(debug=True)
