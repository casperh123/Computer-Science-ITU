from collections import defaultdict, deque
from typing import Dict, List, Set

class Graph:
    def __init__(self, player_edges: List[List[int]], players: int):
        self.nodes: Dict[int, Set[int]] = defaultdict(set)
        self.players = players
        
        source = 0
        sink = 2 * players + 1
        
        for i in range(1, players + 1):
            self.nodes[source].add(i)
        
        for i in range(players):
            player = i + 1
            for target in player_edges[i]:
                target_node = target + players
                self.nodes[player].add(target_node)
        
        for i in range(players + 1, 2 * players + 1):
            self.nodes[i].add(sink)
        
        self.nodes[sink] = set()

    def get_edges(self, node: int) -> set[int]:
        return self.nodes[node]

def solve(graph: Graph, players: int) -> dict[int, int]:
    source = 0
    sink = 2 * players + 1
    
    while True:
        path = find_path(graph, source, sink)
        
        if not path:
            break
            
        push_flow(graph, path)
    
    assignment = {}
    for player in range(1, players + 1):
        for target_node in graph.get_edges(player):
            if target_node > players and target_node <= 2 * players:
                assignment[player] = target_node - players
                break
    
    return assignment if len(assignment) == players else None

def push_flow(graph: Graph, path: List[int]):
    for i in range(len(path) - 1):
        u, v = path[i], path[i + 1]
        
        graph.nodes[u].remove(v)
        graph.nodes[v].add(u)

def find_path(graph: Graph, source: int, sink: int) -> List[int]:
    queue: deque = deque([source])
    visited: set = set([source])
    parent: dict[int, int] = { source: None }

    while queue:
        current = queue.popleft()

        if current == sink:
            return get_path(parent, sink)

        for neighbor in graph.get_edges(current):            
            if neighbor not in visited:
                parent[neighbor] = current
                visited.add(neighbor)

                if neighbor == sink:    
                    return get_path(parent, sink)

                queue.append(neighbor)
            
    return []

def get_path(parent: Dict[int, int], sink):
    path: List[int] = []
    current: int = sink

    while current is not None:
        path.append(current)
        current = parent[current]

    path.reverse()
    return path

player_number_string = input().split(" ")
players = int(player_number_string[0])
edge_amounts = int(player_number_string[1])
player_edges: List[List[int]] = [[] for _ in range(players)]

for i in range(edge_amounts):
    edges_input = input().split(" ")
    player = int(edges_input[0])
    edge_to = int(edges_input[1])

    player_edges[player - 1].append(edge_to)
    player_edges[edge_to - 1].append(player)

graph = Graph(player_edges, players)
solution = solve(graph, players) 

if solution is None:
    print("Impossible")
else:
    for i in range(1, players + 1):
        print(solution[i])