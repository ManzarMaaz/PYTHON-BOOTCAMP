# ⚽ Matchday Pulse – Your Daily Heartbeat of Football News

![Python](https://img.shields.io/badge/Python-3.12-blue?logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-2.3-black?logo=flask&logoColor=white)
![Bootstrap](https://img.shields.io/badge/Bootstrap-5.3-purple?logo=bootstrap&logoColor=white)
![API](https://img.shields.io/badge/REST%20API-Enabled-green)
![License](https://img.shields.io/badge/License-MIT-yellow)
![Status](https://img.shields.io/badge/Status-Active-success)

> “Your daily heartbeat of football news.”  
> Matchday Pulse is a **Flask-powered football blog** that dynamically loads articles from a live API and presents them in a clean, responsive layout.

---

## 🏟️ Overview

**Matchday Pulse** is a simple yet elegant **Flask web app** that delivers the latest football news posts from an API endpoint.  
It demonstrates modular template usage (`header.html`, `footer.html`, `about.html`, etc.) and the integration of external JSON APIs into dynamic content rendering.

Built with **Python**, **Flask**, and **Bootstrap**, this project emphasizes **clarity, scalability, and separation of concerns**.

---

## ⚙️ Features

- 🌍 **Dynamic Content** – Fetches all posts live from an external API  
- 📰 **Post Pages** – Dedicated pages for each article  
- 📖 **Modular Templates** – Reusable headers, footers, and layouts  
- ⚡ **Responsive Design** – Mobile-friendly with Bootstrap 5  
- 💬 **About & Contact Pages** – Simple static pages for branding and outreach  

---

## 🧠 Tech Stack

| Component | Purpose |
|------------|----------|
| **Flask** | Backend framework for routing and templating |
| **Requests** | Fetch data from external API |
| **Bootstrap 5** | Frontend styling and layout |
| **HTML + Jinja2** | Template rendering engine |

---

## 🗂️ Project Structure

```
MatchdayPulse/
│
├── main.py                     # Flask server file
├── templates/
│   ├── index.html              # Home page with all posts
│   ├── post.html               # Individual post template
│   ├── about.html              # About page
│   ├── contact.html            # Contact page
│   ├── header.html             # Shared header
│   └── footer.html             # Shared footer
├── static/
│   ├── assets/
│   │   └── img/                # Backgrounds, icons, etc.
│   └── css/
│       └── styles.css
└── README.md
```

---

## 🚀 Getting Started

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/ManzarMaaz/MatchdayPulse.git
cd MatchdayPulse
```

### 2️⃣ Install Dependencies
```bash
pip install flask requests
```

### 3️⃣ Run the Server
```bash
python main.py
```

### 4️⃣ Open in Browser
Visit [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## 💡 Learning Takeaways

- How to integrate **external REST APIs** into Flask routes  
- Using **modular Jinja templates** for maintainable UI  
- Building responsive pages with **Bootstrap 5**  
- Understanding **Flask routing and dynamic URL parameters**  

---

## 🏁 Future Enhancements

- 🗞️ Add a backend CMS or database  
- 💬 Enable comment sections on posts  
- ⚽ Implement live score widgets via API integration  
- 📸 Add image uploads for each post  

---

## 👤 Author

**Mohammed Manzar Maaz**  
🔗 [LinkedIn](https://www.linkedin.com/in/mohammed-manzar-maaz/) | 💻 [GitHub](https://github.com/ManzarMaaz)

---

⭐ If you enjoyed exploring this project, **give it a star** and stay tuned for more creative Flask builds!
