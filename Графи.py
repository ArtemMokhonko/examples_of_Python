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

"""
Рекурсивна реалізація алгоритму DFS
"""
# def dfs_recursive(graph, vertex, visited=None):
#     if visited is None:
#         visited = set()
#     visited.add(vertex)
#     print(vertex, end=' ')  # Відвідуємо вершину
#     for neighbor in graph[vertex]:
#         if neighbor not in visited:
#             dfs_recursive(graph, neighbor, visited)

# # Представлення графа за допомогою списку суміжності
# graph = {
#     'A': ['B', 'C'],
#     'B': ['A', 'D', 'E'],
#     'C': ['A', 'F'],
#     'D': ['B'],
#     'E': ['B', 'F'],
#     'F': ['C', 'E']
# }

# # Виклик функції DFS
# dfs_recursive(graph, 'A')


"""
Ітеративна реалізація алгоритму DFS
"""
# def dfs_iterative(graph, start_vertex):
#     visited = set()
#     # Використовуємо стек для зберігання вершин
#     stack = [start_vertex]  
#     while stack:
#         # Вилучаємо вершину зі стеку
#         vertex = stack.pop()  
#         if vertex not in visited:
#             print(vertex, end=' ')
#             # Відвідуємо вершину
#             visited.add(vertex)
#             # Додаємо сусідні вершини до стеку
#             stack.extend(reversed(graph[vertex]))  

# # Представлення графа за допомогою списку суміжності
# graph = {
#     'A': ['B', 'C'],
#     'B': ['A', 'D', 'E'],
#     'C': ['A', 'F'],
#     'D': ['B'],
#     'E': ['B', 'F'],
#     'F': ['C', 'E']
# }

# # Виклик функції DFS
# dfs_iterative(graph, 'A')


"""
Ітеративна реалізація алгоритму BFS виглядає таким чином:
"""
from collections import deque

# def bfs_iterative(graph, start):
#     # Ініціалізація порожньої множини для зберігання відвіданих вершин
#     visited = set()
#     # Ініціалізація черги з початковою вершиною
#     queue = deque([start])

#     while queue:  # Поки черга не порожня, продовжуємо обхід
#         # Вилучаємо першу вершину з черги
#         vertex = queue.popleft()
#         # Перевіряємо, чи була вершина відвідана раніше
#         if vertex not in visited:
#             # Якщо не була відвідана, друкуємо її
#             print(vertex, end=" ")
#             # Додаємо вершину до множини відвіданих вершин
#             visited.add(vertex)
#             # Додаємо всіх невідвіданих сусідів вершини до кінця черги
#             # Операція різниці множин вилучає вже відвідані вершини зі списку сусідів
#             queue.extend(set(graph[vertex]) - visited)
#     # Повертаємо множину відвіданих вершин після завершення обходу
#     return visited  

# # Представлення графа за допомогою списку суміжності
# graph = {
#     'A': ['B', 'C'],
#     'B': ['A', 'D', 'E'],
#     'C': ['A', 'F'],
#     'D': ['B'],
#     'E': ['B', 'F'],
#     'F': ['C', 'E']
# }

# # Запуск алгоритму BFS
# bfs_iterative(graph, 'A')

"""
Рекурсивна реалізація BFS може бути трохи менш прямолінійною через властивості черги, яка використовується в BFS.
"""
# from collections import deque

# def bfs_recursive(graph, queue, visited=None):
#     # Перевіряємо, чи існує множина відвіданих вершин, якщо ні, то ініціалізуємо нову
#     if visited is None:
#         visited = set()
#     # Якщо черга порожня, завершуємо рекурсію
#     if not queue:
#         return
#     # Вилучаємо вершину з початку черги
#     vertex = queue.popleft()
#     # Перевіряємо, чи відвідували раніше дану вершину
#     if vertex not in visited:
#         # Якщо не відвідували, друкуємо вершину
#         print(vertex, end=" ")
#         # Додаємо вершину до множини відвіданих вершин.
#         visited.add(vertex)
#         # Додаємо невідвіданих сусідів даної вершини в кінець черги.
#         queue.extend(set(graph[vertex]) - visited)
#     # Рекурсивний виклик функції з тією ж чергою та множиною відвіданих вершин
#     bfs_recursive(graph, queue, visited)

# # Представлення графа за допомогою списку суміжності
# graph = {
#     "A": ["B", "C"],
#     "B": ["A", "D", "E"],
#     "C": ["A", "F"],
#     "D": ["B"],
#     "E": ["B", "F"],
#     "F": ["C", "E"],
# }

# # Запуск рекурсивного алгоритму BFS
# bfs_recursive(graph, deque(["A"]))


import networkx as nx

G = nx.Graph()
