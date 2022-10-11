#matrizes povoadas
matriz_rg = [[0.1, 0.1, 0, 0.8, 0, 0],
            [0.1, 0, 0.1, 0, 0.8, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0.9, 0.1, 0],
            [0, 0, 0, 0.1, 0.8, 0.1],
            [0, 0, 0, 0, 0, 0]]

matriz_up = [[0.1, 0.8, 0, 0.1, 0, 0],
            [0, 0.1, 0.8, 0, 0.1, 0],
            [0, 0, 0, 0, 0, 0],
            [0.1, 0, 0, 0.1, 0.8, 0],
            [0, 0.1, 0, 0, 0.1, 0.8],
            [0, 0, 0, 0, 0, 0]]

matriz_lg = [[0.9, 0.1, 0, 0, 0, 0],
            [0.1, 0.8, 0.1, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0.8, 0, 0, 0.1, 0.1, 0],
            [0, 0.8, 0, 0.1, 0, 0.1],
            [0, 0, 0, 0, 0, 0]]

matriz_down = [[0.9, 0, 0, 0.1, 0, 0],
              [0.8, 0.1, 0, 0, 0.1, 0],
              [0, 0, 0, 0, 0, 0],
              [0.1, 0, 0, 0.9, 0, 0],
              [0, 0.1, 0, 0.8, 0.1, 0],
              [0, 0, 0, 0, 0, 0]]

#Função para dar update nos valores
def trocar_valor(matriz_up, matriz_down, matriz_rg, matriz_lg, vetor, valor, gamma, indice):

    aux = [[0, 0], [0, 0], [0, 0]]
    pointer = 0
    for x in range(2):
        aux[0][x] = valor[pointer+2]
        aux[1][x] = valor[pointer+1]
        aux[2][x] = valor[pointer]
        pointer = 3

    valor_aux = matrix = [0, 0, 0, 0, 0, 0]

    for x in range(6):
        valor_up = 0
        valor_down = 0
        valor_left = 0
        valor_right = 0
        for i in range(6):
            valor_up += matriz_up[x][i] * valor[i]
            valor_down += matriz_down[x][i] * valor[i]
            valor_right += matriz_rg[x][i] * valor[i]
            valor_left += matriz_lg[x][i] * valor[i]

        # EQUACAO DE BELMAN
        valor_aux[x] = vetor[x] + gamma * max(valor_up, valor_down, valor_left, valor_right)



    valor = valor_aux

    aux = [[0, 0], [0, 0], [0, 0]]
    pointer = 0
    for x in range(2):
        aux[0][x] = valor[pointer + 2]
        aux[1][x] = valor[pointer + 1]
        aux[2][x] = valor[pointer]
        pointer = 3

    print(f'Iteração n°{indice+1}')
    for x in aux:
        print(f'{x[0]:.2f} {x[1]:.2f}')

    print('\n')
    return valor_aux

#Função para calcular a política ótima do sistema
def return_policy(matriz_up, matriz_down, matriz_rg, matriz_lg, valor):
    politica = []

    for x in range(6):
        valor_up = 0
        valor_down = 0
        valor_left = 0
        valor_right = 0
        if x != 2 and x != 5:
            for i in range(6):
                valor_up += matriz_up[x][i] * valor[i]
                valor_down += matriz_down[x][i] * valor[i]
                valor_right += matriz_rg[x][i] * valor[i]
                valor_left += matriz_lg[x][i] * valor[i]

            movimentos = {valor_up: 'UP', valor_down: 'DW', valor_right: 'RG', valor_left: 'LG'}
            movimento = max(valor_up, valor_down, valor_left, valor_right)
            politica.append(movimentos[movimento])
        else:
            if x == 2:
                politica.append(-1)
            else:
                politica.append(1)

    print('---- Política final ----\n')
    print(f'-------- {politica[2]} {politica[5]} ----------')
    print(f'-------- {politica[1]} {politica[4]} ---------')
    print(f'-------- {politica[0]} {politica[3]} ---------')

#começo do código
vetor = [-0.04, -0.04, -1, -0.04, -0.04, 1]

gamma = 1

valor = [0, 0, -1, 0, 0, 1]

for i in range(200):
    valor = trocar_valor(matriz_up, matriz_down, matriz_rg, matriz_lg, vetor, valor, gamma, i)

return_policy(matriz_up, matriz_down, matriz_rg, matriz_lg, valor)