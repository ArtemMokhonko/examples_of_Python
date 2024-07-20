import matplotlib.pyplot as plt  # Імпортує бібліотеку для малювання графіків.
import matplotlib.patches as patches  # Імпортує модуль для створення графічних об'єктів, таких як полігони.

def draw_triangle(vertices, ax):  # Визначає функцію для малювання трикутника.
    triangle = patches.Polygon(vertices, fill=False, edgecolor='black')  # Створює об'єкт трикутника з вершинами 'vertices', без заливки (fill=False) та з чорною рамкою (edgecolor='black').
    ax.add_patch(triangle)  # Додає трикутник на осі 'ax'.

def midpoint(point1, point2):  # Визначає функцію для обчислення середньої точки між двома точками.
    return [(point1[0] + point2[0]) / 2, (point1[1] + point2[1]) / 2]  # Обчислює середні координати x та y між точками 'point1' та 'point2'.

def sierpinski(vertices, level, ax):  # Визначає рекурсивну функцію для малювання трикутника Серпінського.
    draw_triangle(vertices, ax)  # Малює трикутник з заданими вершинами 'vertices'.
    if level > 0:  # Якщо рівень рекурсії більше нуля, продовжує рекурсію.
        sierpinski([vertices[0], midpoint(vertices[0], vertices[1]), midpoint(vertices[0], vertices[2])], level-1, ax)  # Рекурсивно малює перший підтрикутник.
        sierpinski([vertices[1], midpoint(vertices[0], vertices[1]), midpoint(vertices[1], vertices[2])], level-1, ax)  # Рекурсивно малює другий підтрикутник.
        sierpinski([vertices[2], midpoint(vertices[2], vertices[1]), midpoint(vertices[0], vertices[2])], level-1, ax)  # Рекурсивно малює третій підтрикутник.

def main():  # Визначає основну функцію для налаштування та відображення малюнка.
    fig, ax = plt.subplots()  # Створює фігуру та осі для малювання.
    ax.set_aspect('equal')  # Встановлює однаковий масштаб по осях, щоб трикутники виглядали правильними.
    ax.set_axis_off()  # Вимикає відображення осей.
    vertices = [[0, 0], [0.5, 0.75], [1, 0]]  # Визначає початкові вершини трикутника.
    sierpinski(vertices, 9, ax)  # Викликає функцію 'sierpinski' для малювання трикутника Серпінського з рівнем рекурсії 3.
    plt.show()  # Відображає малюнок на екрані.

main()  # Викликає основну функцію для виконання всього коду.

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
print(check_edge(matrix, 1, 2))  # Виведе -1
