# 🔐 Py Password Manager (with JSON & Search)

An upgraded **Password Manager App** built using Python’s `tkinter`.  
Unlike the basic version that stored data in a text file, this version uses **JSON** for structured storage and adds a **search feature** to quickly retrieve saved credentials.

---

## 🚀 Features
- ✅ Generate strong random passwords  
- ✅ Save website, username, and password in `Saved_Passwords.json`  
- ✅ Search functionality to find credentials by website name  
- ✅ Input validation & confirmation prompts  
- ✅ Simple Tkinter GUI  

---

## 🛠️ Tech Stack
- **Python 3**
- **Tkinter (GUI library)**
- **Random module**
- **JSON (for structured data storage)**

---

## 📷 Demo Screenshot
*(Add screenshot of the app window here for better appeal)*

---

## 🎯 How It Works
1. Enter website & username/email.  
2. Generate a secure password with **Generate**.  
3. Save credentials — stored in `Saved_Passwords.json`.  
4. Use **Search** to look up credentials by website.  

Example JSON storage:
```json
{
   "facebook.com": {
      "ID": "user@gmail.com",
      "Password": "A9#xP2k!"
   },
   "github.com": {
      "ID": "coder123",
      "Password": "Pq7!Lm2@"
   }
}
