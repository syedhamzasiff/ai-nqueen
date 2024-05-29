# N-Queens Solver

The N-Queens Solver is a web application built with Flask that allows users to find solutions to the N-Queens problem using various algorithms.

## Problem Description

The N-Queens problem is a classic problem in combinatorial optimization and chessboard puzzles. It involves placing N chess queens on an N×N chessboard so that no two queens threaten each other. In other words, no two queens can share the same row, column, or diagonal.

## Features

- **Multiple Algorithms**: The application supports solving the N-Queens problem using different algorithms, including backtracking, genetic algorithm, simulated annealing, and hill climbing.

- **Adjustable Board Size**: Users can adjust the size of the chessboard (N) using a slider control to find solutions for various board sizes.

- **Interactive Visualization**: The application provides an interactive visualization of the chessboard and the queen placements, allowing users to see the solutions in real-time.

- **Error Handling**: If a solution cannot be found for the specified parameters, the application displays a toast message notifying the user of the issue.

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/your_username/N-Queens-Solver.git
    ```

2. Install the dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Run the Flask application:

    ```bash
    python app.py
    ```

4. Open a web browser and navigate to `http://localhost:5000` to access the application.

## Usage

1. Adjust the board size using the slider control.
2. Select an algorithm from the available options (backtracking, genetic algorithm, simulated annealing, hill climbing).
3. Click the "Find Solution" button to start the solving process.
4. Once a solution is found, the chessboard will display the queen placements.
5. If no solution is found, a toast message will be displayed indicating the issue.

## Contributing

Contributions are welcome! If you'd like to contribute to the project, please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/new-feature`).
3. Make your changes.
4. Commit your changes (`git commit -am 'Add new feature'`).
5. Push to the branch (`git push origin feature/new-feature`).
6. Create a new pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
