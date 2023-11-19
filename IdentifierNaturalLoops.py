D = [set(), set([1]), set([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]),
     set([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]), set([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]),
     set([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]), set([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]),
     set([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]), set([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]),
     set([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]), set([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]),
     set([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]), set([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])]

pred = [{}, {}, {1, 3, 4}, {2}, {2}, {4, 10}, {4}, {5, 6}, {5, 9}, {8}, {9}, {7}, {10, 11}]

# Informação de dominadores (manualmente inserida)
dominators = {1: set(), 2: {1}, 3: {1}, 4: {1, 3}, 5: {1, 3}, 6: {1, 3, 4}, 7: {1, 3}, 8: {1, 3, 4},
              9: {1, 3, 4, 5}, 10: {1, 3, 4, 5}, 11: {1, 3, 4, 5, 9}, 12: {1, 3, 4, 5, 9, 10}}

# Loop principal
while True:
    for i in range(1, 13):
        print("D[", i, "]:", D[i])

    Dcopia = [s.copy() for s in D]

    # Propagação de restrições com base nos dominadores
    for i in range(2, 13):
        inter = set([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
        for l in pred[i]:
            inter &= D[l]
        D[i] = {i} | inter | dominators[i]

    # Identificando os laços naturais
    natural_loops = {}
    for node in range(2, 13):
        natural_loop = set()
        current_node = node

        while current_node != 1:  # 1 é o cabeçalho do loop
            if current_node != node:  # Excluindo o próprio nó do conjunto de laços naturais
                natural_loop.add(current_node)
            current_node = next(iter(dominators[current_node]))

        if natural_loop:
            natural_loops[node] = natural_loop

    print("Laços naturais:")
    for node, loop in natural_loops.items():
        print(f"Nó {node}: {loop}")

    if Dcopia == D:
        break
