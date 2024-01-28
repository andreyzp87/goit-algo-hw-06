import networkx as nx
import matplotlib.pyplot as plt

graph = {
    "Академмістечко": ["Театральна"],
    "Театральна": ["Академмістечко", "Золоті ворота", "Хрещатик"],
    "Хрещатик": ["Театральна", "Лісова", "Майдан Незалежності"],
    "Лісова": ["Хрещатик"],
    "Виноградар": ["Золоті ворота"],
    "Золоті ворота": ["Виноградар", "Палац спорту", "Театральна"],
    "Палац спорту": ["Золоті ворота", "Червоний хутір", "Площа Льва Толстого"],
    "Червоний хутір": ["Палац спорту"],
    "Героїв Дніпра": ["Майдан Незалежності"],
    "Майдан Незалежності": ["Героїв Дніпра", "Площа Льва Толстого", "Хрещатик"],
    "Площа Льва Толстого": ["Майдан Незалежності", "Одеська", "Палац спорту"],
    "Одеська": ["Площа Льва Толстого"],
}

if __name__ == '__main__':
    G = nx.Graph(graph)

    plt.figure(figsize=(10, 10))

    nx.draw(G, with_labels=True, node_color='lightblue', edge_color='gray')
    plt.show()

    print(f"Nodes: {len(G.nodes)}")
    print(f"Edges: {len(G.edges)}")

    for degree in G.degree:
        print(f"{degree[0]}: {degree[1]}")