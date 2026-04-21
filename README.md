
# 🎓 EduBridge - Online Learning Platform

EduBridge is a comprehensive Django-based E-Learning system designed to bridge the gap between students and expert mentors. It provides a secure, visually appealing, and functional environment for course management, student enrollment, and academic tracking.

🌐 **Live Demo:** [mdshahadathossainit.pythonanywhere.com](https://mdshahadathossainit.pythonanywhere.com/)

---

## 🖼️ Project Screenshots

### 🖥️ Main Interfaces
| **Admin Dashboard** | **Course List** |
| :---: | :---: |
| <img src="https://i.imgur.com/eshRriC.jpg" width="350" alt="Admin Page"/> | <img src="https://i.imgur.com/tOrToF3.jpg" width="350" alt="Course List Page"/> |

### 🏠 Landing Page (Mobile/Responsive View)
<p align="center">
  <img src="https://i.imgur.com/AEYKFTl.jpg" width="180" alt="Home Page 1"/> 
  <img src="https://i.imgur.com/A0aV2KE.jpg" width="180" alt="Home Page 2"/>
</p>

### 🔐 Authentication & Profiles
| **Login Page** | **Signup Page** |
| :---: | :---: |
| <img src="https://i.imgur.com/ndiTgfY.jpg" width="350" alt="Login Page"/> | <img src="https://i.imgur.com/R48deOZ.jpg" width="350" alt="Signup Page"/> |

| **Teacher List** | **Teacher Details** |
| :---: | :---: |
| <img src="https://i.imgur.com/5aS94Nz.jpg" width="350" alt="Teacher List"/> | <img src="https://i.imgur.com/VeF8UYL.jpg" width="350" alt="Teacher Details"/> |

### 📊 User Dashboards
| **Teacher Dashboard (1)** | **Teacher Dashboard (2)** |
| :---: | :---: |
| <img src="https://i.imgur.com/BuUatQG.jpg" width="350" alt="Teacher Dashboard 1"/> | <img src="https://i.imgur.com/TokeTAI.jpg" width="350" alt="Teacher Dashboard 2"/> |

<p align="center">
  <b>Student Profile / Dashboard</b><br>
  <img src="https://i.imgur.com/IYzIGVk.jpg" width="400" alt="Student Dashboard"/>
</p>

---

## ✨ Key Features

* **Multi-Role Dashboards:** Separate, tailored experiences for Students, Teachers, and Admins.
* **Automatic Profile Creation:** Uses Django **Signals** to create Teacher/Student profiles instantly upon registration.
* **Course Management:** Teachers can create courses, and students can enroll with a single click.
* **Homework System:** Teachers can post homework to specific courses; students see them on their personal dashboard.
* **Glassmorphism UI:** Modern, clean, and responsive design using **Bootstrap 5** and custom CSS.
* **Site Management:** Administrators can update logos, slideshows, and site names directly from the Admin UI.

---

## 🛠️ Technologies Used

### **Backend**
* **Python 3.x**
* **Django Framework:** The core web framework.
* **Django-extensions:** For advanced management commands and graphing.
* **Pillow:** For image processing and thumbnails.

### **Frontend**
* **HTML5 & CSS3:** With custom Glassmorphism effects.
* **Bootstrap 5:** For responsive layouts and UI components.
* **JavaScript:** For dynamic UI interactions.
* **FontAwesome 6.4:** For high-quality iconography.
* **Google Fonts:** (Plus Jakarta Sans).

### **Database & Security**
* **SQLite:** Used for development data storage.
* **Django Auth:** Secure login, registration, and password management.

---

## 📁 Project Structure

```text
└── mdshahadathossainit-edubridge-project/
    ├── courses/            # Course management and enrollment logic
    │   ├── templates/      # Course-related HTML templates
    │   ├── admin.py        # Course & Homework admin configuration
    │   ├── forms.py        # Course & Homework assignment forms
    │   ├── models.py       # Course, Enrollment, Homework schemas
    │   ├── urls.py         # Course app routing
    │   └── views.py        # Logic for course list, detail, and homework
    ├── edubridge/          # Core project settings and configuration
    │   ├── settings.py     # Global settings (Database, Apps, Media)
    │   ├── urls.py         # Master routing
    │   └── wsgi.py
    ├── media/              # User-uploaded files (Course thumbnails, Profile pics)
    ├── members/            # Teacher/Student profile and site settings logic
    │   ├── templates/      # Landing page and teacher profile templates
    │   ├── admin.py        # Custom Teacher/Student admin panels
    │   ├── models.py       # Site settings and Success Story schemas
    │   └── views.py        # Logic for landing page and profiles
    ├── users/              # Authentication and account management
    │   ├── templates/      # Login, Register, Dashboards templates
    │   ├── signals.py      # Profile auto-creation logic
    │   └── views.py        # Multi-role dashboard logic (Admin/Teacher/Student)
    ├── manage.py
    ├── requirements.txt
    └── README.md
```

---

## 🚀 Installation and Setup

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/mdshahadathossainit/edubridge-project.git](https://github.com/mdshahadathossainit/edubridge-project.git)
   cd edubridge-project
   ```

2. **Virtual Environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```

3. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Database Migration:**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Run Server:**
   ```bash
   python manage.py runserver
   ```

---

## 📩 Contact

**Md Shahadat Hossain** *Software Developer | AI/ML Researcher*

* **GitHub:** [@mdshahadathossainit](https://github.com/mdshahadathossainit)
* **Live Site:** [EduBridge Learning Hub](https://mdshahadathossainit.pythonanywhere.com/)
```
