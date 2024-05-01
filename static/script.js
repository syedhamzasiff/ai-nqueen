// script.js
document.addEventListener("DOMContentLoaded", function() {
    const canvas = document.getElementById("board-canvas");
    const ctx = canvas.getContext("2d");

    function drawBoard(N) {
        const cellSize = canvas.width / N;
        for (let row = 0; row < N; row++) {
            for (let col = 0; col < N; col++) {
                const color = (row + col) % 2 === 0 ? "white" : "darkgrey";
                ctx.fillStyle = color;
                ctx.fillRect(col * cellSize, row * cellSize, cellSize, cellSize);
            }
        }
    }

    function drawQueens(queens, N) {
        const cellSize = canvas.width / N;
        const queenImg = new Image();
        queenImg.src = "/static/queen.png";
        queenImg.onload = function() {
            queens.forEach((col, row) => {
                ctx.drawImage(queenImg, col * cellSize, row * cellSize, cellSize, cellSize);
            });
        };
    }

    function showToast(message) {
        const toast = document.getElementById('toast-message');
        toast.textContent = message;
        toast.classList.remove('hidden');
        setTimeout(function() {
            toast.classList.add('hidden');
        }, 3000);
    }
    
    
    function clearCanvas() {
        ctx.clearRect(0, 0, canvas.width, canvas.height);
    }

    document.getElementById("btn-backtracking").addEventListener("click", function() {
        const N = document.getElementById("slider-n").value;
        fetchAndDrawSolution("backtracking", N);
    });

    document.getElementById("btn-genetic").addEventListener("click", function() {
        const N = document.getElementById("slider-n").value;
        fetchAndDrawSolution("genetic", N);
    });

    document.getElementById("btn-simulated-annealing").addEventListener("click", function() {
        const N = document.getElementById("slider-n").value;
        fetchAndDrawSolution("simulated_annealing", N);
    });

    document.getElementById("btn-hill-climbing").addEventListener("click", function() {
        const N = document.getElementById("slider-n").value;
        fetchAndDrawSolution("hill_climbing", N);
    });

    document.getElementById("btn-reset").addEventListener("click", function() {
        const N = document.getElementById("slider-n").value;
        clearCanvas();
        drawBoard(N);
    });

    document.getElementById("slider-n").addEventListener("input", function() {
        const N = parseInt(this.value);
        clearCanvas();
        drawBoard(N);
    });

    drawBoard(8);

    function fetchAndDrawSolution(algorithm, N) {
        fetch("/find_solution", {
            method: "POST",
            headers: {
                "Content-Type": "application/x-www-form-urlencoded"
            },
            body: new URLSearchParams({
                algorithm: algorithm,
                N: N
            })
        })
        .then(response => {
            if (response.ok) {
                return response.json();
            } else {
                throw new Error("Solution not found");
            }
        })
        .then(data => {
            drawQueens(data.board, data.N);
        })
        .catch(error => {
            showToast(error.message); 
        });
    }
    
    
    
});
