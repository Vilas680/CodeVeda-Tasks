# ♛ N-Queens Problem (Python)

This project provides a Python solution to the classic **N-Queens Problem** using the **Backtracking algorithm**.  
The goal is to place **N queens** on an **N × N chessboard** such that no two queens attack each other.

## 📌 Problem Statement

Place N queens on an N×N chessboard in such a way that:
- No two queens share the same row
- No two queens share the same column
- No two queens share the same diagonal

## 🛠️ Technology Used

- **Language:** Python 3
- **Algorithm:** Backtracking
- **Data Structure:** 2D Array (Chessboard)

---

## 📂 Project Structure
n-queens/
│
├── n_queens.py
└── README.md

## ⚙️ Algorithm Explanation

1. Start placing queens row by row.
2. For each row, try placing a queen in all columns.
3. Check if the position is safe:
   - No queen in the same column
   - No queen in left diagonal
   - No queen in right diagonal
4. If safe, place the queen and move to the next row.
5. If no safe position exists, backtrack to the previous row.

---

## ▶️ How to Run the Program

1. Ensure Python 3 is installed.
2. Open terminal or command prompt.
3. Run the program:

python n_queens.py

Example
Input
Enter value of N: 4

Output
. Q . .
. . . Q
Q . . .
. . Q .
