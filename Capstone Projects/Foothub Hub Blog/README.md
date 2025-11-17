# ⚽ The Football Hub – A Full Football Blogging CMS  
A complete football-focused content management system built with **Flask**, **CKEditor**, **SQLAlchemy**, and **Bootstrap**.  
Write, edit, manage, and publish football articles — match reports, tactical breakdowns, transfer talks, opinions & more.

---

## 🏆 Badges  
![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python)
![Flask](https://img.shields.io/badge/Flask-2.x-black?logo=flask)
![Bootstrap](https://img.shields.io/badge/Bootstrap-5-purple?logo=bootstrap)
![CKEditor](https://img.shields.io/badge/CKEditor-4-green)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-2.x-red?logo=python)
![License](https://img.shields.io/badge/License-MIT-yellow)

---

## 📸 Project Preview  
- 📝 Create rich-text football articles  
- ✏️ Edit existing posts (with auto-updated date)  
- 🗑 Delete posts  
- 📰 List of all posts  
- 🖼 Custom cover image per article  
- 🔥 Modern UI based on Bootstrap 5  
- ⚙️ Data stored in SQLite

---

## 📂 Folder Structure
```

football_hub/
│
├── main.py
├── posts.db
├── requirements.txt
│
├── templates/
│   ├── index.html
│   ├── post.html
│   ├── make-post.html
│   ├── about.html
│   ├── contact.html
│   ├── header.html
│   └── footer.html
│
└── static/
├── css/styles.css
├── js/scripts.js
└── assets/
├── football-home-bg.jpg
├── football-contact-bg.jpg
├── football-editor-bg.jpg
└── football-about-bg.jpg

````

---

## 🚀 Features

### ✍️ **Rich Blog Editor (CKEditor 4 LTS)**  
Create football articles with bold text, headings, images, embed videos & more.

### 📰 **Full Blog CMS**  
- Create posts  
- Edit posts  
- Delete posts  
- Auto-updated dates  
- Beautiful front-end layout  

### ⚽ Football-Themed UI  
Bootstrap + custom styling + category badges.

### 💾 Built with SQLAlchemy  
SQLite storage with a fully mapped `BlogPost` model.

### 🔐 Secure Forms  
Flask-WTF + CSRF protection + validators.

---

## 🛠 Installation

### 1) Clone Repo
```bash
git clone https://github.com/yourusername/football-hub.git
cd football-hub
````

### 2) Install Dependencies

```bash
pip install -r requirements.txt
```

### 3) Run the Server

```bash
python main.py
```

App runs at:
👉 [http://127.0.0.1:5003/](http://127.0.0.1:5003/)

---

## 🧠 Tech Stack

* **Flask** (Backend)
* **Bootstrap 5** (Frontend)
* **CKEditor** (Rich Text Editor)
* **SQLAlchemy ORM**
* **WTForms + Flask-WTF**
* **Jinja Templates**
* **SQLite Database**

---

## 🧪 API Routes (Internal)

| Route             | Method   | Description     |
| ----------------- | -------- | --------------- |
| `/`               | GET      | Show all posts  |
| `/post/<id>`      | GET      | View article    |
| `/new-post`       | GET/POST | Create new post |
| `/edit_post/<id>` | GET/POST | Edit post       |
| `/delete/<id>`    | GET/POST | Delete post     |
| `/about`          | GET      | About page      |
| `/contact`        | GET/POST | Contact page    |

---

## ✔ Future Enhancements

* User authentication (login/register)
* Comments section
* Image upload instead of URL
* Categories & tags
* Pagination

---

## 📜 License

MIT License — free to use and modify.

---

## ⭐ Show Support

If this project helped you, consider giving the repo a **star ⭐ on GitHub!**

```

---
