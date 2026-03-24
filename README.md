# 📊 Student Exam Performance Indicator

A machine learning web application that predicts student math scores based on various educational and demographic factors. Built with Flask and scikit-learn, this project provides an intuitive interface for predicting exam performance.

## 🎯 Features

- **Accurate Predictions**: Uses trained ML models to predict math scores
- **Beautiful UI**: Modern, responsive design with gradient backgrounds
- **Input Validation**: Comprehensive client-side and server-side validation
- **Error Handling**: Robust exception handling with user-friendly error messages
- **Production Ready**: Configured for cloud deployment (Azure, Heroku, AWS, GCP)
- **Real-time Results**: Instant predictions with formatted output

## 📋 Requirements

### Input Features
- **Gender**: Male / Female
- **Race/Ethnicity**: Group A, B, C, D, or E
- **Parental Education Level**: High School, Some College, Bachelor's, Master's Degree
- **Lunch Type**: Standard or Free/Reduced
- **Test Preparation Course**: Completed or None
- **Reading Score**: 0-100
- **Writing Score**: 0-100

### Output
- **Predicted Math Score**: Float value representing estimated math performance

## 🚀 Quick Start

### Installation

1. **Clone the repository**:
```bash
git clone <your-repo-url>
cd mlprojects
```

2. **Create virtual environment**:
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python -m venv venv
source venv/bin/activate
```

3. **Install dependencies**:
```bash
pip install -r requirements.txt
```

### Running Locally

**Development mode**:
```bash
python app.py
```
Visit: `http://localhost:5000`

**Production mode** (using Gunicorn):
```bash
gunicorn --workers 4 --bind 0.0.0.0:5000 app:app
```

## 📁 Project Structure

```
mlprojects/
├── app.py                          # Flask application entry point
├── requirements.txt                # Python dependencies
├── Procfile                        # Heroku deployment config
├── .env                            # Environment variables
├── README.md                       # This file
├── DEPLOYMENT.md                   # Detailed deployment guide
│
├── src/
│   ├── __init__.py
│   ├── exception.py               # Custom exception handling
│   ├── logger.py                  # Logging configuration
│   ├── utils.py                   # Utility functions
│   │
│   ├── components/
│   │   ├── data_ingestion.py      # Data loading
│   │   ├── data_transformation.py # Data preprocessing
│   │   └── model_trainer.py       # Model training
│   │
│   └── pipeline/
│       ├── train_pipeline.py      # Training workflow
│       └── predict_pipeline.py    # Prediction workflow
│
├── templates/
│   ├── home.html                  # Prediction form & results
│   └── index.html                 # Home page
│
├── artifacts/
│   ├── model.pkl                  # Trained ML model
│   └── preprocessor.pkl           # Data preprocessor/scaler
│
├── notebook/
│   ├── 1 . EDA STUDENT PERFORMANCE .ipynb
│   └── 2. MODEL TRAINING.ipynb
│
└── logs/                           # Application logs
```

## 🔧 Technology Stack

| Component | Technology |
|-----------|-----------|
| **Backend** | Flask (Python) |
| **ML Models** | scikit-learn, CatBoost, XGBoost |
| **Data Processing** | Pandas, NumPy |
| **Server** | Gunicorn |
| **Frontend** | HTML5, CSS3 (Responsive Design) |
| **Deployment** | Docker, Heroku, Azure App Service |

## 🛡️ Validation & Error Handling

### Frontend Validation
- HTML5 input constraints (min/max for scores)
- Required field validation
- Dropdown selections for categorical data

### Backend Validation
- **Score Range Check**: Reading & Writing scores must be 0-100
- **Custom Exceptions**: Detailed error messages with file & line info
- **Error Logging**: All errors logged with timestamps
- **Graceful Fallback**: User-friendly error messages

## 📊 Model Information

The application uses ensemble models trained on student performance data:
- **Primary Models**: CatBoost, XGBoost, scikit-learn estimators
- **Preprocessing**: StandardScaler for feature normalization
- **Accuracy**: Validated on test dataset

*Trained models are located in `artifacts/` directory*

## 🌐 Deployment

### Option 1: Heroku (Free Tier Available)
```bash
heroku login
heroku create your-app-name
git push heroku main
heroku open
```

### Option 2: Azure App Service
```bash
az login
az webapp up --name your-app-name --resource-group myresourcegroup --runtime python:3.9 --sku B1
```

### Option 3: Docker
```bash
docker build -t mlapp .
docker run -p 5000:5000 mlapp
```

**For detailed deployment instructions**, see [DEPLOYMENT.md](DEPLOYMENT.md)

## 📝 Environment Variables

Create a `.env` file in root directory:
```env
FLASK_DEBUG=False          # Set to True for development only
PORT=5000                  # Server port
FLASK_ENV=production       # Set to development for debug mode
```

## 🔍 How It Works

1. **User Input**: Fill the form with student information
2. **Validation**: Server validates all inputs (scores 0-100)
3. **Processing**: Data is preprocessed using StandardScaler
4. **Prediction**: ML models generate score prediction
5. **Display**: Result shown with formatted output

## 🧪 Testing

Test the application locally:
```bash
# Run with valid data
# Expected: Prediction displayed in green

# Run with invalid score (>100)
# Expected: Error message in red, no prediction
```

## 📚 Notebooks

Data exploration and model training notebooks available:
- `1 . EDA STUDENT PERFORMANCE .ipynb` - Exploratory Data Analysis
- `2. MODEL TRAINING.ipynb` - Model training & evaluation

## ⚠️ Important Notes

1. **Model Files Required**: Ensure `artifacts/model.pkl` and `artifacts/preprocessor.pkl` exist
2. **Production Settings**: 
   - Set `FLASK_DEBUG=False` in production
   - Use Gunicorn or similar WSGI server
   - Configure proper logging
3. **Security**:
   - Never commit `.env` with secrets
   - Use environment variables for sensitive data
   - Validate all user inputs (already implemented)

## 🤝 Contributing

Contributions are welcome! Please:
1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## 📄 License

This project is licensed under the MIT License

## 📞 Support

For deployment help, see [DEPLOYMENT.md](DEPLOYMENT.md)  
For issues, check error logs in `logs/` directory

## 🎓 Learning Outcomes

This project demonstrates:
- ✅ Flask web application development
- ✅ ML model deployment
- ✅ Exception handling & logging
- ✅ Form validation (client & server-side)
- ✅ Cloud deployment (Heroku, Azure, Docker)
- ✅ Production-ready code practices

---

**Status**: ✅ Ready for Deployment  
**Last Updated**: March 2026  
**Version**: 1.0.0