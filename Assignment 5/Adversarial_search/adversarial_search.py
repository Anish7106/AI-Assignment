"""
Adversarial Search Algorithms
Implements:
1. Minimax
2. Alpha-Beta Pruning
3. Heuristic Alpha-Beta Search
4. Monte-Carlo Tree Search (MCTS)

"""

import math
import random

# Makes MCTS random every run
# Remove/comment this if you want fully random results
# random.seed(42)


class TicTacToe:
    def __init__(self, board=None, player="X"):
        self.board = board if board else [" "] * 9
        self.player = player

    # Available empty positions
    def actions(self):
        return [i for i, value in enumerate(self.board) if value == " "]

    # Generate new state after move
    def result(self, action):
        new_board = self.board[:]
        new_board[action] = self.player

        next_player = "O" if self.player == "X" else "X"

        return TicTacToe(new_board, next_player)

    # Check winner
    def winner(self):
        winning_positions = [
            (0, 1, 2),
            (3, 4, 5),
            (6, 7, 8),
            (0, 3, 6),
            (1, 4, 7),
            (2, 5, 8),
            (0, 4, 8),
            (2, 4, 6)
        ]

        for a, b, c in winning_positions:
            if (
                self.board[a] != " "
                and self.board[a] == self.board[b] == self.board[c]
            ):
                return self.board[a]

        if " " not in self.board:
            return "Draw"

        return None

    # Terminal state
    def terminal(self):
        return self.winner() is not None

    # Utility function
    def utility(self):
        result = self.winner()

        if result == "X":
            return 1
        elif result == "O":
            return -1
        else:
            return 0

    # Display board
    def display(self):
        for i in range(0, 9, 3):
            print(
                self.board[i],
                "|",
                self.board[i + 1],
                "|",
                self.board[i + 2]
            )

            if i < 6:
                print("--+---+--")

        print()


# ---------------------------------------------------
# RANDOM BOARD GENERATOR
# ---------------------------------------------------

def random_board():
    """
    Generates random valid Tic-Tac-Toe board
    every time program runs.
    """

    board = [" "] * 9

    # Random number of moves already played
    moves = random.randint(2, 6)

    current_player = "X"

    for _ in range(moves):

        empty_positions = [
            i for i, value in enumerate(board)
            if value == " "
        ]

        if not empty_positions:
            break

        move = random.choice(empty_positions)

        board[move] = current_player

        current_player = (
            "O" if current_player == "X" else "X"
        )

    return TicTacToe(board, current_player)


# ---------------------------------------------------
# MINIMAX
# ---------------------------------------------------

def minimax(state):

    if state.terminal():
        return state.utility(), None

    # Maximizing player
    if state.player == "X":

        best_value = -math.inf
        best_move = None

        for action in state.actions():

            value, _ = minimax(state.result(action))

            if value > best_value:
                best_value = value
                best_move = action

        return best_value, best_move

    # Minimizing player
    else:

        best_value = math.inf
        best_move = None

        for action in state.actions():

            value, _ = minimax(state.result(action))

            if value < best_value:
                best_value = value
                best_move = action

        return best_value, best_move


# ---------------------------------------------------
# ALPHA BETA PRUNING
# ---------------------------------------------------

def alpha_beta(state, alpha=-math.inf, beta=math.inf):

    if state.terminal():
        return state.utility(), None

    # Maximizer
    if state.player == "X":

        best_value = -math.inf
        best_move = None

        for action in state.actions():

            value, _ = alpha_beta(
                state.result(action),
                alpha,
                beta
            )

            if value > best_value:
                best_value = value
                best_move = action

            alpha = max(alpha, best_value)

            # Pruning
            if beta <= alpha:
                break

        return best_value, best_move

    # Minimizer
    else:

        best_value = math.inf
        best_move = None

        for action in state.actions():

            value, _ = alpha_beta(
                state.result(action),
                alpha,
                beta
            )

            if value < best_value:
                best_value = value
                best_move = action

            beta = min(beta, best_value)

            # Pruning
            if beta <= alpha:
                break

        return best_value, best_move


# ---------------------------------------------------
# HEURISTIC FUNCTION
# ---------------------------------------------------

def heuristic_score(state):

    result = state.winner()

    if result == "X":
        return 100

    if result == "O":
        return -100

    if result == "Draw":
        return 0

    score = 0

    lines = [
        (0, 1, 2),
        (3, 4, 5),
        (6, 7, 8),
        (0, 3, 6),
        (1, 4, 7),
        (2, 5, 8),
        (0, 4, 8),
        (2, 4, 6)
    ]

    for line in lines:

        cells = [state.board[i] for i in line]

        x_count = cells.count("X")
        o_count = cells.count("O")

        if x_count > 0 and o_count == 0:
            score += 10 ** x_count

        elif o_count > 0 and x_count == 0:
            score -= 10 ** o_count

    return score


# ---------------------------------------------------
# HEURISTIC ALPHA BETA
# ---------------------------------------------------

def heuristic_alpha_beta(
    state,
    depth,
    alpha=-math.inf,
    beta=math.inf
):

    if state.terminal() or depth == 0:
        return heuristic_score(state), None

    # Maximizer
    if state.player == "X":

        best_value = -math.inf
        best_move = None

        for action in state.actions():

            value, _ = heuristic_alpha_beta(
                state.result(action),
                depth - 1,
                alpha,
                beta
            )

            if value > best_value:
                best_value = value
                best_move = action

            alpha = max(alpha, best_value)

            if beta <= alpha:
                break

        return best_value, best_move

    # Minimizer
    else:

        best_value = math.inf
        best_move = None

        for action in state.actions():

            value, _ = heuristic_alpha_beta(
                state.result(action),
                depth - 1,
                alpha,
                beta
            )

            if value < best_value:
                best_value = value
                best_move = action

            beta = min(beta, best_value)

            if beta <= alpha:
                break

        return best_value, best_move


# ---------------------------------------------------
# MCTS NODE
# ---------------------------------------------------

class MCTSNode:

    def __init__(
        self,
        state,
        parent=None,
        action=None
    ):

        self.state = state
        self.parent = parent
        self.action = action

        self.children = []

        self.visits = 0
        self.wins = 0

        self.untried_actions = state.actions()

    def uct_score(self, exploration=1.41):

        if self.visits == 0:
            return math.inf

        return (
            (self.wins / self.visits)
            + exploration
            * math.sqrt(
                math.log(self.parent.visits)
                / self.visits
            )
        )

    def best_child(self):
        return max(
            self.children,
            key=lambda child: child.uct_score()
        )

    def expand(self):

        action = self.untried_actions.pop()

        child_state = self.state.result(action)

        child = MCTSNode(
            child_state,
            parent=self,
            action=action
        )

        self.children.append(child)

        return child


# ---------------------------------------------------
# RANDOM SIMULATION
# ---------------------------------------------------

def random_playout(state):

    current = state

    while not current.terminal():

        move = random.choice(current.actions())

        current = current.result(move)

    return current.utility()


# ---------------------------------------------------
# BACKPROPAGATION
# ---------------------------------------------------

def backpropagate(node, result):

    while node is not None:

        node.visits += 1

        if result == 1:
            node.wins += 1

        elif result == 0:
            node.wins += 0.5

        node = node.parent


# ---------------------------------------------------
# MONTE CARLO TREE SEARCH
# ---------------------------------------------------

def mcts(state, iterations=1000):

    root = MCTSNode(state)

    for _ in range(iterations):

        node = root

        # Selection
        while (
            not node.state.terminal()
            and not node.untried_actions
        ):
            node = node.best_child()

        # Expansion
        if (
            not node.state.terminal()
            and node.untried_actions
        ):
            node = node.expand()

        # Simulation
        result = random_playout(node.state)

        # Backpropagation
        backpropagate(node, result)

    best_child = max(
        root.children,
        key=lambda child: child.visits
    )

    return best_child.action


# ---------------------------------------------------
# MAIN DEMO
# ---------------------------------------------------

def demo():

    # RANDOM BOARD EVERY RUN
    state = random_board()

    print("Initial Board:")
    state.display()

    minimax_value, minimax_move = minimax(state)

    ab_value, ab_move = alpha_beta(state)

    heuristic_value, heuristic_move = heuristic_alpha_beta(
        state,
        depth=3
    )

    mcts_move = mcts(state, iterations=2000)

    print("Minimax best move:", minimax_move)

    print("Alpha-Beta best move:", ab_move)

    print(
        "Heuristic Alpha-Beta best move:",
        heuristic_move
    )

    print("MCTS best move:", mcts_move)


# ---------------------------------------------------
# RUN PROGRAM
# ---------------------------------------------------

if __name__ == "__main__":
    demo()