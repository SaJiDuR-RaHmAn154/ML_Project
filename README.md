# CardioInsight: AI-Powered Heart Disease Prediction Web App

CardioInsight is a comprehensive full-stack web application that leverages advanced machine learning algorithms to predict heart disease risk. The platform provides users with secure authentication, educational resources, health tracking, and personalized recommendations for maintaining cardiovascular health.

---

## 🚀 Key Features

### 🔐 **Secure User Management**
- **User Registration & Authentication:** Secure signup and login with email verification
- **Password Reset:** Automated password recovery via email with 6-digit temporary passwords
- **Session Management:** Secure session handling with logout functionality
- **Profile Management:** User profile updates with photo upload capabilities

### 🧠 **AI-Powered Health Assessment**
- **Heart Disease Prediction:** Machine learning model trained on medical datasets
- **Risk Assessment:** Confidence scores and probability analysis
- **Multiple ML Models:** Random Forest, Decision Tree, and Logistic Regression comparison
- **Feature Scaling:** Standardized input processing for accurate predictions

### 📊 **Health Dashboard & Tracking**
- **Prediction History:** Complete history of all health assessments
- **Visual Analytics:** Charts and statistics for health trends
- **Detailed Reports:** Comprehensive analysis with confidence metrics
- **Export Functionality:** Download health reports for medical consultations

### 📚 **Educational Resources**
- **Cardiac Information:** Comprehensive heart health education
- **Prevention Guidelines:** Evidence-based prevention strategies
- **Health Statistics:** Population-level health insights
- **Interactive Content:** Engaging educational materials

### 🎨 **Modern User Experience**
- **Responsive Design:** Mobile-first, cross-device compatibility
- **Ocean Theme UI:** Professional medical-grade interface
- **Toast Notifications:** Real-time user feedback
- **Guest Access:** Explore features without registration

---

## 🗂️ Project Architecture

```
ML_Project/
│
├── Heart_Disease_Analysis.ipynb    # Jupyter notebook for ML model training
├── Heart_Disease_Prediction.csv    # Training dataset
├── heartdiseaseprediction.model    # Trained ML model (pickle file)
├── requirements.txt                # Python dependencies
├── venv/                          # Virtual environment
│
└── Frontend/                      # Main web application
    ├── app.py                     # Flask backend with routing & logic
    ├── database.py                # MongoDB operations & user management
    ├── heartdiseaseprediction.model # ML model for predictions
    ├── scaler.model               # Feature scaling model
    ├── model_info.pkl             # Model metadata
    │
    ├── templates/                 # HTML templates
    │   ├── home.html              # Landing page with navigation
    │   ├── login.html             # User authentication
    │   ├── signup.html            # User registration
    │   ├── forgot.html            # Password recovery
    │   ├── profile.html           # User dashboard & history
    │   ├── find.html              # Health assessment form
    │   ├── check.html             # Alternative prediction form
    │   ├── results.html           # Prediction results display
    │   ├── input_details.html     # Detailed input review
    │   ├── cardiac_info.html      # Heart health education
    │   ├── prevention.html        # Prevention guidelines
    │   └── statistics.html        # Health statistics & insights
    │
    └── static/                    # Static assets
        ├── CSS/                   # Stylesheet files
        │   ├── home.css           # Landing page styles
        │   ├── login.css          # Authentication styles
        │   ├── profile.css        # Dashboard styles
        │   ├── find.css           # Prediction form styles
        │   ├── results.css        # Results page styles
        │   └── [other].css        # Page-specific styles
        │
        ├── Images/                # Application assets
        │   ├── heartLogo.jpg      # Application logo
        │   ├── favicon.png        # Browser icon
        │   └── [charts].png       # Statistical visualizations
        │
        └── uploads/               # User-uploaded content
            └── [profile_pics]/    # User profile pictures
```

### 🔧 **Core Components**

- **`app.py`:** Main Flask application with route handlers, authentication logic, and ML prediction integration
- **`database.py`:** MongoDB interface for user management, authentication, and data persistence
- **`Heart_Disease_Analysis.ipynb`:** Complete ML pipeline for model training and evaluation
- **Templates:** Comprehensive set of responsive HTML pages with Bootstrap integration
- **Static Assets:** Professional CSS styling, images, and user uploads

---

## 🖥️ Installation & Setup

### 1. **Clone the Repository**

```bash
git clone <your-repo-url>
cd ML_Project
```

### 2. **Set Up Python Environment**

**Create Virtual Environment:**
```bash
# On macOS/Linux
python3 -m venv venv

# On Windows
python -m venv venv
```

**Activate Virtual Environment:**
```bash
# On macOS/Linux
source venv/bin/activate

# On Windows
venv\Scripts\activate
```

### 3. **Install Dependencies**

```bash
pip install -r requirements.txt
```

### 4. **Configure Database**

**Install & Start MongoDB:**
- Download [MongoDB Community Server](https://www.mongodb.com/try/download/community)
- Start MongoDB service:
  ```bash
  # On macOS (with Homebrew)
  brew services start mongodb-community
  
  # On Windows/Linux
  mongod
  ```

### 5. **Configure Email Settings**

Update email credentials in `Frontend/app.py`:
```python
app.config["MAIL_USERNAME"] = "your_email@gmail.com"
app.config["MAIL_PASSWORD"] = "your_app_password"
```

**For Gmail users:**
1. Enable 2-Factor Authentication
2. Generate App Password in Google Account settings
3. Use the App Password (not your regular password)

### 6. **Train ML Model (Optional)**

If you want to retrain the model:
```bash
# Open and run the Jupyter notebook
jupyter notebook Heart_Disease_Analysis.ipynb
```

The pre-trained models are already included in the project.

### 7. **Launch Application**

```bash
cd Frontend
python app.py
```

🚀 **Access the application at:** [http://localhost:4000](http://localhost:4000)

---

## 💡 How to Use CardioInsight

### 🔐 **Getting Started**

1. **Register Account:**
   - Visit the signup page
   - Enter your email and username
   - A secure 6-digit password will be sent to your email
   - Use this password to log in

2. **Login:**
   - Use your email and received password
   - Enable "Remember Me" for convenience
   - Access guest mode to explore features

### 🏥 **Health Assessment**

3. **Take Health Assessment:**
   - Navigate to "Predict" from the dashboard
   - Fill in comprehensive health metrics:
     - Age, Gender, Chest Pain Type
     - Blood Pressure, Cholesterol levels
     - Exercise tolerance, EKG results
     - And other cardiac indicators
   - Submit for AI analysis

4. **View Results:**
   - Get instant prediction: Presence/Absence of heart disease risk
   - Review confidence score and probability metrics
   - Access detailed analysis and recommendations

### 📊 **Dashboard Features**

5. **Profile Management:**
   - View complete prediction history
   - Update profile information and photo
   - Track health trends over time
   - Export reports for medical consultations

6. **Educational Resources:**
   - **Cardiac Info:** Learn about heart health
   - **Prevention:** Evidence-based prevention strategies
   - **Statistics:** Population health insights

### 🔧 **Account Management**

7. **Password Recovery:**
   - Use "Forgot Password?" link
   - Enter email and username
   - New 6-digit password sent via email

8. **Security Features:**
   - Secure session management
   - Automatic logout for security
   - Password encryption and protection

---

## 🤖 Machine Learning Implementation

### **Model Architecture**
- **Algorithms:** Random Forest, Decision Tree, Logistic Regression
- **Feature Engineering:** 13 standardized cardiac indicators
- **Performance:** Best model automatically selected based on accuracy
- **Scaling:** StandardScaler for feature normalization

### **Health Metrics Analyzed**
- Age and Gender
- Chest Pain Type (4 categories)
- Resting Blood Pressure
- Serum Cholesterol levels
- Fasting Blood Sugar
- Resting EKG results
- Maximum Heart Rate achieved
- Exercise-induced Angina
- ST Depression
- Slope of peak exercise ST segment
- Number of major vessels colored by fluoroscopy
- Thallium stress test results

### **Model Training Process**
1. Data preprocessing and cleaning
2. Feature scaling and normalization
3. Train-test split (80/20)
4. Model comparison and evaluation
5. Best model selection and deployment
6. Pickle serialization for production use

---

## 🛠️ Technical Stack

### **Backend**
- **Framework:** Flask 3.1.1
- **Database:** MongoDB with PyMongo
- **Authentication:** Flask sessions with password hashing
- **Email:** Flask-Mail for notifications
- **ML Libraries:** scikit-learn, pandas, numpy

### **Frontend**
- **UI Framework:** Bootstrap 5.3.3
- **Icons:** Bootstrap Icons
- **Styling:** Custom CSS with ocean theme
- **Responsive:** Mobile-first design
- **Animations:** CSS animations and transitions

### **Data Science**
- **Analysis:** Jupyter Notebook
- **Visualization:** Matplotlib for model evaluation
- **Model Persistence:** Pickle for model serialization
- **Feature Engineering:** StandardScaler integration

---

## 📁 Code Structure Deep Dive

### **Backend Architecture (`app.py`)**
- Route handlers for all endpoints
- User authentication and session management
- ML model integration and prediction logic
- Email notification system
- File upload handling for profile pictures

### **Database Layer (`database.py`)**
- User registration and authentication
- Password hashing with Werkzeug
- MongoDB operations for user data
- Prediction history storage
- Profile management functions

### **Frontend Templates**
- **Authentication Pages:** login.html, signup.html, forgot.html
- **Dashboard:** home.html, profile.html
- **Prediction System:** find.html, check.html, results.html, input_details.html
- **Educational:** cardiac_info.html, prevention.html, statistics.html

### **Styling System**
- Modular CSS architecture
- Page-specific stylesheets
- Consistent ocean theme
- Responsive breakpoints
- Professional medical interface

---

## 🛠️ Troubleshooting & FAQ

### **Common Issues**

**🔴 MongoDB Connection Error**
```bash
# Start MongoDB service
# macOS (Homebrew)
brew services start mongodb-community

# Windows
net start MongoDB

# Linux/Manual
mongod --dbpath /data/db
```

**🔴 Email Not Sending**
- Verify Gmail App Password (not regular password)
- Check Flask-Mail configuration in `app.py`
- Ensure 2FA is enabled on Gmail account
- Test with different email provider if needed

**🔴 Module Import Errors**
```bash
# Ensure virtual environment is activated
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate     # Windows

# Reinstall dependencies
pip install -r requirements.txt
```

**🔴 Port Already in Use**
```bash
# Kill process on port 4000
# macOS/Linux
lsof -ti:4000 | xargs kill -9

# Windows
netstat -ano | findstr :4000
taskkill /PID <process_id> /F
```

**🔴 Model Loading Error**
- Ensure model files exist in `Frontend/` directory
- Retrain models using the Jupyter notebook if needed
- Check pickle file compatibility

### **Performance Optimization**

**🚀 Database Optimization**
- Create indexes for frequently queried fields
- Implement connection pooling for production
- Consider MongoDB Atlas for cloud deployment

**🚀 Frontend Optimization**
- CSS files are already minified (comments removed)
- Static files served efficiently by Flask
- Responsive images and optimized loading

### **Production Deployment**

**🌐 Recommended Stack**
- **Web Server:** Gunicorn + Nginx
- **Database:** MongoDB Atlas (cloud)
- **Hosting:** AWS EC2, Heroku, or DigitalOcean
- **SSL:** Let's Encrypt for HTTPS

**🔧 Environment Variables**
```bash
# Create .env file for production
MONGODB_URI=mongodb://localhost:27017/
MAIL_USERNAME=your_email@gmail.com
MAIL_PASSWORD=your_app_password
SECRET_KEY=your_secret_key
```

---

## 🤝 Contributing

We welcome contributions to CardioInsight! Here's how you can help:

### **Development Guidelines**
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

### **Areas for Contribution**
- 🧠 **ML Model Improvements:** Add new algorithms or features
- 🎨 **UI/UX Enhancements:** Improve design and user experience
- 📊 **Data Visualization:** Add charts and analytics
- 🔒 **Security Features:** Enhance authentication and data protection
- 📱 **Mobile App:** React Native or Flutter implementation
- 🧪 **Testing:** Unit tests and integration tests

### **Code Standards**
- Follow PEP 8 for Python code
- Use semantic HTML and CSS best practices
- Add comments for complex logic
- Test thoroughly before submitting PRs

---

## 📋 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 📧 Support & Contact

- **Issues:** [GitHub Issues](https://github.com/your-username/cardioinsight/issues)
- **Email:** cardioinsight.support@example.com
- **Documentation:** [Project Wiki](https://github.com/your-username/cardioinsight/wiki)

---

## 📷 Application Screenshots

### 🏠 **Landing Page**
![Home Page - Modern ocean-themed interface with navigation and guest access](/Frontend/static/Images/home_screenshot.png)

### 🔐 **Authentication System**
![Login Page - Secure authentication with remember me functionality](/Frontend/static/Images/login_screenshot.png)
![Signup Page - User registration with email verification](/Frontend/static/Images/signup_screenshot.png)
![Forgot Password - Automated password recovery system](/Frontend/static/Images/forgot_screenshot.png)

### 🏥 **Health Assessment**
![Prediction Form - Comprehensive health metrics input](/Frontend/static/Images/predict_screenshot.png)
![Results Page - AI prediction with confidence scores](/Frontend/static/Images/result1.png)
![Detailed Results - In-depth analysis and recommendations](/Frontend/static/Images/result2.png)

### 👤 **User Dashboard**
![User Profile - Personal dashboard with prediction history](/Frontend/static/Images/user_profile1.png)
![Health History - Complete tracking of health assessments](/Frontend/static/Images/user_profile2.png)

### 📊 **Reports & Analytics**
![Health Report - Comprehensive analysis for medical consultation](/Frontend/static/Images/report1.png)
![Statistical Insights - Population health data and trends](/Frontend/static/Images/report2.png)

### 📚 **Educational Resources**
- **Cardiac Information:** Interactive learning about heart health
- **Prevention Guidelines:** Evidence-based lifestyle recommendations
- **Health Statistics:** Population-level insights and research data

---

**🎯 CardioInsight: Your AI-powered companion for heart health monitoring and prevention.**

**💙 Stay heart healthy, stay informed, stay protected.**