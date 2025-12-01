import os
import pickle
from flask import Flask, render_template, request, jsonify, send_file

def detect(text):
    f=open("phishing detector.pkl", "rb")
    m=pickle.load(f)
    r=m.predict([text])
    f.close()
    return r


app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():
    result = None
    if request.method == "POST":
        mail = request.form.get("mail")
        if mail:
            try:
                prediction = detect(mail)[0]
                result = prediction
                print("Detection Result:", prediction)
            except Exception as e:
                print("Error during detection:", e)
                result = "Error"

    return render_template("index.html", result=result)


@app.route("/detect", methods=["POST"])
def detect_email():
    try:
        email_text = request.form.get("mail")
        if not email_text:
            return jsonify({"error": "No email text provided"}), 400
        
        prediction = detect(email_text)[0]
        return jsonify({
            "success": True,
            "result": prediction,
            "is_phishing": prediction.lower() in ["phishing email"]
        })
    except Exception as e:
        print("Error:", e)
        return jsonify({
            "success": False,
            "error": str(e)
        }), 500


if __name__ == '__main__':
    os.makedirs('templates', exist_ok=True)
    
    # Check if model file exists
    model_exists = False
    for path in ["phishing detector.pkl", "phishing-detector.pkl"]:
        if os.path.exists(path):
            model_exists = True
            print(f"Model file found: {path}")
            break
    
    if not model_exists:
        print("\n" + "="*70)
        print("WARNING: Model file not found!")
        print("="*70)
        print("Please ensure 'phishing detector.pkl' is in the same directory as app.py")
        print("You can generate it by running: python main.py")
        print("="*70 + "\n")
    
    print("\n" + "="*70)
    print("E-Mail Phishing Detector")
    print("="*70)
    print("\n🌐 Starting server on http://127.0.0.1:5000")
    print("\nPress CTRL+C to stop the server")
    print("="*70 + "\n")
    
    app.run(debug=True, host='127.0.0.1', port=5000)