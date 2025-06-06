import heapq

class PriorityQueue:
    def __init__(self):
        self._queue = []  
        self._index = 0

    def push(self, item, priority):
        heapq.heappush(self._queue, (priority, self._index, item))
        self._index += 1

    def pop(self):
        return heapq.heappop(self._queue)[-1]

    def is_empty(self):
        return len(self._queue) == 0


heuristic = {
    'Arad': 366,
    'Bucharest': 0,
    'Craiova': 160,
    'Drobeta': 242,
    'Eforie': 161,
    'Fagaras': 176,
    'Giurgiu': 77,
    'Hirsova': 151,
    'Iasi': 226,
    'Lugoj': 244,
    'Mehadia': 241,
    'Neamt': 234,
    'Oradea': 380,
    'Pitesti': 100,
    'Rimnicu Vilcea': 193,
    'Sibiu': 253,
    'Timisoara': 329,
    'Urziceni': 80,
    'Vaslui': 199,
    'Zerind': 374
}

graph2={'Arad': [('Zerind', 75), ('Sibiu', 140), ('Timisoara', 118)], 'Zerind': [('Arad', 75), ('Oradea', 71)], 
        'Sibiu': [('Arad', 140), ('Oradea', 151), ('Rimnicu Vilcea', 80), ('Fagaras', 99)], 'Timisoara': [('Arad', 118), ('Lugoj', 111)], 'Oradea': [('Zerind', 71), ('Sibiu', 151)], 'Lugoj': [('Timisoara', 111), ('Mehadia', 70)], 'Mehadia': [('Lugoj', 70), ('Drobeta', 75)], 'Drobeta': [('Mehadia', 75), ('Craiova', 120)], 'Craiova': [('Drobeta', 120), ('Rimnicu Vilcea', 146), ('Pitesti', 138)], 'Rimnicu Vilcea': [('Craiova', 146), ('Sibiu', 80), ('Pitesti', 97)], 'Pitesti': [('Craiova', 138), ('Rimnicu Vilcea', 97), ('Bucharest', 101)], 'Fagaras': [('Sibiu', 99), ('Bucharest', 211)], 'Bucharest': [('Fagaras', 211), ('Pitesti', 101), ('Giurgiu', 90), ('Urziceni', 85)], 'Giurgiu': [('Bucharest', 90)], 'Urziceni': [('Bucharest', 85), ('Hirsova', 98), ('Vaslui', 142)], 'Hirsova': [('Urziceni', 98), ('Eforie', 86)], 'Eforie': [('Hirsova', 86)], 'Vaslui': [('Urziceni', 142), ('Iasi', 92)], 'Iasi': [('Vaslui', 92), ('Neamt', 87)], 'Neamt': [('Iasi', 87)]}

def gn(initial,upto,graph):# the function for finding g(n) for A* that is actual path length upto the node
    l=len(upto)
    dist=0
    for i in range(1,l):
        b=upto[i]
        a=upto[i-1]
        b_graph=graph[a]
        bl=len(b_graph)
        for j in range(bl):
            if b_graph[j][0]==b:
                dist+=b_graph[j][1]
    return dist


def a_star(initial, goal, graph, heuristic):
    pq = PriorityQueue()
    pq.push((initial, [initial]), heuristic[initial])
    visited = set()

    while not pq.is_empty(): 
        current, path = pq.pop()#getting least heuristic value 
        # print(path)
        
        if current == goal:# reached goal state
            return path
        
        if current in visited:# it skips if the node already visited
            continue
        
        visited.add(current)
        
        for nbr, cost in graph[current]:
            if nbr not in visited:
                new_path = path + [nbr]
                g_cost = gn(initial, new_path, graph)# calculating the cost 
                f_cost = g_cost + heuristic[nbr]# calculating actual cost
                pq.push((nbr, new_path), f_cost)
    
    return None  # If no path is found


if __name__=="__main__":

    start_city = 'Arad'
    end_city = 'Bucharest'

    ans = a_star(start_city, end_city, graph2, heuristic)

    if ans:
        print(f"Path from {start_city} to {end_city}: {' -> '.join(ans)}")
    else:
        print(f"No path found from {start_city} to {end_city}")


    
        
        
