from django.shortcuts import render
from django.http import JsonResponse
from .utils import solve_n_queens, solve_n_queens_hill_climbing

# Armazena soluções na memória (simples)
solutions = solve_n_queens()
current_solution_index = 0

def tabuleiro_view(request):
    global current_solution_index
    current_solution_index = 0  # Reinicia no início
    return render(request, 'tabuleiro.html')

def iniciar_busca(request):
    global solutions, current_solution_index
    algoritmo = request.GET.get('algoritmo', 'dfs')  # Pega o parâmetro correto enviado pelo front-end
    
    if algoritmo == 'dfs':
        solutions, exec_time = solve_n_queens()  # Chama o DFS com medição de tempo
    elif algoritmo == 'hill_climbing':
        solutions, exec_time = solve_n_queens_hill_climbing()  # Chama o Hill Climbing com medição de tempo
    else:
        return JsonResponse({'error': 'Algoritmo inválido'}, status=400)  # Erro para valores inválidos
    
    current_solution_index = 0
    return JsonResponse({'solution': solutions[current_solution_index], 'time': exec_time})


def proxima_solucao(request):
    global solutions, current_solution_index
    current_solution_index += 1
    if current_solution_index >= len(solutions):
        current_solution_index = 0  # Reinicia ao atingir o final
    return JsonResponse({'solution': solutions[current_solution_index]})

#calcula o tempo de busca

