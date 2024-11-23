from django.shortcuts import render
from django.http import JsonResponse
from .utils import solve_n_queens

# Armazena soluções na memória (simples)
solutions = solve_n_queens()
current_solution_index = 0

def tabuleiro_view(request):
    global current_solution_index
    current_solution_index = 0  # Reinicia no início
    return render(request, 'tabuleiro.html')

def iniciar_busca(request):
    global solutions, current_solution_index
    current_solution_index = 0
    return JsonResponse({'solution': solutions[current_solution_index]})

def proxima_solucao(request):
    global solutions, current_solution_index
    current_solution_index += 1
    print(solutions[current_solution_index])
    if current_solution_index >= len(solutions):
        current_solution_index = 0  # Reinicia ao atingir o final
    return JsonResponse({'solution': solutions[current_solution_index]})
