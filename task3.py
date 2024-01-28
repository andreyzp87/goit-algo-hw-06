def dijkstra(graph, start):
    # Ініціалізація відстаней та множини невідвіданих вершин
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0
    unvisited = list(graph.keys())

    while unvisited:
        # Знаходження вершини з найменшою відстанню серед невідвіданих
        current_vertex = min(unvisited, key=lambda vertex: distances[vertex])

        # Якщо поточна відстань є нескінченністю, то ми завершили роботу
        if distances[current_vertex] == float('infinity'):
            break

        for neighbor, weight in graph[current_vertex].items():
            distance = distances[current_vertex] + weight

            # Якщо нова відстань коротша, то оновлюємо найкоротший шлях
            if distance < distances[neighbor]:
                distances[neighbor] = distance

        # Видаляємо поточну вершину з множини невідвіданих
        unvisited.remove(current_vertex)

    return distances


if __name__ == '__main__':
    graph = {
        "Академмістечко": {"Театральна": 30},
        "Театральна": {"Академмістечко": 30, "Золоті ворота": 5, "Хрещатик": 3},
        "Хрещатик": {"Театральна": 3, "Лісова": 30, "Майдан Незалежності": 5},
        "Лісова": {"Хрещатик": 30},
        "Виноградар": {"Золоті ворота": 20},
        "Золоті ворота": {"Виноградар": 20, "Палац спорту": 3, "Театральна": 5},
        "Палац спорту": {"Золоті ворота": 3, "Червоний хутір": 40, "Площа Льва Толстого": 5},
        "Червоний хутір": {"Палац спорту": 40},
        "Героїв Дніпра": {"Майдан Незалежності": 30},
        "Майдан Незалежності": {"Героїв Дніпра": 30, "Площа Льва Толстого": 3, "Хрещатик": 5},
        "Площа Льва Толстого": {"Майдан Незалежності": 3, "Одеська": 30, "Палац спорту": 5},
        "Одеська": {"Площа Льва Толстого": 30},
    }

    for vertex, neighbors in graph.items():
        print(f"{vertex}: {dijkstra(graph, vertex)}")
