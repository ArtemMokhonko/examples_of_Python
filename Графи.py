def check_edge(adjacency_matrix, node1, node2):
    """
    Перевіряє, чи існує ребро між двома вузлами в графі.
    
    :param adjacency_matrix: Матриця суміжності графа.
    :param node1: Індекс першого вузла.
    :param node2: Індекс другого вузла.
    :return: 1, якщо ребро існує, -1, якщо не існує.
    """
    if adjacency_matrix[node1][node2] != 0:
        return 1
    else:
        return -1

# Приклад використання
matrix = [
    [0, 1, 0, 0],
    [1, 0, 1, 0],
    [0, 1, 0, 1],
    [0, 0, 1, 0]
]

print(check_edge(matrix, 0, 1))  # Виведе 1
print(check_edge(matrix, 0, 2))  # Виведе -1
