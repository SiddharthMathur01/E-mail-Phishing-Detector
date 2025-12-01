import os
import pickle
from flask import Flask, render_template, request, jsonify, send_file

def detect(text):
    f=open("CyberSecurity/phishing-detector/phishing detector.pkl", "rb")
    m=pickle.load(f)
    r=m.predict([text])
    f.close()
    return r


app=Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        username = request.form.get("username")
        print("Received from HTML:", detect(username)[0])

    return render_template("index.html")

if __name__ == '__main__':
    os.makedirs('templates', exist_ok=True)
       
    print("\n" + "="*70)
    print("E-Mail Phishing Detector")
    print("="*70)
    print("\n🌐 Starting server on http://127.0.0.1:5000")
    print("\nPress CTRL+C to stop the server")
    print("="*70 + "\n")
    
    app.run(debug=True, host='127.0.0.1', port=5000)