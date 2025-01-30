# 🎲 Sudoku Solver & Puzzle Generator

This is a **Sudoku Solver and Puzzle Generator** that automatically **solves and generates Sudoku puzzles** for both **9x9 and 16x16** grids.  
It supports **Easy, Medium, and Hard difficulty levels** and allows users to switch between grid sizes.

**⚠️ This is NOT a manual Sudoku-solving platform** – it solves puzzles **for you** and generates playable puzzles.

---

## 🚀 Features

✅ **Instantly solves Sudoku puzzles** (9x9 & 16x16).  
✅ **Generates Sudoku puzzles** at three difficulty levels: **Easy, Medium, Hard**.  
✅ **Switch between 9x9 and 16x16 grids** dynamically.  
✅ **Displays "Please wait..." message when generating 16x16 puzzles**.  
✅ **Clean, responsive UI** with automatic cell resizing.  

---

## 🛠 Installation & Setup

### 1️⃣ Clone the Repository  
```sh
git clone https://github.com/YOUR-USERNAME/sudoku-solver.git
cd sudoku-solver

2️⃣ Backend Setup (Flask API)

cd backend
python -m venv venv  # Create a virtual environment
venv\Scripts\activate  # Windows
source venv/bin/activate  # macOS/Linux
pip install flask flask-cors
python server.py  # Start the backend

3️⃣ Frontend Setup (React App)
sh
Copy
Edit
cd ../sudoku-solver
npm install  # Install dependencies
npm start  # Start the React frontend

