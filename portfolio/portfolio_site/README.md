# Portfolio Site – Shanib Khan

## Overview
A **modern Django-based personal portfolio** featuring 3D CSS animations, glassmorphism effects, and a multi-page structure with About, Projects, Skills, and Contact sections.

## Features
- 🎨 Modern, responsive design with glassmorphism effects
- 🎭 3D CSS animations and hover effects
- 📱 Fully responsive layout for all devices
- 🌐 Multi-page structure (Home, About, Projects, Skills, Contact)
- 🎯 Interactive project cards with 3D flip animations
- 📊 Skills progress bars with smooth animations
- 🎨 Gradient backgrounds and modern color scheme
- ⚡ Fast performance with optimized CSS

## Directory Structure
```
portfolio_site/
├─ manage.py
├─ portfolio/                # Django project settings
│   ├─ __init__.py
│   ├─ settings.py
│   ├─ urls.py
│   ├─ wsgi.py
│   └─ asgi.py
├─ main/                    # Core app
│   ├─ __init__.py
│   ├─ apps.py
│   ├─ views.py
│   ├─ urls.py
│   └─ templates/main/
│       ├─ base.html
│       ├─ index.html
│       ├─ about.html
│       ├─ projects.html
│       ├─ skills.html
│       └─ contact.html
├─ static/                  # Static files
│   ├─ css/style.css
│   ├─ js/main.js
│   └─ images/
├─ db.sqlite3               # SQLite DB (auto-created)
└─ README.md                # This documentation
```

## Setup Instructions
```bash
# 1. Enter the project directory
cd /a0/usr/workdir/portfolio_site

# 2. Install Django
pip install django

# 3. Apply migrations (creates SQLite DB)
python manage.py migrate

# 4. Run the development server
python manage.py runserver 0.0.0.0:8000
```

Open a browser at `http://localhost:8000/` or `http://host.docker.internal:8000/` to view the portfolio.

## Pages
- **Home**: Hero section with 3D card effect and featured expertise
- **About**: Personal background with statistics and 3D profile card
- **Projects**: Interactive project cards with 3D flip animations
- **Skills**: Progress bars for programming languages, data tools, web technologies, and machine learning
- **Contact**: Contact form and social media links

## Technologies Used
- **Backend**: Django, Python
- **Frontend**: HTML5, CSS3, JavaScript
- **Styling**: Custom CSS with 3D transforms, gradients, and animations
- **Icons**: Font Awesome
- **Database**: SQLite (can be switched to MySQL)

## Customization
Edit the following files to customize the portfolio:
- `main/templates/main/*.html`: Update content and structure
- `static/css/style.css`: Modify colors, fonts, and animations
- `static/js/main.js`: Add custom JavaScript functionality

## License
MIT License - feel free to use this template for your own portfolio.

---
*Created by Agent Zero for Shanib Khan*
