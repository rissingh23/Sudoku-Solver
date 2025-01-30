from flask import Flask, request, jsonify
from flask_cors import CORS
from sudoku_solver import SudokuSolver
import random

app = Flask(__name__)
CORS(app)

solver_9x9 = SudokuSolver(["1", "2", "3", "4", "5", "6", "7", "8", "9"])
solver_16x16 = SudokuSolver(
    ["1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F", "G"]
)

@app.route("/solve", methods=["POST"])
def solve_sudoku():
    data = request.json
    grid = data.get("grid", [])
    size = data.get("size", 9)

    solver = solver_9x9 if size == 9 else solver_16x16
    formatted_grid = [[None if cell == "" else cell for cell in row] for row in grid]

    solved_grid = solver.solve(formatted_grid)

    return jsonify({"solution": solved_grid})


@app.route("/generate", methods=["GET"])
def generate_sudoku():
    size = int(request.args.get("size", 9))
    difficulty = request.args.get("difficulty", "easy").lower()

    solver = solver_9x9 if size == 9 else solver_16x16

    # Step 1: Generate a fully solved Sudoku board
    empty_grid = [[None for _ in range(size)] for _ in range(size)]
    solved_grid = solver.solve(empty_grid)

    if not solved_grid:
        return jsonify({"error": "Failed to generate a Sudoku puzzle"}), 500

    # Step 2: Define the number of cells to remove based on difficulty
    if size == 9:
        remove_counts = {"easy": 20, "medium": 40, "hard": 60}
    else:
        remove_counts = {"easy": 40, "medium": 70, "hard": 100}

    num_to_remove = remove_counts.get(difficulty, 40)  # Default to medium if invalid

    # Step 3: Remove numbers from the board
    removed_positions = set()
    while len(removed_positions) < num_to_remove:
        row, col = random.randint(0, size - 1), random.randint(0, size - 1)
        if (row, col) not in removed_positions:
            solved_grid[row][col] = ""
            removed_positions.add((row, col))

    return jsonify({"puzzle": solved_grid})


if __name__ == "__main__":
    app.run(debug=True)
