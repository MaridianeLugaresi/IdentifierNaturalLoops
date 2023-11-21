D = [set(), set([1]),
set([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]),
set([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]),
set([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]),
set([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]),
set([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]),
set([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]),
set([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]),
set([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]),
set([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]),
set([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]),
set([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])]

pred = [{}, {}, {1, 3, 4}, {2}, {2}, {4, 10}, {4}, {5, 6}, {5, 9}, {8}, {9}, {7}, {10, 11}]

# Informação de dominadores (manualmente inserida)
dominators = { 1: set(),
               2: {1},
               3: {1},
               4: {1, 3},
               5: {1, 3},
               6: {1, 3, 4},
               7: {1, 3},
               8: {1, 3, 4},
               9: {1, 3, 4, 5},
              10: {1, 3, 4, 5},
              11: {1, 3, 4, 5, 9},
              12: {1, 3, 4, 5, 9, 10}}

# Identify Natural Loops
natural_loops = {}
for header_node in range(1, 13):
    for back_edge_node in pred[header_node]:
        natural_loop = {back_edge_node}
        current_node = back_edge_node

        while current_node != header_node:
            if current_node != back_edge_node:
                natural_loop.add(current_node)
            
            # Fix: Use the immediate dominator instead of the dominator set
            dominator_set = dominators[current_node]
            if not dominator_set:
                break  # Exit the loop if the dominator set is empty
            current_node = next(iter(dominator_set))

        natural_loops[(header_node, back_edge_node)] = natural_loop

# Print Natural Loops
for key, loop_set in natural_loops.items():
    header_node, back_edge_node = key
    print(f"Laço {header_node}:\nCabeçalho: {back_edge_node}\nBlocos: {loop_set}")