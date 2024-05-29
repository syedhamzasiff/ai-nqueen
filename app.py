from flask import Flask, render_template, request, jsonify
from nqueen import NQueens
import time


app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/find_solution", methods=["POST"])
def find_solution():
    algorithm = request.form.get("algorithm")
    N = int(request.form.get("N"))
    n_queens = NQueens(N)

    start_time = time.time()
    success = False
    additional_info = {}

    if algorithm == "backtracking":
        success = n_queens.backtracking(0)
    elif algorithm == "genetic":
        success, additional_info = n_queens.genetic_algorithm()
    elif algorithm == "ant_colony":
        success, additional_info = n_queens.ant_colony_optimization()
    elif algorithm == "particle_swarm":
        success, additional_info = n_queens.particle_swarm_optimization()
    elif algorithm == "brute_force":
        success = n_queens.brute_force()

    end_time = time.time()
    execution_time = end_time - start_time

    n_queens.log_run_info(algorithm, execution_time, success, additional_info)

    iterations = additional_info.get('iterations', None)

    return jsonify({
        "success": success,
        "board": n_queens.board,
        "execution_time": execution_time,
        "additional_info": additional_info
    })

if __name__ == "__main__":
    app.run(debug=True)
