# tabuleiro/utils.py

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
    dfs(tabuleiro, 0, solutions)
    return solutions
