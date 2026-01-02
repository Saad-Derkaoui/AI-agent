# ============================================
# SEARCH ALGORITHMS
# ============================================

from collections import deque
import heapq


class Node:
    def __init__(self, state, parent=None, action=None, cost=0):
        self.state = state
        self.parent = parent
        self.action = action
        self.cost = cost
    
    def __lt__(self, other):
        return self.cost < other.cost


class SearchAlgorithms:
    
    def __init__(self, graph):
        self.graph = graph
        self.nodes_explored = 0
    
    def reconstruct_path(self, node):
        path = []
        total_cost = node.cost
        
        while node.parent is not None:
            path.append(node.state)
            node = node.parent
        path.append(node.state)
        path.reverse()
        
        return path, total_cost
    
    
    def bfs(self, initial_state, goal_state):
        print("\n=== BFS ===")
        self.nodes_explored = 0
        
        frontier = deque([Node(initial_state)])
        explored = set()
        in_frontier = {initial_state}
        
        while frontier:
            current_node = frontier.popleft()
            in_frontier.remove(current_node.state)
            self.nodes_explored += 1
            
            if current_node.state == goal_state:
                path, cost = self.reconstruct_path(current_node)
                return {
                    'path': path,
                    'cost': cost,
                    'nodes_explored': self.nodes_explored
                }
            
            explored.add(current_node.state)
            
            neighbors = self.graph.get_neighbors(current_node.state)
            for neighbor, distance in neighbors.items():
                if neighbor not in explored and neighbor not in in_frontier:
                    new_node = Node(
                        state=neighbor,
                        parent=current_node,
                        action=f"Go to {neighbor}",
                        cost=current_node.cost + distance
                    )
                    frontier.append(new_node)
                    in_frontier.add(neighbor)
        
        return None
    
    
    def dfs(self, initial_state, goal_state):
        print("\n=== DFS ===")
        self.nodes_explored = 0
        
        frontier = [Node(initial_state)]
        explored = set()
        
        while frontier:
            current_node = frontier.pop()
            self.nodes_explored += 1
            
            if current_node.state == goal_state:
                path, cost = self.reconstruct_path(current_node)
                return {
                    'path': path,
                    'cost': cost,
                    'nodes_explored': self.nodes_explored
                }
            
            if current_node.state not in explored:
                explored.add(current_node.state)
                
                neighbors = self.graph.get_neighbors(current_node.state)
                neighbor_list = list(neighbors.items())
                for neighbor, distance in reversed(neighbor_list):
                    if neighbor not in explored:
                        new_node = Node(
                            state=neighbor,
                            parent=current_node,
                            action=f"Go to {neighbor}",
                            cost=current_node.cost + distance
                        )
                        frontier.append(new_node)
        
        return None
    
    
    def ucs(self, initial_state, goal_state):
        print("\n=== UCS ===")
        self.nodes_explored = 0
        
        frontier = []
        heapq.heappush(frontier, (0, Node(initial_state)))
        explored = set()
        best_cost = {initial_state: 0}
        
        while frontier:
            current_cost, current_node = heapq.heappop(frontier)
            self.nodes_explored += 1
            
            if current_node.state in explored:
                continue
            
            if current_node.state == goal_state:
                path, cost = self.reconstruct_path(current_node)
                return {
                    'path': path,
                    'cost': cost,
                    'nodes_explored': self.nodes_explored
                }
            
            explored.add(current_node.state)
            
            neighbors = self.graph.get_neighbors(current_node.state)
            for neighbor, distance in neighbors.items():
                if neighbor not in explored:
                    new_cost = current_node.cost + distance
                    
                    if neighbor not in best_cost or new_cost < best_cost[neighbor]:
                        best_cost[neighbor] = new_cost
                        new_node = Node(
                            state=neighbor,
                            parent=current_node,
                            action=f"Go to {neighbor}",
                            cost=new_cost
                        )
                        heapq.heappush(frontier, (new_cost, new_node))
        
        return None
    
    
    def a_star(self, initial_state, goal_state, heuristic):
        print("\n=== A* ===")
        self.nodes_explored = 0
        
        frontier = []
        h_initial = heuristic.get(initial_state, 0)
        heapq.heappush(frontier, (h_initial, Node(initial_state)))
        explored = set()
        best_cost = {initial_state: 0}
        
        while frontier:
            f_current, current_node = heapq.heappop(frontier)
            self.nodes_explored += 1
            
            if current_node.state in explored:
                continue
            
            if current_node.state == goal_state:
                path, cost = self.reconstruct_path(current_node)
                return {
                    'path': path,
                    'cost': cost,
                    'nodes_explored': self.nodes_explored
                }
            
            explored.add(current_node.state)
            
            neighbors = self.graph.get_neighbors(current_node.state)
            for neighbor, distance in neighbors.items():
                if neighbor not in explored:
                    g_new = current_node.cost + distance
                    
                    if neighbor not in best_cost or g_new < best_cost[neighbor]:
                        best_cost[neighbor] = g_new
                        h_new = heuristic.get(neighbor, 0)
                        f_new = g_new + h_new
                        
                        new_node = Node(
                            state=neighbor,
                            parent=current_node,
                            action=f"Go to {neighbor}",
                            cost=g_new
                        )
                        heapq.heappush(frontier, (f_new, new_node))
        
        return None
