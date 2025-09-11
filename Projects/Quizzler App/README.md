# Quizzler App 🧠

A Python-based Quiz Game that fetches **live trivia questions** from the [Open Trivia Database](https://opentdb.com/) API and presents them in a clean, interactive Tkinter UI.

---

## 🚀 Features
- ✅ Fetches fresh questions every run using API  
- ✅ Supports True/False quiz format  
- ✅ Live scoring system  
- ✅ Clean and responsive Tkinter UI  
- ✅ Feedback with color highlights (green/red)  
- ✅ Auto-disables buttons after quiz completion  

---

## 📂 Project Structure
├── main.py # Entry point
├── ui.py # Tkinter user interface
├── quiz_brain.py # Quiz logic and scoring
├── question_model.py # Question object
├── data.py # API call for fetching questions
└── images/ # UI button images (True/False)

---

## ⚙️ Setup Instructions
1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/quizzler-app.git
   cd quizzler-app
   
##Install dependencies:
```
pip install requests
```

##Run the app:
```
python main.py
```

##🎮 Demo
```
The app fetches 10 random True/False sports questions and lets you test your knowledge in a fun way.
Each correct answer increases your score, and feedback is given instantly with color highlights.
```
##📚 What I Learned
```
Working with external APIs (Open Trivia DB)
Using html.unescape() to clean API text
Structuring a Tkinter app with multiple modules
Implementing OOP concepts (Question, QuizBrain, QuizInterface)
```
##🚀 Future Improvements
```
Add multiple categories & difficulty levels
Support multiple-choice questions
Track high scores and quiz history
Package into a desktop app with PyInstaller
```
##🛠️ Tech Stack
```
Python 3
Tkinter (UI)
Requests (API calls)
```
