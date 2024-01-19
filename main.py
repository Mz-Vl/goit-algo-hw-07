from aa_tree import AATree

aa_tree = AATree()

keys = [5, 3, 8, 2, 4, 7, 9, -10, 1, 6, 10, 11, 12, 13, 14, 15, 16, 17]
for key in keys:
    aa_tree.insert(key)

print("\nMax node value is:", aa_tree.max_node_value())
print("\nMin node value is:", aa_tree.min_node_value())
print("\nSum node values is:", aa_tree.sum_node_values())
