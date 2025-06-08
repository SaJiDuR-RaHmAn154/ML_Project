# CardioInsight: Heart Disease Prediction Web App

## Project Structure

```
ML_Project/
│
├── Frontend/
│   ├── app.py                  # Main Flask application
│   ├── database.py             # MongoDB database operations
│   ├── templates/              # HTML templates (login, signup, home, etc.)
│   ├── static/                 # Static files (CSS, images, JS)
│   │   ├── CSS/
│   │   └── Images/
│   └── requirements.txt        # Python dependencies
│
├── heart.csv                   # Main dataset (large)
├── Heart_Disease_Dataset.csv   # Dataset with headers only (for transfer)
└── ...                         # Other files
```

- **app.py**: Main Flask backend for the web app.
- **database.py**: Handles all MongoDB user operations (registration, login, password reset).
- **templates/**: Contains all HTML pages.
- **static/**: Contains CSS, images, and other static assets.
- **requirements.txt**: All required Python packages for the project.

---

## Getting Started

### 1. Clone the Repository

```sh
git clone <your-repo-url>
cd ML_Project/Frontend
```

### 2. Create a Virtual Environment

```sh
python3 -m venv .venv
```

### 3. Activate the Virtual Environment

- **On macOS/Linux:**
  ```sh
  source .venv/bin/activate
  ```
- **On Windows:**
  ```sh
  .venv\Scripts\activate
  ```

### 4. Install Required Packages

```sh
pip install -r requirements.txt
```

### 5. Run the Flask App

```sh
python app.py
```

The app will start on [http://localhost:4000](http://localhost:4000).

---

## Notes

- Make sure you have **MongoDB** running locally before starting the app.
- Update email credentials in `app.py` for Flask-Mail if needed.
- For any issues, check the error messages in your terminal for missing dependencies or misconfigurations.

---

Enjoy using **CardioInsight**!