from graph import Graph

obj = Graph()
# obj.create_graph_interactive()
obj.graph = {'A': [{'B': 10}, {'C': 2}, {'D': 8}], 'B': [{'D': 12}], 'C': [{'A': 7}, {'B': 6}], 'D': [{'A': 1}]}
graph = {
    'A': [{'B': 10}, {'C': 2}, {'D': 8}], 'B': [{'D': 12}], 'C': [{'A': 7}, {'B': 6}], 'D': [{'A': 1}]}
# graph = {'A': ['B'], 'B': []}
# graph = {'B': []}
(obj.display_graph_edges(graph))
# print(list(obj.graph.keys())[0])

# print(obj.is_edge_direct(graph, 'A', 'A'))
# print(graph[list(graph.keys())[0]][0])
# print(graph.keys())
# print(obj.number_of_edges(graph))