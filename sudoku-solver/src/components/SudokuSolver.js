import React, { useState } from "react";

function SudokuSolver() {
  const [gridSize, setGridSize] = useState(9); // Default to 9x9 grid
  const [difficulty, setDifficulty] = useState("medium"); // Default difficulty
  const [loading, setLoading] = useState(false); // Show loading message for 16x16

  const emptyGrid = (size) => Array(size).fill("").map(() => Array(size).fill(""));

  const [grid, setGrid] = useState(emptyGrid(gridSize));
  const [solvedGrid, setSolvedGrid] = useState(null);

  const solveSudoku = async () => {
    const response = await fetch("http://127.0.0.1:5000/solve", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ grid, size: gridSize }),
    });

    const data = await response.json();
    setSolvedGrid(data.solution);
  };

  const handleChange = (row, col, value) => {
    const validInput = gridSize === 9 ? /^[1-9]?$/.test(value) : /^[1-9A-G]?$/.test(value);
    if (validInput) {
      const newGrid = [...grid];
      newGrid[row][col] = value;
      setGrid(newGrid);
    }
  };

  const resetGrid = () => {
    setGrid(emptyGrid(gridSize));
    setSolvedGrid(null);
  };

  const generatePuzzle = async () => {
    if (gridSize === 16) {
      setLoading(true); // Show "Please wait" message for 16x16
    }

    const response = await fetch(`http://127.0.0.1:5000/generate?size=${gridSize}&difficulty=${difficulty}`, {
      method: "GET",
    });

    const data = await response.json();
    setGrid(data.puzzle);
    setSolvedGrid(null);
    setLoading(false); // Hide message after loading
  };

  const handleGridSizeChange = (e) => {
    const newSize = parseInt(e.target.value);
    setGridSize(newSize);
    setGrid(emptyGrid(newSize));
    setSolvedGrid(null);
  };

  const handleDifficultyChange = (e) => {
    setDifficulty(e.target.value);
  };

  const cellSize = gridSize === 9 ? "40px" : "25px"; // Smaller cells for 16x16

  return (
    <div className="sudoku-container">
      <h1>Sudoku Solver</h1>

      {/* Grid Size Selector */}
      <label>Grid Size: </label>
      <select onChange={handleGridSizeChange} value={gridSize} className="dropdown">
        <option value="9">9x9</option>
        <option value="16">16x16</option>
      </select>

      {/* Difficulty Selector */}
      <label>Difficulty: </label>
      <select onChange={handleDifficultyChange} value={difficulty} className="dropdown">
        <option value="easy">Easy</option>
        <option value="medium">Medium</option>
        <option value="hard">Hard</option>
      </select>

      {/* Show "Please wait..." only for 16x16 when generating */}
      {loading && <p className="loading-message">Please wait a few seconds while the puzzle generates...</p>}

      {/* Sudoku Grid Input */}
      <div
        className="sudoku-grid"
        style={{
          gridTemplateColumns: `repeat(${gridSize}, ${cellSize})`,
          gridTemplateRows: `repeat(${gridSize}, ${cellSize})`,
          width: `${gridSize * parseInt(cellSize)}px`,
          height: `${gridSize * parseInt(cellSize)}px`,
        }}
      >
        {(solvedGrid || grid).map((row, rowIndex) =>
          row.map((cell, colIndex) => (
            <input
              key={`${rowIndex}-${colIndex}`}
              className="sudoku-cell"
              style={{
                width: cellSize,
                height: cellSize,
                fontSize: gridSize === 9 ? "18px" : "14px",
              }}
              maxLength={1}
              value={solvedGrid ? solvedGrid[rowIndex][colIndex] : cell}
              onChange={(e) => handleChange(rowIndex, colIndex, e.target.value)}
              disabled={solvedGrid !== null && grid[rowIndex][colIndex] !== ""}
            />
          ))
        )}
      </div>

      <button className="solve-button" onClick={solveSudoku}>
        Solve
      </button>
      <button className="reset-button" onClick={resetGrid}>
        Reset Grid
      </button>
      <button className="generate-button" onClick={generatePuzzle}>
        Generate Puzzle
      </button>
    </div>
  );
}

export default SudokuSolver;
