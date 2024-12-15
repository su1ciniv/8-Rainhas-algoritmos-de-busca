import random
import time

# tabuleiro/utils.py

# Algoritmo de busca em profundidade
def posicao_valida(tabuleiro, linha, coluna):
    """Verifica se a posição é válida para colocar uma rainha no tabuleiro."""
    for i in range(linha):
        if tabuleiro[i] == coluna or \
           tabuleiro[i] - i == coluna - linha or \
           tabuleiro[i] + i == coluna + linha:
            return False
    return True

def busca_profundidade(tabuleiro, linha, solucoes):
    """Realiza a busca em profundidade para encontrar todas as soluções possíveis."""
    if linha == len(tabuleiro):
        solucoes.append(tabuleiro[:])
        return
    for coluna in range(len(tabuleiro)):
        if posicao_valida(tabuleiro, linha, coluna):
            tabuleiro[linha] = coluna
            busca_profundidade(tabuleiro, linha + 1, solucoes)
            tabuleiro[linha] = -1

def resolver_n_rainhas_dfs(n=8):
    """Resolve o problema das N-rainhas utilizando busca em profundidade."""
    tabuleiro = [-1] * n
    solucoes = []
    tempo_inicio = time.time()
    busca_profundidade(tabuleiro, 0, solucoes)
    tempo_fim = time.time()
    tempo_execucao = tempo_fim - tempo_inicio
    return solucoes, tempo_execucao

# Algoritmo de subida de encosta com reinícios aleatórios
def calcular_conflitos(tabuleiro):
    """Calcula o número total de conflitos entre as rainhas no tabuleiro."""
    conflitos = 0
    n = len(tabuleiro)
    for i in range(n):
        for j in range(i + 1, n):
            if tabuleiro[i] == tabuleiro[j] or abs(tabuleiro[i] - tabuleiro[j]) == abs(i - j):
                conflitos += 1
    return conflitos

def obter_vizinhos(tabuleiro):
    """Gera os vizinhos da configuração atual do tabuleiro."""
    vizinhos = []
    n = len(tabuleiro)
    for coluna in range(n):
        for linha in range(n):
            if tabuleiro[coluna] != linha:
                novo_tabuleiro = tabuleiro[:]
                novo_tabuleiro[coluna] = linha
                vizinhos.append(novo_tabuleiro)
    return vizinhos

def subida_encosta(n=8):
    """Encontra uma solução para o problema das N-rainhas usando Subida de Encosta."""
    tabuleiro = [random.randint(0, n - 1) for _ in range(n)]
    while True:
        conflitos = calcular_conflitos(tabuleiro)
        if conflitos == 0:
            return tabuleiro
        vizinhos = obter_vizinhos(tabuleiro)
        conflitos_vizinhos = [(calcular_conflitos(vizinho), vizinho) for vizinho in vizinhos]
        melhor_vizinho = min(conflitos_vizinhos, key=lambda x: x[0])
        if melhor_vizinho[0] >= conflitos:
            tabuleiro = [random.randint(0, n - 1) for _ in range(n)]
        else:
            tabuleiro = melhor_vizinho[1]

def resolver_n_rainhas_subida_encosta(n=8):
    """Resolve o problema das N-rainhas utilizando Subida de Encosta."""
    solucoes = set()
    tempo_inicio = time.time()
    while len(solucoes) < 92:  # O problema das 8 rainhas tem exatamente 92 soluções
        solucao = tuple(subida_encosta(n))
        solucoes.add(solucao)
    tempo_fim = time.time()
    tempo_execucao = tempo_fim - tempo_inicio
    return list(solucoes), tempo_execucao
