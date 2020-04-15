def earliest_ancestor(ancestors, starting_node):
    for children in ancestors:
        print(children)

test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]
#make a list of all child
for children in ancestors:
