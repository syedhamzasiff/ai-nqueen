# app.py
from flask import Flask, render_template, jsonify, request
from nqueen import NQueens

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/static/<path:path>")
def static_files(path):
    return app.send_static_file(path)

@app.route("/find_solution", methods=["POST"])
def find_solution():
    algorithm = request.form.get("algorithm")
    N = int(request.form.get("N"))
    n_queens = NQueens(N)
    
    if algorithm == "backtracking":
        if n_queens.backtracking(0):
            return jsonify({"board": n_queens.board, "N": N})
    elif algorithm == "genetic":
        if n_queens.genetic_algorithm():
            return jsonify({"board": n_queens.board, "N": N})
    elif algorithm == "simulated_annealing":
        if n_queens.simulated_annealing():
            return jsonify({"board": n_queens.board, "N": N})
    elif algorithm == "hill_climbing":
        if n_queens.hill_climbing():
            return jsonify({"board": n_queens.board, "N": N})
    
    return jsonify({"error": "Solution not found"}), 400 


