from django.shortcuts import render
from django.http import JsonResponse
from .utils import resolver_n_rainhas_dfs, resolver_n_rainhas_subida_encosta

# Índice da solução atual (para controle da navegação)
indice_solucao_atual = 0

def exibir_tabuleiro(request):
    """Renderiza a página inicial do tabuleiro."""
    global indice_solucao_atual
    indice_solucao_atual = 0  # Reinicia para a primeira solução
    return render(request, 'tabuleiro.html')

def iniciar_busca(request):
    """Inicia a busca de soluções com o algoritmo escolhido."""
    global solucoes, indice_solucao_atual
    algoritmo = request.GET.get('algoritmo', 'dfs')  # Obtém o parâmetro 'algoritmo' enviado pelo front-end

    if algoritmo == 'dfs':
        solucoes, tempo_execucao = resolver_n_rainhas_dfs()  # Executa busca em profundidade
    elif algoritmo == 'hill_climbing':
        solucoes, tempo_execucao = resolver_n_rainhas_subida_encosta()  # Executa subida de encosta
    else:
        return JsonResponse({'erro': 'Algoritmo inválido'}, status=400)  # Retorna erro se o algoritmo não for reconhecido

    indice_solucao_atual = 0
    return JsonResponse({'solucao': solucoes[indice_solucao_atual], 'tempo': tempo_execucao})

def proxima_solucao(request):
    """Avança para a próxima solução."""
    global solucoes, indice_solucao_atual
    indice_solucao_atual += 1
    if indice_solucao_atual >= len(solucoes):
        indice_solucao_atual = 0  # Reinicia para a primeira solução se atingir o final
    return JsonResponse({'solucao': solucoes[indice_solucao_atual]})