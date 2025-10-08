# Lab 6 — Introduction to Django and Flask Web Frameworks
---

## 🧩 Objective
This lab demonstrates building simple web applications using **Flask** and **Django** to understand routing, templating, and view handling.

---

## 🚀 How to Run Each App

### 🧠 Flask Application

**Folder:** `Flask_App/`

#### 1. Setup
```bash
cd Flask_App
python3 -m venv venv
source venv/bin/activate
pip install flask
```

#### 2. Run the App
```bash
python app.py
```

#### 3. Test in Browser
Open your browser and visit:
- `http://127.0.0.1:5000/` → Welcome page  
- `http://127.0.0.1:5000/hello/sai` → Dynamic greeting  
- `http://127.0.0.1:5000/form` → Form input page  

When you enter your name, Flask displays a personalized greeting.

---

### 🧱 Django Application

**Folder:** `Django_App/`

#### 1. Setup
```bash
cd Django_App
python3 -m venv venv
source venv/bin/activate
pip install django
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
```

#### 2. Run the Server
```bash
python manage.py runserver
```

#### 3. Test in Browser
Open your browser and visit:
- `http://127.0.0.1:8000/` → Homepage ("Hello from Django!")  
- `http://127.0.0.1:8000/greet/Sai/` → Dynamic greeting  
- `http://127.0.0.1:8000/messages/` → List of all Message objects  
- `http://127.0.0.1:8000/admin/` → Admin panel to add Message entries  

---

## 🧰 Summary of What Was Implemented

### Flask
- A lightweight app with:
  - **Home route** `/` → displays “Welcome to Flask!”
  - **Dynamic route** `/hello/<name>` → greets the user
  - **Form route** `/form` → takes user input and shows greeting using a Jinja2 template
- Templates used: `form.html`, `hello.html`

### Django
- Full-featured web app with:
  - **Homepage** `/` → “Hello from Django!”
  - **Dynamic greeting** `/greet/<name>/`
  - **Model:** `Message` with a text field
  - **Admin registration** to add and view messages
  - **Messages view** `/messages/` → lists all entries
  - Templates used: `index.html`, `greet.html`, `messages.html`



## 🧑‍💻 Tech Summary
| Framework | Type | Key Feature Used | Local URL |
|------------|------|------------------|------------|
| Flask | Lightweight | Routing, Templates, Forms | http://127.0.0.1:5000/ |
| Django | Full Framework | Models, Admin, Templates, Dynamic URLs | http://127.0.0.1:8000/ |

---

**End of README**

