import os
import pickle
from flask import Flask, render_template, request, jsonify

# Get the absolute path to the directory containing this script
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def detect(text):
    # Try multiple possible paths for the pickle file
    possible_paths = [
        "phishing detector.pkl",
        os.path.join(BASE_DIR, "phishing detector.pkl"),
        "phishing-detector.pkl",
        os.path.join(BASE_DIR, "phishing-detector.pkl"),
        os.path.join(BASE_DIR, "CyberSecurity", "phishing-detector", "phishing detector.pkl"),
    ]
    
    model_path = None
    for path in possible_paths:
        abs_path = os.path.abspath(path)
        print(f"Checking: {abs_path}")
        if os.path.exists(path):
            model_path = path
            print(f"✓ Found model at: {abs_path}")
            break
    
    if model_path is None:
        # List all .pkl files in current directory for debugging
        pkl_files = [f for f in os.listdir(BASE_DIR) if f.endswith('.pkl')]
        error_msg = (
            f"Could not find 'phishing detector.pkl' in any of the expected locations.\n"
            f"Current directory: {BASE_DIR}\n"
            f"PKL files found: {pkl_files if pkl_files else 'None'}\n"
            f"Please ensure the file is in the same directory as app.py"
        )
        raise FileNotFoundError(error_msg)
    
    with open(model_path, "rb") as f:
        m = pickle.load(f)
        r = m.predict([text])
    
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
        print(f"Prediction: '{prediction}'")
        
        # Check if it's a phishing email
        is_phishing = "phishing" in prediction.lower()
        
        return jsonify({
            "success": True,
            "result": prediction,
            "is_phishing": is_phishing
        })
    except Exception as e:
        print("Error:", e)
        import traceback
        traceback.print_exc()
        return jsonify({
            "success": False,
            "error": str(e)
        }), 500


if __name__ == '__main__':
    os.makedirs('templates', exist_ok=True)
    
    print("\n" + "="*70)
    print("Checking for model file...")
    print("="*70)
    print(f"Current directory: {BASE_DIR}")
    
    # Check if model file exists
    model_exists = False
    for path in ["phishing detector.pkl", "phishing-detector.pkl"]:
        full_path = os.path.join(BASE_DIR, path)
        if os.path.exists(full_path):
            model_exists = True
            print(f"✓ Model file found: {full_path}")
            break
    
    if not model_exists:
        print("\n⚠ WARNING: Model file not found!")
        print("Please ensure 'phishing detector.pkl' is in:", BASE_DIR)
        print("You can generate it by running: python main.py")
        
        # List all files in directory for debugging
        print("\nFiles in current directory:")
        for file in os.listdir(BASE_DIR):
            print(f"  - {file}")
    
    print("\n" + "="*70)
    print("E-Mail Phishing Detector")
    print("="*70)
    print("\n🌐 Starting server on http://127.0.0.1:5000")
    print("\nPress CTRL+C to stop the server")
    print("="*70 + "\n")
    
    app.run(debug=True, host='127.0.0.1', port=5000)