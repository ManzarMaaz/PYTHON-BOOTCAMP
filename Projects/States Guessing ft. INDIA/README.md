# 🗺️ India States Guessing Game 🇮🇳

An interactive Python game built with **Turtle Graphics** and **Pandas** where you guess all **28 states of India**.  
Inspired by the classic **U.S. States Game** from the 100 Days of Code bootcamp, but redesigned for India.  

---

## 🎮 How to Play
1. Run the game.
2. A blank outline map of India appears.
3. Enter the name of a state in the input box.
4. If correct ✅, the state’s name is placed on the map at the right coordinates.
5. Keep guessing until you find all **28 states**.
6. Type `Exit` anytime to quit — the game will save a list of **missing states** in a CSV file so you can practice later.

---

## 📂 Project Structure
```

📁 India-States-Game
┣ 📄 main.py                 # Main game logic
┣ 📄 india\_states.csv        # State names with coordinates
┣ 🖼️ india-outline-map.gif   # Background map of India
┣ 📄 Missing States.csv      # Auto-generated (states you missed)
┗ 📄 README.md               # Project documentation

````

---

## 🛠️ Tech Stack
- **Python** 🐍
- **Turtle** (for graphics)
- **Pandas** (for data handling)

---

## 📊 Dataset
The file **india_states.csv** contains:
- State Name  
- X-coordinate  
- Y-coordinate  

Example:
```csv
state,x,y
Andhra Pradesh,-125,-226
Assam,239,117
Tamil Nadu,-131,-345
...
````

---

## 🚀 Demo

* Start the game:

  ```bash
  python main.py
  ```
* Guess states until you win 🎉

---

## 📌 Features

* Covers all **28 Indian states** (no Union Territories).
* Keeps track of guessed vs. missing states.
* Auto-saves progress for practice.
* Easy to extend (you can add UTs later).

---

## 🌟 Future Ideas

* Add Union Territories (Delhi, J\&K, Ladakh, etc.)
* Add scoring & timer for challenge mode.
* Web version using **Flask/Django**.

---

## 📷 Preview

*(Insert screenshot or GIF of the game here)*

---

## 🤝 Contribution

Feel free to fork this repo and improve:

* Better UI/UX
* Add hints
* Multi-language support (Hindi/English)

---

## 📜 License

MIT License – free to use & modify.

---

