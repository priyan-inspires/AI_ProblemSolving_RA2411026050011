#  AI Problem Solving Assignment

##  Student Details

| Field | Details |
|------|--------|
| Name | Shanmugapriyan J|
| Register Number | RA2411026050011 |
| Department | CSE - AIML- "A"|
| Institution | SRM Institute of Science and Technology, Trichy |
| Submission Date | April 25, 2026 |

---

#  Table of Contents

1. Problem Description  
2. Features  
3. Algorithms Used  
4. Algorithm Comparison  
5. Folder Structure  
6. Installation & Execution  
7. Sample Output  
8. Code Explanation  
9. Real-World Applications  
10. References  

---

# 📌 Problem Description

This project implements two Artificial Intelligence problems using an interactive web interface.

### 🎮 Problem 1: Tic Tac Toe AI
- A classic game where a human plays against an AI.
- The AI always makes optimal decisions.

### 🧭 Problem 8: Smart Navigation System
- Finds a path between nodes in a graph.
- Compares BFS and DFS algorithms.

---

#  Features

| Feature | Description |
|--------|------------|
|  Interactive UI | Built using Streamlit |
|  Intelligent AI | Uses Minimax & Alpha-Beta |
|  Graph Traversal | BFS & DFS implementation |
|  Comparison | Execution time and path |
|  Fast Performance | Optimized algorithms |
|  Web-based | Runs in browser |

---

#  Algorithms Used

---

##  Tic Tac Toe AI

### 🔹 Minimax Algorithm
- Explores all possible moves
- Guarantees optimal decision
- Recursive decision-making

### 🔹 Alpha-Beta Pruning
- Optimized Minimax
- Eliminates unnecessary branches
- Faster execution

---

##  Smart Navigation System

### 🔵 BFS — Breadth-First Search

Concept:
- Explores graph level by level
- Always finds shortest path

| Property | Value |
|--------|------|
| Strategy | Level-order |
| Data Structure | Queue |
| Shortest Path | ✅ Yes |
| Time Complexity | O(V + E) |
| Space Complexity | O(V) |

---

### 🟣 DFS — Depth-First Search

Concept:
- Explores deep into graph
- Does not guarantee shortest path

| Property | Value |
|--------|------|
| Strategy | Depth-first |
| Data Structure | Stack / Recursion |
| Shortest Path | ❌ No |
| Time Complexity | O(V + E) |
| Space Complexity | O(V) |

---

#  Algorithm Comparison

| Metric | BFS | DFS |
|------|-----|-----|
| Path Optimality | ✅ Shortest | ❌ Not guaranteed |
| Nodes Explored | More | Less |
| Memory Usage | Higher | Lower |
| Speed | Moderate | Faster (in some cases) |

---

#  Folder Structure

AI_ProblemSolving_RA2411026050011/ │ ├── Problem_1_TicTacToe/ │   ├── minimax.py │   ├── alphabeta.py │   ├── tictactoe_ui.py │ ├── Problem_8_Navigation/ │   ├── bfs.py │   ├── dfs.py │   ├── navigation_ui.py │ ├── screenshots/ │   ├── tictactoe.png │   ├── navigation.png │ ├── main_app.py ├── requirements.txt ├── README.md

---

#  Installation & Execution

### 1️⃣ Clone Repository
git clone https://github.com/priyan-inspires/AI_ProblemSolving_RA2411026050011.git
cd AI_ProblemSolving_RA2411026050011

### 2️⃣ Install Dependencies
pip install -r requirements.txt

### 3️⃣ Run Application
streamlit run main_app.py

---

#  Sample Output

##  Tic Tac Toe
TicTacToe

## Navigation
Navigation

---

#  Code Explanation

### Tic Tac Toe
- Uses recursive Minimax algorithm
- Alpha-Beta pruning reduces complexity
- AI always chooses best move

### Navigation
- BFS uses queue (FIFO)
- DFS uses recursion
- Both compared using execution time

---

#  Real-World Applications

-  GPS Navigation Systems
-  Game AI (Chess, Tic Tac Toe)
-  Autonomous Vehicles
-  Network Routing
-  Decision-Making Systems

---

#  References

- Russell & Norvig – Artificial Intelligence  
- GeeksforGeeks  
- Python Documentation  
- Streamlit Official Docs  

---

#  Conclusion

This project demonstrates the implementation of AI algorithms for:
- Game decision-making  
- Graph traversal  
- Performance comparison  

It provides an interactive and visual way to understand core AI concep
