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

# Example usage:
pq = PriorityQueue()
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

graph2={'Arad': [('Zerind', 75), ('Sibiu', 140), ('Timisoara', 118)], 'Zerind': [('Arad', 75), ('Oradea', 71)], 'Sibiu': [('Arad', 140), ('Oradea', 151), ('Rimnicu Vilcea', 80), ('Fagaras', 99)], 'Timisoara': [('Arad', 118), ('Lugoj', 111)], 'Oradea': [('Zerind', 71), ('Sibiu', 151)], 'Lugoj': [('Timisoara', 111), ('Mehadia', 70)], 'Mehadia': [('Lugoj', 70), ('Drobeta', 75)], 'Drobeta': [('Mehadia', 75), ('Craiova', 120)], 'Craiova': [('Drobeta', 120), ('Rimnicu Vilcea', 146), ('Pitesti', 138)], 'Rimnicu Vilcea': [('Craiova', 146), ('Sibiu', 80), ('Pitesti', 97)], 'Pitesti': [('Craiova', 138), ('Rimnicu Vilcea', 97), ('Bucharest', 101)], 'Fagaras': [('Sibiu', 99), ('Bucharest', 211)], 'Bucharest': [('Fagaras', 211), ('Pitesti', 101), ('Giurgiu', 90), ('Urziceni', 85)], 'Giurgiu': [('Bucharest', 90)], 'Urziceni': [('Bucharest', 85), ('Hirsova', 98), ('Vaslui', 142)], 'Hirsova': [('Urziceni', 98), ('Eforie', 86)], 'Eforie': [('Hirsova', 86)], 'Vaslui': [('Urziceni', 142), ('Iasi', 92)], 'Iasi': [('Vaslui', 92), ('Neamt', 87)], 'Neamt': [('Iasi', 87)]}



def Bestfirstsearch(initial,goal,graph,heurestic):#inital is point from where we are starting,The point where we have to reach,
                                                # graph is graph  should be in the form dict which contain key as place and value as list of tuples which having the adjecent place with weight
                                                # heurestic should be in the form of dict 
    visited=[]
    visited.append(initial)
    goal_reached=True
    present=initial
    
    while goal_reached:
        pq=PriorityQueue()
        nbr=graph[present]# checking neibours
        for i in range(len(nbr)):
            if nbr not in visited:
                pq.push(nbr[i][0],heurestic[nbr[i][0]])#pusing the palce of name with its heuristic as key to priority queue so that if we pop the lower the heuristic will come
        ele=pq.pop()
        visited.append(ele)
        if ele==goal:# checking the final condition
            goal_reached=False
        present=ele
        # print(visited)
        

    return visited




if __name__=="__main__":
    start_city = 'Arad'
    end_city = 'Bucharest'

    ans = Bestfirstsearch(start_city, end_city, graph2, heuristic)

    if ans:
        print(f"Path from {start_city} to {end_city}: {' -> '.join(ans)}")
    else:
        print(f"No path found from {start_city} to {end_city}")
