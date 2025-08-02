# FlaskAuth Pro 🚀

> Modern Flask authentication with Google OAuth and stunning UI design.

A production-ready authentication system combining Flask backend with Google OAuth 2.0, featuring a beautiful glassmorphism interface with smooth animations.

## ✨ Features

- 🔐 **Google OAuth 2.0** - Secure authentication
- 🎨 **Modern UI** - Glassmorphism design with animations
- 📱 **Responsive** - Works on all devices
- ⚡ **Fast** - Optimized performance
- 🛡️ **Secure** - Environment variables and best practices

## 🚀 Quick Start

1. **Clone and install**
   ```bash
   git clone https://github.com/AliiAssi/AuthFlow.git
   cd AuthFlow
   pip install -r requirements.txt
   ```

2. **Set up Google OAuth**
   - Go to [Google Cloud Console](https://console.cloud.google.com/)
   - Create OAuth 2.0 credentials
   - Add authorized origins: `http://localhost:5000`

3. **Configure environment**
   ```bash
   cp .env.example .env
   ```
   
   Edit `.env`:
   ```env
   GOOGLE_CLIENT_ID=your-google-client-id
   FLASK_SECRET_KEY=your-secret-key
   FLASK_ENV=development
   ```

4. **Run**
   ```bash
   python app.py
   ```

Visit `http://localhost:5000`

## 📁 Structure

```
flaskauth-pro/
├── app.py              # Main Flask app
├── requirements.txt    # Dependencies
├── templates/login.html# Login page
├── .env.example       # Environment template
└── README.md          # Documentation
```

## 🔧 API Endpoints

- `GET /` - Login page
- `POST /google-login` - OAuth callback
- `GET /dashboard` - Protected route

## 🚀 Deploy

Update `.env` for production:
- Set `FLASK_ENV=production`
- Use HTTPS URLs for OAuth
- Generate strong `FLASK_SECRET_KEY`

Compatible with Heroku, Vercel, AWS, DigitalOcean.


---

**Made with ❤️ for developers**