# Phishing-Simulation Toolkit
Phishing Simulation Toolkit is a lightweight and educational tool designed to simulate real-world phishing attacks for cybersecurity awareness training.
A simple educatinal toolkit todemonstrate how phishing attacks work using a fack login form, flask backend, and automated exposure via ngrok.


## 📂 Project Structure

Phishing-simulation/
1. app.py #Flask server handling from submission
2. templates/
  2.1. login.html# Fake login page template
3. captured_data/
   3.1 credentials.txt #Stores captured login data
4. requirements.txt # Python dependencies
5. Phishing.sh #shell script to automate setup & launch

   ###Features
   -simple fack login from interface
   - Flask backend to receive and store submitted credntials
   - Auto-start script with Flask + ngrok tunnel
   - Real-time logging of credentials to 'captured_data/credentials.txt'
  
     ----

     '''bash
     git clone https://github.com/amartyadas27/Phishing-Simulation.git

     cd phishing-simulation

     Pip install Flask

     python3 -m venv venv

     source venv/bin/activate

     pip install -r requirments.txt


     ./ngrok authtoken YOUR_TOKEN

     chmod +x Phishing.sh

     ./phishing.sh


     

     
