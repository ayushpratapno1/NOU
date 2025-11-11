# E-Gyan Project - Online Learning Management System

![Django](https://img.shields.io/badge/Django-4.2.4-green.svg)
![Python](https://img.shields.io/badge/Python-3.x-blue.svg)
![Database](https://img.shields.io/badge/Database-SQLite3-lightgrey.svg)

## 📋 Project Overview

**E-Gyan** is a comprehensive web-based Learning Management System (LMS) built with Django. It facilitates online education by providing a platform where administrators can manage study materials, students can access educational resources, participate in Q&A forums, and submit feedback or complaints. The system is designed for educational institutions offering various programs, branches, and year levels.

## ✨ Key Features

### 🎓 For Students
- **User Registration & Authentication**: Secure student registration with roll number-based login
- **Profile Management**: View and manage personal profile information
- **Study Material Access**: Download course materials filtered by program, branch, and year
- **Q&A Forum**: Post questions and answer queries from fellow students
- **Feedback & Complaints**: Submit feedback or complaints to the administration
- **Password Management**: Change password securely
- **News Updates**: View latest news and announcements

### 👨‍💼 For Administrators
- **Student Management**: View all registered students and their details
- **Study Material Management**: Upload and manage study materials by program, branch, year, and subject
- **Enquiry Management**: View and manage enquiries from prospective students
- **Feedback & Complaint Tracking**: Monitor and respond to student feedback and complaints
- **News Management**: Post news and announcements for students
- **Dashboard**: Comprehensive admin dashboard for system oversight

### 🌐 Public Features
- **Home Page**: Overview of the learning platform
- **About Us**: Information about the institution
- **Contact/Enquiry Form**: Allow prospective students to submit enquiries
- **Login Portal**: Unified login for both students and administrators

## 🏗️ Project Structure

```
egyanproject/
├── adminapp/                    # Administrator module
│   ├── models.py               # Program, Branch, Year, Material, News models
│   ├── views.py                # Admin views and business logic
│   ├── adminappurls.py         # Admin URL routing
│   ├── templates/              # Admin HTML templates
│   └── static/                 # Admin static files (CSS, JS, images)
│
├── studentapp/                  # Student module
│   ├── models.py               # sturesponse, Question, Answer models
│   ├── views.py                # Student views and business logic
│   ├── studentappurls.py       # Student URL routing
│   ├── templates/              # Student HTML templates
│   └── static/                 # Student static files (CSS, JS, images)
│
├── nouapp/                      # Public/Common module (NOU - Nalanda Open University)
│   ├── models.py               # Student, Login, Enquiry models
│   ├── views.py                # Public views (index, login, registration)
│   ├── nouappurls.py           # Public URL routing
│   ├── templates/              # Public HTML templates
│   └── static/                 # Public static files (CSS, JS, images)
│
├── egyanproject/                # Main project configuration
│   ├── settings.py             # Django settings
│   ├── urls.py                 # Main URL configuration
│   ├── wsgi.py                 # WSGI configuration
│   └── asgi.py                 # ASGI configuration
│
├── media/                       # User-uploaded files (study materials)
├── db.sqlite3                   # SQLite database
└── manage.py                    # Django management script
```

## 📊 Database Schema

### Core Models

#### `Student` (nouapp)
- Roll Number (Primary Key)
- Name, Father's Name, Mother's Name
- Gender, Address
- Program, Branch, Year
- Contact Number, Email Address
- Registration Date

#### `Login` (nouapp)
- User ID (Primary Key) - Roll Number for students
- Password
- User Type (student/admin)
- Status (active/inactive)

#### `Material` (adminapp)
- ID (Auto-increment Primary Key)
- Program, Branch, Year, Subject
- File Name
- File Upload

#### `Question` & `Answer` (studentapp)
- Question ID (Auto-increment)
- Question Text/Answer Text
- Posted By/Answered By
- Posted Date

#### `sturesponse` (studentapp)
- Student Details (Roll Number, Name, Program, Branch, Year)
- Response Type (Feedback/Complaint)
- Subject, Response Text
- Response Date

#### `Enquiry` (nouapp)
- Name, Gender, Address
- Contact Number, Email Address
- Enquiry Text, Enquiry Date

#### `News` (adminapp)
- News ID (Auto-increment)
- News Text
- News Date

#### `Program`, `Branch`, `Year` (adminapp)
- Reference tables for academic structure

## 🔐 User Roles & Access Control

### Administrator
- Access URL: `/adminapp/`
- Can manage all students, materials, enquiries, feedback, and complaints
- Can post news and announcements
- Session-based authentication with cache control

### Student
- Access URL: `/studentapp/`
- Can view their profile and study materials
- Can post questions and answers
- Can submit feedback/complaints
- Can change password
- Session-based authentication with cache control

### Public/Guest
- Access URL: `/`
- Can view home page and about us
- Can register as new student
- Can submit enquiries
- Can login to access respective dashboards

## 🚀 Installation & Setup

### Prerequisites
- Python 3.x
- pip (Python package manager)
- Virtual environment (recommended)

### Installation Steps

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd egyanproject
   ```

2. **Create and activate virtual environment** (recommended)
   ```bash
   # Windows
   python -m venv venv
   venv\Scripts\activate

   # Linux/Mac
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install django==4.2.4
   ```

4. **Apply database migrations**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Create superuser for admin access**
   ```bash
   python manage.py createsuperuser
   ```

6. **Run the development server**
   ```bash
   python manage.py runserver
   ```

7. **Access the application**
   - Main Site: `http://127.0.0.1:8000/`
   - Django Admin: `http://127.0.0.1:8000/admin/`
   - Student Portal: `http://127.0.0.1:8000/studentapp/`
   - Admin Portal: `http://127.0.0.1:8000/adminapp/`

## 🔧 Configuration

### Database Configuration
The project uses SQLite3 by default (configured in `egyanproject/settings.py`):
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
```

For production, consider switching to PostgreSQL or MySQL.

### Media Files Configuration
User-uploaded files are stored in the `media/` directory:
```python
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
```

### Static Files Configuration
Static files are served from individual app directories:
```python
STATIC_URL = 'static/'
```

## 📱 Application Modules

### 1. NOU App (Public Module)
**Purpose**: Handles public-facing pages and authentication

**Key Views**:
- `index()` - Landing page with news
- `aboutus()` - About the institution
- `registration()` - Student registration
- `login()` - Unified login for students and admins
- `contactus()` - Enquiry submission

### 2. Admin App
**Purpose**: Administrative functions and content management

**Key Views**:
- `adminhome()` - Admin dashboard
- `viewstudent()` - View all registered students
- `studymaterial()` - Upload study materials
- `viewmaterial()` - View all materials
- `viewenquiry()` - View enquiries
- `viewfeedback()` - View student feedback
- `viewcomplain()` - View complaints
- `news()` - Post news/announcements
- `adminlogout()` - Admin logout

### 3. Student App
**Purpose**: Student-specific features and interactions

**Key Views**:
- `studenthome()` - Student dashboard
- `viewprofile()` - View personal profile
- `viewstudymaterial()` - Access study materials
- `postquestion()` - Post and view questions
- `postanswer()` - Answer questions
- `viewanswer()` - View answers to questions
- `response()` - Submit feedback/complaints
- `changepassword()` - Change account password
- `studentlogout()` - Student logout

## 🔒 Security Features

1. **Session Management**: User sessions are properly managed with Django's session framework
2. **Cache Control**: Implemented cache control decorators to prevent back-button access after logout
3. **CSRF Protection**: Django's CSRF middleware is enabled
4. **Password Validation**: Built-in Django password validators are configured
5. **Authentication Checks**: All protected views check for valid sessions before rendering

## 🎨 Frontend Technologies

- **HTML5**: Semantic markup
- **CSS3**: Custom stylesheets with Bootstrap integration
- **JavaScript**: Interactive functionality
- **Bootstrap**: Responsive design framework
- **SCSS**: Advanced styling with Sass preprocessing
- **Vendor Libraries**:
  - Chart.js (Data visualization)
  - Select2 (Enhanced select boxes)
  - jVectorMap (Map visualizations)
  - Owl Carousel (Image carousels)
  - CodeMirror (Code editing)
  - And many more...

## 📄 Templates Structure

### Public Templates (nouapp)
- `parent.html` - Base template
- `index.html` - Home page
- `aboutus.html` - About page
- `registration.html` - Student registration
- `login.html` - Login page
- `contactus.html` - Contact/Enquiry page

### Admin Templates (adminapp)
- `adminparent.html` - Admin base template
- `adminhome.html` - Admin dashboard
- `viewstudent.html` - Student list
- `studymaterial.html` - Upload materials
- `viewmaterial.html` - Material list
- `viewenquiry.html` - Enquiry list
- `viewfeedback.html` - Feedback list
- `viewcomplain.html` - Complaint list
- `news.html` - News management

### Student Templates (studentapp)
- `studentparent.html` - Student base template
- `studenthome.html` - Student dashboard
- `viewprofile.html` - Profile page
- `viewstudymaterial.html` - Study materials
- `postquestion.html` - Q&A forum
- `postanswer.html` - Answer form
- `viewanswer.html` - Answer list
- `response.html` - Feedback/Complaint form
- `changepassword.html` - Password change

## 🔄 Workflow

### Student Registration Flow
1. Visit registration page
2. Fill in personal and academic details
3. Select program, branch, and year
4. Submit registration
5. Account created with "inactive" status (pending admin approval)

### Study Material Management Flow
1. Admin logs in
2. Navigate to Study Material section
3. Upload file with program, branch, year, and subject details
4. Students can view and download materials based on their academic details

### Q&A Forum Flow
1. Student posts a question
2. Question appears in the forum for all students
3. Any student can post answers
4. Multiple answers can be provided for each question
5. Students can view all answers for a question

### Feedback/Complaint Flow
1. Student submits feedback or complaint with subject and details
2. Admin can view all feedback and complaints separately
3. Admin can take appropriate action

## 🚧 Known Limitations & Future Enhancements

### Current Limitations
- No email notification system
- Admin approval for student registration is not implemented
- No file type validation for study material uploads
- Limited search and filter functionality
- No real-time chat or messaging system

### Potential Enhancements
- **Email Integration**: Send notifications for registration, new materials, Q&A activity
- **Advanced Analytics**: Dashboard with charts and statistics
- **Assignment Module**: Allow submission and grading of assignments
- **Quiz System**: Online tests and assessments
- **Discussion Forums**: Threaded discussions beyond Q&A
- **Mobile App**: Native mobile applications
- **Video Lectures**: Integration with video streaming
- **Calendar**: Academic calendar and event management
- **Notification System**: Real-time notifications
- **Advanced Search**: Full-text search across materials and Q&A
- **API Development**: RESTful API for third-party integrations
- **Payment Gateway**: Integration for course fees
- **Certificate Generation**: Automated certificate issuance

## 🛠️ Troubleshooting

### Common Issues

**Issue**: Cannot run migrations
```bash
# Solution: Delete migration files and recreate
find . -path "*/migrations/*.py" -not -name "__init__.py" -delete
find . -path "*/migrations/*.pyc" -delete
python manage.py makemigrations
python manage.py migrate
```

**Issue**: Static files not loading
```bash
# Solution: Collect static files
python manage.py collectstatic
```

**Issue**: Session expired error
```bash
# Solution: Clear browser cache and cookies, then login again
```

## 📝 Development Notes

### Settings Configuration
- `DEBUG = True` - Currently set for development, must be set to `False` for production
- `SECRET_KEY` - Should be changed and kept secret in production
- `ALLOWED_HOSTS = []` - Must be configured with domain names in production

### Best Practices Followed
- Separation of concerns with multiple apps
- Template inheritance for consistent UI
- Session-based authentication
- Cache control for security
- Model-View-Template (MVT) architecture

## 👥 Contributing

Contributions are welcome! Please follow these steps:
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is developed for educational purposes. Please add appropriate license information based on your requirements.

## 📞 Contact & Support

For questions, issues, or suggestions, please:
- Open an issue on the repository
- Contact the development team
- Refer to Django documentation: https://docs.djangoproject.com/

## 🙏 Acknowledgments

- Built with Django Framework
- Uses Bootstrap for responsive design
- Various open-source libraries and components
- Inspired by modern Learning Management Systems

---

**Note**: This is an educational project. For production deployment, please ensure proper security measures, testing, and configuration are in place.

**Version**: 1.0  
**Last Updated**: November 2025  
**Django Version**: 4.2.4  
**Python Version**: 3.x

