# 🛡️ Phishing Email Detector

A beautiful, modern web application that uses machine learning to detect phishing emails with 97% accuracy. Built with Flask, scikit-learn, and a stunning gradient UI.

![Phishing Detector](https://img.shields.io/badge/Accuracy-97%25-brightgreen)
![Python](https://img.shields.io/badge/Python-3.7+-blue)
![Flask](https://img.shields.io/badge/Flask-2.0+-lightgrey)
![License](https://img.shields.io/badge/License-MIT-yellow)

## ✨ Features

- 🎯 **High Accuracy**: 97% accurate phishing detection using Logistic Regression
- 🎨 **Modern UI**: Beautiful gradient background with glassmorphism design
- 🔄 **Real-time Analysis**: Instant email analysis with animated loading states
- 📱 **Responsive Design**: Works seamlessly on desktop, tablet, and mobile
- 🎭 **3D Card Effects**: Interactive 3D tilt effects on hover
- 💫 **Smooth Animations**: Fluid transitions and glowing result indicators
- 🟢🔴 **Visual Feedback**: Color-coded results (Green = Safe, Red = Phishing)

## 🖼️ Screenshots

### Main Interface
Clean, modern interface with animated gradient background and glassmorphic card design.

### Phishing Detection
Red glowing indicator with clear warning message when phishing is detected.

### Safe Email
Green glowing indicator confirming the email is safe and legitimate.

## 🚀 Quick Start

### Prerequisites

- Python 3.7 or higher
- pip (Python package manager)
- A dataset file: `data set/Phishing_Email.csv`

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/phishing-detector.git
   cd phishing-detector
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Prepare your dataset**
   
   Ensure you have a CSV file at `data set/Phishing_Email.csv` with the following columns:
   - `Email Text`: The content of the email
   - `Email Type`: Label ('Safe Email' or 'Phishing Email')

4. **Train the model**
   ```bash
   python main.py
   ```
   
   This will create `phishing detector.pkl` file containing the trained model.

5. **Run the application**
   ```bash
   python app.py
   ```

6. **Open your browser**
   
   Navigate to `http://127.0.0.1:5000`

## 📁 Project Structure

```
phishing-detector/
├── data set/
│   └── Phishing_Email.csv      # Training dataset
├── static/
│   ├── css/
│   │   └── styles.css          # All styling and animations
│   └── js/
│       └── app.js              # Frontend logic and interactions
├── templates/
│   └── index.html              # Main HTML template
├── app.py                      # Flask backend server
├── main.py                     # Model training script
├── phishing detector.pkl       # Trained model (generated)
├── requirements.txt            # Python dependencies
└── README.md                   # This file
```

## 🔧 Configuration

### Model Training

You can modify the model in `main.py`:

```python
# Current: Logistic Regression
pipe = Pipeline([
    ("tfidf", TfidfVectorizer(stop_words="english", max_features=5000)),
    ("clf", LogisticRegression()),
])

# Alternative: Random Forest (commented out in main.py)
pipe = Pipeline([
    ("tfidf", TfidfVectorizer(stop_words="english", max_features=5000)),
    ("clf", RandomForestClassifier(random_state=42)),
])
```

### Server Configuration

Modify `app.py` to change server settings:

```python
app.run(
    debug=True,              # Set to False in production
    host='127.0.0.1',        # Change to '0.0.0.0' for network access
    port=5000                # Change port if needed
)
```

## 🎨 UI Customization

The entire UI is customizable through CSS variables in `static/css/styles.css`:

```css
:root {
    --color-bg: #050505;           /* Background color */
    --color-text: #ffffff;         /* Text color */
    --color-primary: #ff3366;      /* Primary gradient color */
    --color-secondary: #3366ff;    /* Secondary gradient color */
    --color-tertiary: #33ddff;     /* Tertiary gradient color */
    --color-accent: #ffcc00;       /* Accent color */
    --color-danger: #ff3366;       /* Phishing indicator */
    --color-success: #00ff88;      /* Safe indicator */
}
```

## 🧪 API Endpoints

### `GET /`
Renders the main page with the detection interface.

### `POST /`
Handles form submission and returns HTML response.

**Parameters:**
- `mail` (form-data): Email text to analyze

### `POST /detect`
API endpoint for programmatic access.

**Request:**
```json
{
    "mail": "Email content here..."
}
```

**Response:**
```json
{
    "success": true,
    "result": "Phishing Email",
    "is_phishing": true
}
```

## 📊 Model Performance

- **Algorithm**: Logistic Regression with TF-IDF Vectorization
- **Accuracy**: ~97%
- **Features**: 5000 TF-IDF features
- **Training Split**: 80% training, 20% testing
- **Stop Words**: English stop words removed

## 🛠️ Technologies Used

### Backend
- **Flask**: Web framework
- **scikit-learn**: Machine learning
- **pandas**: Data manipulation
- **NumPy**: Numerical computations
- **pickle**: Model serialization

### Frontend
- **HTML5**: Structure
- **CSS3**: Styling and animations
- **JavaScript (ES6+)**: Interactions and API calls
- **Font Awesome**: Icons

### Design
- **Glassmorphism**: Translucent card design
- **Gradient Animation**: Floating blob animations
- **3D Transforms**: Interactive tilt effects
- **Backdrop Filter**: Blur effects

## 🐛 Troubleshooting

### Model file not found
```
Error: [Errno 2] No such file or directory: 'phishing detector.pkl'
```

**Solution**: Run `python main.py` to generate the model file first.

### Dataset not found
```
FileNotFoundError: [Errno 2] No such file or directory: 'data set/Phishing_Email.csv'
```

**Solution**: Ensure your dataset is in the correct location with the correct name.

### Port already in use
```
OSError: [Errno 98] Address already in use
```

**Solution**: Change the port in `app.py` or kill the process using port 5000:
```bash
# Linux/Mac
lsof -ti:5000 | xargs kill -9

# Windows
netstat -ano | findstr :5000
taskkill /PID <PID> /F
```

### Module not found
```
ModuleNotFoundError: No module named 'sklearn'
```

**Solution**: Install all dependencies:
```bash
pip install -r requirements.txt
```

## 📝 Requirements

```
scikit-learn>=1.0.0
pandas>=1.3.0
numpy>=1.21.0
flask>=2.0.0
```

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👤 Author

**Siddharth Mathur**
- GitHub: [@SiddharthMathur01](https://github.com/SiddharthMathur01)
- Email: 16mathursiddharth@gmail.com

## 🙏 Acknowledgments

- Dataset source: [https://www.kaggle.com/datasets/subhajournal/phishingemails]
- Inspired by modern web design trends
- Built with ❤️ using Flask and scikit-learn

## 📈 Future Enhancements

- [ ] Add email history tracking
- [ ] Implement user authentication
- [ ] Support for multiple languages
- [ ] Export detection reports
- [ ] Batch email analysis
- [ ] Integration with email clients
- [ ] Advanced analytics dashboard
- [ ] Real-time threat intelligence updates

---

Made with ❤️ and Python | ⭐ Star this repo if you find it helpful!
