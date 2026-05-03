import time
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

def check_winner(board):
    wins = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
    for w in wins:
        if board[w[0]] == board[w[1]] == board[w[2]] and board[w[0]] != "":
            return board[w[0]]
    if "" not in board: return "draw"
    return None

def minimax(board, is_max):
    result = check_winner(board)
    if result == "O": return 1
    if result == "X": return -1
    if result == "draw": return 0
    
    if is_max:
        best = -100
        for i in range(9):
            if board[i] == "":
                board[i] = "O"; score = minimax(board, False); board[i] = ""; best = max(score, best)
        return best
    else:
        best = 100
        for i in range(9):
            if board[i] == "":
                board[i] = "X"; score = minimax(board, True); board[i] = ""; best = min(score, best)
        return best

@app.route("/")
def index(): return render_template("index.html")

@app.route("/ai-move", methods=["POST"])
def ai_move():
    board = request.json["board"]
    # Simulate "Neural Processing" time for better UX
    time.sleep(0.6) 
    
    best_score = -100
    move = -1
    # Trace logic for the frontend "Neural Log"
    evaluated_nodes = []

    for i in range(9):
        if board[i] == "":
            board[i] = "O"
            score = minimax(board, False)
            board[i] = ""
            evaluated_nodes.append({"index": i, "score": score})
            if score > best_score:
                best_score = score
                move = i
                
    return jsonify({"move": move, "nodes": evaluated_nodes})

if __name__ == "__main__":
    app.run(debug=True)