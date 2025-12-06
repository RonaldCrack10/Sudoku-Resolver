
# 🧩 Sudoku Solver

A simple and efficient Sudoku Solver implemented using backtracking.
The solver can read Sudoku boards, validate them, and compute a complete solution if one exists.

# ✨ Features

✔ Solves any valid 9×9 Sudoku puzzle

✔ Backtracking algorithm

✔ Input validation

✔ Command-line interface (optional)

✔ Easy to integrate into larger projects

✔ Includes tests

# 🚀 Getting Started
Prerequisites

You need Python 3.8+ installed.
(If you use Conda, you can import the provided environment file.)

Install dependencies

If using Conda:

conda env update --file environment.yml
conda activate sudoku


Or using pip:

pip install -r requirements.txt

# 🧠 How It Works

The solver uses a depth-first search with backtracking:

Find an empty cell.

Try digits 1–9.

Check if placing the digit is valid.

If yes → continue recursively.

If not → backtrack.

Continue until the board is solved.

This algorithm guarantees a solution if one exists.

# ▶ Usage
Run the solver:
python sudoku_solver.py

Solve a custom board:

Modify the board variable inside the file or load from a text file:

python sudoku_solver.py puzzles/hard01.txt

# 📜 License

This project is released under the MIT License.

# 🙌 Contributing

Pull requests are welcome!
Feel free to open an issue if you have ideas or encounter bugs.
