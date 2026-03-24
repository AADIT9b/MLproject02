# Deployment Guide

## ✅ Production Deployment Checklist

### Local Testing (Before Deployment)
```bash
# Load environment
python -m venv venv
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Test with Gunicorn (production server)
gunicorn --workers 4 --bind 0.0.0.0:5000 app:app
```

### Azure App Service / Cloud Deployment

**Changes Made for Deployment:**
✅ `debug=False` - Disabled debug mode  
✅ `0.0.0.0` - Listens on all interfaces (not just localhost)  
✅ Environment variables - PORT and FLASK_DEBUG configurable  
✅ Remove print statements - Clean logs  
✅ gunicorn in requirements.txt - Production WSGI server  

**Next Steps:**

1. **Create `Procfile` for cloud deployment:**
```
web: gunicorn --workers 4 --worker-class sync --timeout 180 --bind 0.0.0.0:$PORT app:app
```

2. **Deploy to Azure App Service:**
```bash
az webapp up --name your-app-name --resource-group your-resource-group --runtime python:3.9 --sku B1
```

3. **Or deploy to Heroku:**
```bash
heroku create your-app-name
git push heroku main
```

### Important Security Notes:
- Never commit `.env` with real secrets
- Set `FLASK_SECRET_KEY` in production environment
- Add CORS headers if needed
- Use SSL/TLS (HTTPS)
- Log all errors properly
- Validate all user inputs

### Model Files:
Ensure `artifacts/model.pkl` and `artifacts/preprocessor.pkl` exist before deployment!

---
Ready to deploy! 🚀
