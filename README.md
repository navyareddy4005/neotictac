# 🤖 Neo TicTac AI

This is a Tic Tac Toe game I built with a smarter twist — instead of a basic opponent, it uses an AI that actually thinks before making a move.

I wanted to go beyond a simple game and try something that connects **DSA concepts with a real application**, so I used the **Minimax algorithm** to make the AI play optimally. Along with that, I designed a clean, futuristic UI to make the experience feel more interactive.

---

## 🎮 What you can do here

* Play against an AI that doesn’t make random moves
* Play with a friend on the same screen
* See how the AI evaluates moves through a small “neural log” panel
* Track wins and draws in real time

---

## 🧠 How the AI works

The AI uses the **Minimax algorithm**, which:

* Checks all possible future moves
* Assumes the opponent also plays perfectly
* Chooses the best possible outcome

Because of this, the AI is very hard to beat 😄

---

## 🛠️ Tech Stack

* **Backend:** Python (Flask)
* **Frontend:** HTML, CSS, JavaScript
* **Logic:** Minimax Algorithm

---

## 📂 Project Structure

```
neotictac-ai/
│
├── app.py
├── templates/
│   └── index.html
└── static/
    └── style.css
```

---

## ▶️ How to run this project

1. Clone the repository:

```
git clone https://github.com/your-username/neotictac.git
```

2. Open the project folder:

```
cd neotictac
```

3. Install required package:

```
pip install flask
```

4. Run the server:

```
python app.py
```

5. Open in browser:

```
http://127.0.0.1:5000/
```

---

## 🎮 Preview

(Add a screenshot of your project here)

---

## 💭 Why I built this

I wanted to understand how algorithms like Minimax actually work in real scenarios instead of just studying theory. This project helped me connect recursion, decision-making, and UI into one working system.

---

## 🚀 Future improvements

* Add difficulty levels (easy / medium / hard)
* Add animations and sound effects
* Make it playable online

---

## 👩‍💻 Author

Navya Reddy

---

## ⭐ Final note

This started as a small idea, but it turned into something I genuinely enjoyed building. If you try it and manage to beat the AI… that’s impressive 😄
