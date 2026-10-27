<div align="center">

# 📚 E-Gyan — Online Learning Management System

**A full-featured LMS built with Django, deployed on Render, backed by Neon PostgreSQL.**

[![Live Demo](https://img.shields.io/badge/🚀_Live_Demo-egyanproject.onrender.com-4F46E5?style=for-the-badge)](https://egyanproject.onrender.com/)
[![Django](https://img.shields.io/badge/Django-6.0.2-092E20?style=for-the-badge&logo=django&logoColor=white)](https://www.djangoproject.com/)
[![Python](https://img.shields.io/badge/Python-3.14.7-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Neon-336791?style=for-the-badge&logo=postgresql&logoColor=white)](https://neon.tech/)
[![Cloudinary](https://img.shields.io/badge/Cloudinary-Media_CDN-3448C5?style=for-the-badge&logo=cloudinary&logoColor=white)](https://cloudinary.com/)
[![Render](https://img.shields.io/badge/Render-Deployed-46E3B7?style=for-the-badge&logo=render&logoColor=white)](https://render.com/)

</div>

---

## 📖 Overview

**E-Gyan** is a comprehensive web-based Learning Management System (LMS) built for educational institutions offering various programs, branches, and year levels — specifically tailored for **Nalanda Open University (NOU)**. It provides a unified platform for administrators to manage academic content and for students to access study materials, participate in Q&A forums, and submit feedback.

---

## 🌐 Live Demo

> **Production URL**: [https://egyanproject.onrender.com/](https://egyanproject.onrender.com/)

| Portal | URL |
|--------|-----|
| 🏠 Home | `/` |
| 🎓 Student Login | `/studentapp/` |
| 🔧 Admin Portal | `/adminapp/` |
| ⚙️ Django Admin | `/admin/` |

---

## ✨ Features

### 🎓 Student Portal
- Secure roll number-based registration & login
- Personal profile management
- Study material download (filtered by program, branch & year)
- Community Q&A forum (post questions & answers)
- Feedback & complaint submission
- Secure password change

### 👨‍💼 Admin Portal
- Dashboard with full system overview
- Student management (view all registered students)
- Study material upload & management (by program / branch / year / subject)
- Enquiry, feedback & complaint tracking
- News & announcements management

### 🌍 Public Pages
- Landing page with latest news/announcements
- About Us page
- Student registration form
- Contact / Enquiry form

---

## 🏗️ Tech Stack

### Backend
| Component | Local (Development) | Production |
|-----------|-------------------|------------|
| **Framework** | Django 6.0.2 | Django 6.0.2 |
| **Database** | SQLite 3 | Neon PostgreSQL (via `dj-database-url`) |
| **Media Storage** | FileSystem (`/media/`) | Cloudinary CDN |
| **Static Files** | Django StaticFiles | WhiteNoise (Compressed Manifest) |
| **WSGI Server** | `python manage.py runserver` | Gunicorn |
| **Deployment** | Local | Render (Free Tier) |

### Frontend
- **HTML5** + **CSS3** + **JavaScript**
- **Bootstrap** — Responsive layout
- **Chart.js** — Data visualization
- **Select2**, **Owl Carousel**, **jVectorMap**
- **SCSS** — Advanced styling

---

## 📁 Project Structure

```
egyanproject/
├── nouapp/                     # 🌍 Public module (home, login, registration, enquiry)
│   ├── models.py               #    Student, Login, Enquiry models
│   ├── views.py                #    Public-facing views
│   ├── nouappurls.py           #    URL routing
│   └── templates/ & static/
│
├── adminapp/                   # 🔧 Admin module
│   ├── models.py               #    Program, Branch, Year, Material, News models
│   ├── views.py                #    Admin views and business logic
│   ├── adminappurls.py         #    URL routing
│   └── templates/ & static/
│
├── studentapp/                 # 🎓 Student module
│   ├── models.py               #    sturesponse, Question, Answer models
│   ├── views.py                #    Student views and business logic
│   ├── studentappurls.py       #    URL routing
│   └── templates/ & static/
│
├── egyanproject/               # ⚙️ Project configuration
│   ├── settings.py             #    Environment-aware settings
│   ├── urls.py                 #    Root URL dispatcher
│   ├── wsgi.py & asgi.py
│
├── media/                      # 📂 Local media uploads (dev only)
├── staticfiles/                # 📦 Collected static files (production)
├── build.sh                    # 🔨 Render build script
├── render.yaml                 # 🚀 Render deployment config
├── create_superuser.py         # 👤 Auto superuser creation script
├── requirements.txt
├── manage.py
└── db.sqlite3                  # 🗄️ Local dev database
```

---

## 📊 Data Models

| Model | App | Key Fields |
|-------|-----|------------|
| `Student` | `nouapp` | Roll Number (PK), Name, Father/Mother Name, Gender, Program, Branch, Year, Contact, Email |
| `Login` | `nouapp` | User ID (PK), Password, User Type (`student`/`admin`), Status |
| `Enquiry` | `nouapp` | Name, Contact, Email, Enquiry Text, Date |
| `Program` / `Branch` / `Year` | `adminapp` | Reference/lookup tables for academic structure |
| `Material` | `adminapp` | Program, Branch, Year, Subject, File |
| `News` | `adminapp` | News Text, Date |
| `Question` / `Answer` | `studentapp` | Text, Posted By, Date |
| `sturesponse` | `studentapp` | Roll No, Name, Response Type (Feedback/Complaint), Subject, Text, Date |

---

## 🔐 Access Control

| Role | Session Key | Capabilities |
|------|-------------|--------------|
| **Admin** | `admin_session` | Full CRUD on materials, students, news; view enquiries/feedback/complaints |
| **Student** | `student_session` | View profile & materials, post Q&A, submit feedback, change password |
| **Guest** | — | View home/about, register, submit enquiry |

All protected views enforce session checks and use Django's cache-control decorators to prevent back-button access after logout.

---

## 🚀 Local Development Setup

### Prerequisites
- Python 3.14.7
- `pip`
- Git

### Steps

**1. Clone the repository**
```bash
git clone https://github.com/ayushpratapno1/NOU
cd NOU
```

**2. Create and activate a virtual environment**
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux / macOS
python3 -m venv venv
source venv/bin/activate
```

**3. Install dependencies**
```bash
pip install -r requirements.txt
```

**4. Configure environment variables**

Create a `.env` file in the project root:
```env
SECRET_KEY=your-local-secret-key
DEBUG=True
# Leave DATABASE_URL unset to use SQLite automatically
# Leave CLOUDINARY_* unset to use local filesystem storage
```

**5. Apply migrations**
```bash
python manage.py makemigrations
python manage.py migrate
```

**6. Create a superuser**
```bash
python manage.py createsuperuser
```

**7. Start the development server**
```bash
python manage.py runserver
```

**8. Open in browser**
- Home: `http://127.0.0.1:8000/`
- Student Portal: `http://127.0.0.1:8000/studentapp/`
- Admin Portal: `http://127.0.0.1:8000/adminapp/`
- Django Admin: `http://127.0.0.1:8000/admin/`

> **Media files** in local development are stored in the `media/` directory via Django's `FileSystemStorage`.

---

## ☁️ Production Deployment (Render + Neon + Cloudinary)

### Architecture

```
Browser ──► Render Web Service (Gunicorn)
                │
                ├── Static files ──► WhiteNoise (served inline)
                ├── Media files  ──► Cloudinary CDN
                └── Database     ──► Neon PostgreSQL (SSL)
```

### Render Setup

The project includes a [`render.yaml`](render.yaml) for zero-config deploys on Render.

**Required environment variables** (set in Render dashboard or `render.yaml`):

| Variable | Description |
|----------|-------------|
| `SECRET_KEY` | Django secret key (auto-generated by Render) |
| `DEBUG` | Must be `False` in production |
| `PRODUCTION` | Set to `True` to enable HTTPS/HSTS security settings |
| `DATABASE_URL` | Neon PostgreSQL connection string (e.g. `postgres://user:pass@host/db?sslmode=require`) |
| `ALLOWED_HOSTS` | Auto-set from Render's `RENDER_EXTERNAL_HOSTNAME` |
| `CLOUDINARY_CLOUD_NAME` | Your Cloudinary cloud name |
| `CLOUDINARY_API_KEY` | Your Cloudinary API key |
| `CLOUDINARY_API_SECRET` | Your Cloudinary API secret |
| `SUPERUSER_USERNAME` | Initial superuser username |
| `SUPERUSER_EMAIL` | Initial superuser email |
| `SUPERUSER_PASSWORD` | Initial superuser password |

### Build Script ([`build.sh`](build.sh))

Render runs this automatically on every deploy:
```bash
pip install -r requirements.txt     # Install dependencies
python manage.py collectstatic       # Build static file manifest
python manage.py migrate             # Apply DB migrations
python create_superuser.py           # Create superuser (idempotent)
```

### How Environment Switching Works

The settings file in [`egyanproject/settings.py`](egyanproject/settings.py) automatically detects the environment:

```python
# Database: SQLite locally, Neon PostgreSQL in production
DATABASES = {
    "default": dj_database_url.config(
        default=f"sqlite:///{BASE_DIR / 'db.sqlite3'}",  # fallback
        conn_max_age=60,
        ssl_require=bool(os.getenv("DATABASE_URL")),
    )
}

# Storage: FileSystem locally, Cloudinary in production
if DEBUG:
    STORAGES = {"default": {"BACKEND": "django.core.files.storage.FileSystemStorage"}}
else:
    STORAGES = {"default": {"BACKEND": "cloudinary_storage.storage.MediaCloudinaryStorage"}}
```

### Production Security Settings (`PRODUCTION=True`)

- `SECURE_SSL_REDIRECT = True`
- `SESSION_COOKIE_SECURE = True`
- `CSRF_COOKIE_SECURE = True`
- `SECURE_HSTS_SECONDS = 31536000` (1 year)
- `SECURE_HSTS_INCLUDE_SUBDOMAINS = True`
- `SECURE_HSTS_PRELOAD = True`

---

## 🔄 Application Workflows

### Student Registration
```
Register → Fill profile & academic details → Account created (inactive)
→ Admin activates → Student can log in
```

### Study Material Upload
```
Admin login → Study Material → Upload file with Program/Branch/Year/Subject
→ Students filter & download by their academic details
```

### Q&A Forum
```
Student posts question → Visible to all students
→ Any student answers → Multiple answers per question supported
```

---

## 🛡️ Security Highlights

| Feature | Implementation |
|---------|----------------|
| Session auth | Custom session keys (`admin_session`, `student_session`) |
| Back-button prevention | `cache_control(no_cache=True, must_revalidate=True)` decorator |
| CSRF protection | Django `CsrfViewMiddleware` |
| Password validation | Django's built-in validators |
| HTTPS enforcement | `SECURE_SSL_REDIRECT` in production |
| Secure cookies | `SESSION_COOKIE_SECURE`, `CSRF_COOKIE_SECURE` |
| HSTS | 1-year preload-ready HSTS header |

---

## 🛠️ Troubleshooting

**Migration errors**
```bash
find . -path "*/migrations/*.py" -not -name "__init__.py" -delete
python manage.py makemigrations
python manage.py migrate
```

**Static files not loading locally**
```bash
python manage.py collectstatic
```

**Session expired / redirected to login**
Clear browser cookies and cache, then log in again.

**Cloudinary upload errors**
Ensure `CLOUDINARY_CLOUD_NAME`, `CLOUDINARY_API_KEY`, and `CLOUDINARY_API_SECRET` are set correctly in your environment.

**Neon DB connection issues**
Make sure `DATABASE_URL` includes `?sslmode=require` and matches your Neon project's connection string.

---

## 🗺️ Roadmap

- [ ] Email notifications (registration, new materials, Q&A activity)
- [ ] Admin approval workflow for student registration
- [ ] File type & size validation on uploads
- [ ] Assignment submission & grading module
- [ ] Online quiz / assessment system
- [ ] Full-text search across materials and Q&A
- [ ] REST API for third-party integrations
- [ ] Real-time notifications
- [ ] Mobile-responsive redesign
- [ ] Academic calendar & event management

---

## 👥 Contributing

Contributions are welcome!

1. Fork the repository
2. Create your feature branch: `git checkout -b feature/your-feature`
3. Commit your changes: `git commit -m 'feat: add your feature'`
4. Push to the branch: `git push origin feature/your-feature`
5. Open a Pull Request

---

## 📄 License

This project is developed for educational purposes. Please add an appropriate license based on your requirements.

---

## 🙏 Acknowledgments

- [Django](https://www.djangoproject.com/) — Web framework
- [Render](https://render.com/) — Cloud deployment platform
- [Neon](https://neon.tech/) — Serverless PostgreSQL
- [Cloudinary](https://cloudinary.com/) — Media CDN & storage
- [WhiteNoise](https://whitenoise.readthedocs.io/) — Static file serving
- [Bootstrap](https://getbootstrap.com/) — UI framework

---

<div align="center">

**Version**: 1.0 &nbsp;|&nbsp; **Django**: 6.0.2 &nbsp;|&nbsp; **Python**: 3.14.7 &nbsp;|&nbsp; **Last Updated**: October 2026

</div>
