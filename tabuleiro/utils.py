import random
import time

# tabuleiro/utils.py

#Algoritmo de busca em profundidade
def posicao_valida(tabuleiro, row, col):
    for i in range(row):
        if tabuleiro[i] == col or \
           tabuleiro[i] - i == col - row or \
           tabuleiro[i] + i == col + row:
            return False
    return True

def dfs(tabuleiro, row, solutions):
    if row == len(tabuleiro):
        solutions.append(tabuleiro[:])
        return
    for col in range(len(tabuleiro)):
        if posicao_valida(tabuleiro, row, col):
            tabuleiro[row] = col
            dfs(tabuleiro, row + 1, solutions)
            tabuleiro[row] = -1

def solve_n_queens(n=8):
    tabuleiro = [-1] * n
    solutions = []
    start_time = time.time()
    dfs(tabuleiro, 0, solutions)
    end_time = time.time()
    execution_time = end_time - start_time
    
    return solutions, execution_time

#Algoritmo subindo morro com reinícios aleatórios 

def calculate_conflicts(board):
    """Calcula o número total de conflitos entre as rainhas no tabuleiro."""
    conflicts = 0
    n = len(board)
    for i in range(n):
        for j in range(i + 1, n):
            if board[i] == board[j] or abs(board[i] - board[j]) == abs(i - j):
                conflicts += 1
    return conflicts

def get_neighbors(board):
    """Gera os vizinhos da configuração atual do tabuleiro."""
    neighbors = []
    n = len(board)
    for col in range(n):
        for row in range(n):
            if board[col] != row:
                new_board = board[:]
                new_board[col] = row
                neighbors.append(new_board)
    return neighbors

def hill_climbing(n=8):
    """Encontra uma solução para o problema das N-rainhas usando Hill Climbing."""
    board = [random.randint(0, n - 1) for _ in range(n)]
    while True:
        conflicts = calculate_conflicts(board)
        if conflicts == 0:
            return board
        neighbors = get_neighbors(board)
        neighbor_conflicts = [(calculate_conflicts(neighbor), neighbor) for neighbor in neighbors]
        best_neighbor = min(neighbor_conflicts, key=lambda x: x[0])
        if best_neighbor[0] >= conflicts:
            board = [random.randint(0, n - 1) for _ in range(n)]
        else:
            board = best_neighbor[1]

def solve_n_queens_hill_climbing(n=8):
    """Envolve Hill Climbing para encontrar soluções."""
    
    solutions = set()
    # O problema das 8 rainhas tem exatamente 92 soluções
    start_time = time.time()
    while len(solutions) < 92:
        solution = tuple(hill_climbing(n))
        solutions.add(solution)
    end_time = time.time()
    execution_time = end_time - start_time
    return list(solutions), execution_time

