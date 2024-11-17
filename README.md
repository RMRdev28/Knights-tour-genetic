# Knight's Tour Solver using Genetic Algorithm
## Overview
This project implements a genetic algorithm to solve the Knight's Tour problem, developed as part of the Problem
Solving course in Master 1 Visual Computing at USTHB (2023/2024). The Knight's Tour is a sequence of moves where
a knight visits every square on a chessboard exactly once.
![Knight Moves](https://i.ibb.co/j4W55Dh/image.png "Knight Moves")
## Problem Description
In chess, a knight moves in an "L-shaped" pattern: two squares in one direction and then one square perpendicular to
that direction. The challenge is to find a sequence of moves that allows the knight to visit all 64 squares of the
chessboard exactly once.
## Project Structure
```
knights-tour-genetic/
│
├── genetic/
│ ├── chromosome.py
│ └── population.py
│
├── game/
│ ├── knight.py
│
├── visualization/
│ ├── visualize.py
│ ├── assets/
│   ├── knight.png
│   ├── board_green_light.png
│   ├── board_green_dark.png
│   ├── board_brown_light.png
│   └── board_brown_dark.png
│   └── knight_white.png
│   └── knight_black.png
│
├── main.py
├── config.py
├── requirements.txt
└── README.md
```
## Components

### 1. Chromosome Class
- Represents a sequence of knight's moves as genes
- Implements crossover and mutation operations
- Each gene represents one of 8 possible moves

### 2. Knight Class
Key features:
- Tracks position coordinates (x, y)
- Manages chromosome sequence
- Records path history
- Calculates fitness value (max 64)
- Implements move validation and correction

### 3. Population Class
Manages:
- Population size (default: 50)
- Generation counting
- Tournament selection
- Population evolution
- Fitness evaluation


### 4. Visualization
- Interactive display using Pygame
- Shows the knight's path on the chessboard
- Displays move numbers
- Supports multiple board themes

## Installation
1. Clone the repository:
```bash
git clone https://github.com/yourusername/knights-tour-genetic.git
cd knights-tour-genetic
```
2. Create and activate a virtual environment (optional but recommended):
```bash
python -m venv venv
source venv/bin/activate # On Windows: venv\Scripts\activate
```
3. Install dependencies:
```bash
pip install -r requirements.txt
```
## Usage
Run the main program:
```bash
python main.py
```
The program will:
1. Initialize a population of knights
2. Evolve solutions through generations
3. Display progress in the console
4. Visualize the final solution when found


## Configuration
Adjust parameters in `config.py`:
```python
MUTATION_RATE = 0.05
CROSSOVER_RATE = 1
POPULATION_SIZE = 50
```
## Visualization Features
- Interactive chessboard display
- Knight movement animation
- Move number tracking
- Multiple board themes (Green/Brown)
- Path visualization


## Dependencies
- Python 3.x
- Pygame

## License
This project is licensed under the MIT License - see the LICENSE file for details.

---
**Note**: This project is part of an academic assignment and is intended for educational purposes.
For any questions or issues, please open an issue in the GitHub repository.