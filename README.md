EduBridge - Online Learning Platform

EduBridge is a comprehensive Django-based E-Learning system designed to bridge the gap between students and expert mentors. It provides a secure, visually appealing, and functional environment for course management, student enrollment, and academic tracking.

Live Demo: mdshahadathossainit.pythonanywhere.com

📸 Screenshots

🏠 Home & Discovery

<p align="center">
<img src="https://www.google.com/search?q=https://i.imgur.com/W89g7ZU.png" width="400" alt="Home Page 1"/>
<img src="https://www.google.com/search?q=https://i.imgur.com/YGHUwha.png" width="400" alt="Home Page 2"/>
</p>

📚 Course & Mentors

<p align="center">
<img src="https://www.google.com/search?q=https://i.imgur.com/k6HhOXq.png" width="45% " alt="Course List"/>
<img src="https://www.google.com/search?q=https://i.imgur.com/GdeOd53.png" width="45%" alt="Teacher List"/>
</p>

👨‍🏫 Teacher Experience

<p align="center">
<img src="https://www.google.com/search?q=https://i.imgur.com/GdP4B7t.png" width="30%" alt="Teacher Details"/>
<img src="https://www.google.com/search?q=https://i.imgur.com/Ubx0GFD.png" width="30%" alt="Teacher Profile"/>
<img src="https://www.google.com/search?q=https://i.imgur.com/JqkeHS4.png" width="30%" alt="Teacher Dashboard"/>
</p>

🎓 Student Experience

<p align="center">
<img src="https://www.google.com/search?q=https://i.imgur.com/eTHZ2qY.png" width="850" alt="Student Dashboard"/>
</p>

🔐 Authentication & Security

<p align="center">
<img src="https://www.google.com/search?q=https://i.imgur.com/PHggkLk.png" width="45%" alt="Login Page"/>
<img src="https://www.google.com/search?q=https://i.imgur.com/OSSDGYY.png" width="45%" alt="Signup Page"/>
</p>

⚙️ Administration

<p align="center">
<img src="https://www.google.com/search?q=https://i.imgur.com/U8baQkF.png" width="850" alt="Admin Panel"/>
</p>

✨ Key Features

For Students

Course Exploration: Browse through a wide variety of courses with detailed curricula.

One-Click Enrollment: Seamless enrollment process for authenticated students.

Personal Dashboard: Track enrolled courses, view progress, and check pending homework.

Profile Management: Update personal information and profile pictures.

For Teachers

Course Creation: Dedicated interface to upload and manage course content.

Homework Assignment: Ability to assign tasks to specific courses with due dates.

Analytics Dashboard: Monitor the number of students enrolled in each class.

Professional Profiles: Public profile pages showcasing bio, subject expertise, and ratings.

For Administrators

Advanced Control Center: Manage users, teachers, students, and site-wide settings.

Success Stories: Manage and display student success stories on the homepage.

UI Customization: Update slideshow images and site logos through the admin panel.

🛠️ Technologies Used

Backend: Python 3.x, Django Framework

Frontend: HTML5, CSS3 (Custom Glassmorphism), JavaScript, Bootstrap 5

Database: SQLite (Development)

Icons & UI: FontAwesome 6.4, Google Fonts (Plus Jakarta Sans)

Authentication: Django Auth System (Custom Signals for Profile creation)

🚀 Installation and Setup

Clone the repository:

git clone [https://github.com/mdshahadathossainit/edubridge-project.git](https://github.com/mdshahadathossainit/edubridge-project.git)
cd edubridge-project


Create and activate a virtual environment:

python -m venv venv
# Windows:
venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate


Install dependencies:

pip install -r requirements.txt


Database Setup:

python manage.py makemigrations
python manage.py migrate


Create Admin User:

python manage.py createsuperuser


Run Server:

python manage.py runserver
