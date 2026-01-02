# 🏥 Intelligent Hospital Medication Distribution Agent

A Python-based intelligent agent that optimizes medication distribution in a hospital environment using classical AI search algorithms (BFS, DFS, UCS, A\*).

**Author:** Saad Derkaoui  
**Course:** Artificial Intelligence  
**Institution:** High Tech Rabat  
**Date:** January 2026

---

## 📋 Project Overview

This project implements a **goal-based intelligent agent** that navigates a hospital graph to deliver medications efficiently. The agent compares four search algorithms to find optimal delivery routes while minimizing travel distance.

### Key Features

- ✅ 4 search algorithms (BFS, DFS, UCS, A\*)
- ✅ Interactive simulation interface
- ✅ Algorithm performance comparison
- ✅ Realistic hospital graph (9 services, 20 connections)
- ✅ Zero external dependencies (pure Python)

---

## 🗺️ Hospital Graph

The hospital consists of **9 services** connected by corridors:

| Service       | Type          | Description                            |
| ------------- | ------------- | -------------------------------------- |
| Pharmacy      | Central Hub   | Medication distribution starting point |
| Emergency     | Urgent Care   | Emergency room - high priority         |
| Surgery       | Critical Care | Operating rooms                        |
| ICU           | Critical Care | Intensive Care Unit                    |
| Pediatrics    | Specialty     | Children care unit                     |
| Cardiology    | Specialty     | Heart disease treatment                |
| Laboratory    | Diagnostic    | Medical tests and analysis             |
| Radiology     | Diagnostic    | X-ray and imaging services             |
| Consultations | Outpatient    | General consultations                  |

**Graph Statistics:**

- **Nodes:** 9 services
- **Edges:** 20 bidirectional connections
- **Distance Range:** 1-6 units
- **Average Distance:** 3.2 units

---

## 🤖 Agent Architecture

### PEAS Model

| Component       | Description                                   |
| --------------- | --------------------------------------------- |
| **Performance** | Minimize total distance, maximize deliveries  |
| **Environment** | Hospital graph with 9 services                |
| **Actuators**   | Move between services, deliver medications    |
| **Sensors**     | Current position, service requests, distances |

### Agent Type

**Goal-Based Agent** - Plans optimal routes using search algorithms to achieve delivery goals.

### Environment Properties

- **Observable:** Fully (agent knows all graph information)
- **Deterministic:** Yes (actions have predictable results)
- **Sequential:** Yes (current decisions affect future routes)
- **Static:** Yes (graph doesn't change during planning)
- **Discrete:** Yes (finite services and connections)
- **Single-Agent:** Yes (one agent operating)

---

## 🔬 Search Algorithms

### 1. BFS (Breadth-First Search)

- **Strategy:** Explores level by level
- **Data Structure:** FIFO Queue (deque)
- **Optimality:** Finds shortest path in _number of hops_, NOT distance
- **Use Case:** When all edge weights are equal

### 2. DFS (Depth-First Search)

- **Strategy:** Explores depth-first, then backtracks
- **Data Structure:** LIFO Stack (list)
- **Optimality:** Not guaranteed - finds _any_ path
- **Use Case:** Fast exploration when optimality isn't required

### 3. UCS (Uniform Cost Search)

- **Strategy:** Always expands lowest-cost node
- **Data Structure:** Priority Queue (heapq)
- **Optimality:** **Guaranteed** - always finds shortest distance
- **Use Case:** When you need optimal path without heuristic

### 4. A\* (A-Star)

- **Strategy:** UCS + heuristic guidance (f = g + h)
- **Data Structure:** Priority Queue with heuristic
- **Optimality:** **Guaranteed** (with admissible heuristic)
- **Efficiency:** Explores fewer nodes than UCS
- **Use Case:** Optimal path with maximum efficiency

---

## 📊 Performance Comparison

Example results for route: `Pharmacy → Surgery → Laboratory → Cardiology`

| Algorithm | Distance | Optimal? | Characteristic                  |
| --------- | -------- | -------- | ------------------------------- |
| BFS       | 80       | ❌ NO    | Fast but suboptimal             |
| DFS       | 80       | ❌ NO    | Unpredictable path              |
| UCS       | 41       | ✅ YES   | Optimal but explores many nodes |
| A\*       | 41       | ✅ YES   | Optimal AND efficient           |

**Conclusion:** A\* is the best algorithm for this problem - it guarantees optimal distance while exploring fewer nodes than UCS.

---

## 🚀 Installation & Usage

### Prerequisites

- Python 3.7 or higher
- No external libraries required (uses only Python standard library)

### Quick Start

1. **Clone the repository**

```bash
git clone https://github.com/Saad-Derkaoui/hospital-ai-agent.git
cd hospital-ai-agent
```

2. **Run the simulation**

```bash
python simulation.py
```

3. **Choose from the menu:**

```
1. Simple test (Pharmacy → Laboratory)
2. Complete mission with UCS
3. Compare all algorithms
4. Display hospital graph
5. Exit
```

### Running Individual Modules

**Display hospital graph:**

```bash
python hospital_graph.py
```

**Test the agent:**

```bash
python distribution_agent.py
```

**Run automated tests:**

```bash
python test_project.py
```

---

## 📁 Project Structure

```
hospital-ai-agent/
├── hospital_graph.py          # Hospital graph structure (9 services)
├── algorithms.py              # Search algorithms (BFS, DFS, UCS, A*)
├── distribution_agent.py      # Intelligent agent implementation
├── simulation.py              # Interactive menu and comparisons
├── test_project.py            # Automated testing
├── check_syntax.py            # Syntax validation
├── hospital_graph_visualization.html  # Visual graph (for presentation)
├── README.md                  # This file
└── __pycache__/              # Python cache (auto-generated)
```

---

## 🧪 Example Usage

### Simple Test

```python
from distribution_agent import DistributionAgent

agent = DistributionAgent()
agent.execute_mission(['Emergency', 'ICU'], algorithm='astar')
```

**Output:**

```
MISSION START
============================================================
Requests: Emergency, ICU

--- Delivery to Emergency ---
Planning: Pharmacy -> Emergency
Path: Pharmacy -> Emergency
Cost: 3, Nodes explored: 2

--- Delivery to ICU ---
Planning: Emergency -> ICU
Path: Emergency -> Pediatrics -> Surgery -> ICU
Cost: 6, Nodes explored: 5

REPORT
============================================================
Deliveries: 2
Services: Emergency, ICU
Total distance: 15 units
Final position: Pharmacy
```

---

## 🎓 Educational Value

This project demonstrates understanding of:

- ✅ **AI Agent Design** - PEAS modeling, goal-based reasoning
- ✅ **Search Algorithms** - Uninformed (BFS, DFS) vs Informed (UCS, A\*)
- ✅ **Graph Theory** - Representation, traversal, shortest path
- ✅ **Heuristic Design** - Creating admissible heuristics for A\*
- ✅ **Algorithm Analysis** - Time/space complexity, optimality guarantees
- ✅ **Problem Formulation** - States, actions, goals, costs

---

## 🔍 Problem Formulation

**State Space:**

- **Initial State:** Agent at Pharmacy
- **States:** 9 possible service locations
- **Actions:** Move(service_A, service_B) - travel between connected services
- **Goal Test:** All requested services have received medications
- **Path Cost:** Sum of corridor distances traveled

**Solution:** Sequence of moves that delivers all medications with minimum total distance.

---

## 📈 Algorithm Complexity

| Algorithm | Time Complexity  | Space Complexity | Optimal?  | Complete? |
| --------- | ---------------- | ---------------- | --------- | --------- |
| BFS       | O(b^d)           | O(b^d)           | No\*      | Yes       |
| DFS       | O(b^m)           | O(bm)            | No        | Yes\*\*   |
| UCS       | O(b^(1+⌊C\*/ε⌋)) | O(b^(1+⌊C\*/ε⌋)) | Yes       | Yes       |
| A\*       | O(b^d)           | O(b^d)           | Yes\*\*\* | Yes       |

\*BFS is optimal only for unweighted graphs  
**DFS is complete only in finite graphs  
\***A\* is optimal only with admissible heuristic

---

## 🛠️ Technical Implementation

### Key Design Decisions

**1. Graph Representation**

- Adjacency list (dictionary of dictionaries)
- Bidirectional edges (symmetric distances)
- Weighted edges (corridor distances)

**2. Node Structure**

```python
class Node:
    state: str        # Current service location
    parent: Node      # Previous node in path
    action: str       # Action that led here
    cost: int         # Total path cost from start
```

**3. Heuristic Function (A\*)**

- Pre-computed distance estimates
- Admissible (never overestimates true distance)
- Consistent (satisfies triangle inequality)

---

## 🎯 Future Improvements

Possible extensions for this project:

- [ ] Dynamic graph (services temporarily unavailable)
- [ ] Multiple agents (coordination required)
- [ ] Priority-based delivery (urgent medications first)
- [ ] Real-time visualization of agent movement
- [ ] Machine learning to improve heuristic
- [ ] Energy/battery constraints for the agent
- [ ] Delivery time windows

---

## 📚 References

- Russell, S., & Norvig, P. (2020). _Artificial Intelligence: A Modern Approach_ (4th ed.)
- Hart, P. E., Nilsson, N. J., & Raphael, B. (1968). "A Formal Basis for the Heuristic Determination of Minimum Cost Paths"
- Dijkstra, E. W. (1959). "A Note on Two Problems in Connexion with Graphs"

---

## 📝 License

This project is developed for educational purposes as part of the Artificial Intelligence course at High Tech Rabat.

---

## 👤 Author

**Saad Derkaoui**

- GitHub: [@Saad-Derkaoui](https://github.com/Saad-Derkaoui)

---

**⭐ If you find this project helpful, please consider giving it a star!**
