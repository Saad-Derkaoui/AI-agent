# ============================================
# DISTRIBUTION AGENT
# ============================================

from hospital_graph import HospitalGraph
from algorithms import SearchAlgorithms


class DistributionAgent:
    
    def __init__(self):
        self.graph = HospitalGraph()
        self.current_position = 'Pharmacy'
        self.services_to_serve = []
        self.medications_delivered = []
        self.possible_actions = ['move', 'deliver_medications']
        self.algorithms = SearchAlgorithms(self.graph)
        self.total_distance = 0
        self.number_of_deliveries = 0
    
    
    def perceive_requests(self, services):
        self.services_to_serve = services
        print(f"\nRequests: {', '.join(services)}")
    
    
    def move(self, destination_service):
        distance = self.graph.get_distance(self.current_position, destination_service)
        if distance:
            self.current_position = destination_service
            self.total_distance += distance
            print(f"  Moving to {destination_service} (distance: {distance})")
            return True
        return False
    
    def deliver_medications(self, service):
        if service in self.services_to_serve:
            self.medications_delivered.append(service)
            self.services_to_serve.remove(service)
            self.number_of_deliveries += 1
            print(f"  Delivered to {service}")
            return True
        return False
    
    
    def plan_route(self, goal_service, algorithm='ucs'):
        print(f"\nPlanning: {self.current_position} -> {goal_service}")
        
        if algorithm == 'bfs':
            result = self.algorithms.bfs(self.current_position, goal_service)
        elif algorithm == 'dfs':
            result = self.algorithms.dfs(self.current_position, goal_service)
        elif algorithm == 'ucs':
            result = self.algorithms.ucs(self.current_position, goal_service)
        elif algorithm == 'astar':
            heuristic = self.create_heuristic(goal_service)
            result = self.algorithms.a_star(self.current_position, goal_service, heuristic)
        else:
            print("Unknown algorithm")
            return None
        
        return result
    
    
    def create_heuristic(self, goal):
        heuristiques = {
            'Pharmacy': {
                'Pharmacy': 0, 'Emergency': 4, 'Surgery': 3, 'Pediatrics': 6,
                'Cardiology': 8, 'ICU': 5, 'Radiology': 7, 'Consultation': 9, 'Laboratory': 8
            },
            'Emergency': {
                'Pharmacy': 4, 'Emergency': 0, 'Surgery': 6, 'Pediatrics': 2,
                'Cardiology': 5, 'ICU': 8, 'Radiology': 10, 'Consultation': 4, 'Laboratory': 10
            },
            'Surgery': {
                'Pharmacy': 3, 'Emergency': 6, 'Surgery': 0, 'Pediatrics': 8,
                'Cardiology': 10, 'ICU': 2, 'Radiology': 4, 'Consultation': 11, 'Laboratory': 4
            },
            'Pediatrics': {
                'Pharmacy': 6, 'Emergency': 2, 'Surgery': 8, 'Pediatrics': 0,
                'Cardiology': 5, 'ICU': 10, 'Radiology': 12, 'Consultation': 3, 'Laboratory': 12
            },
            'Cardiology': {
                'Pharmacy': 8, 'Emergency': 5, 'Surgery': 10, 'Pediatrics': 5,
                'Cardiology': 0, 'ICU': 12, 'Radiology': 14, 'Consultation': 2, 'Laboratory': 14
            },
            'ICU': {
                'Pharmacy': 5, 'Emergency': 8, 'Surgery': 2, 'Pediatrics': 10,
                'Cardiology': 12, 'ICU': 0, 'Radiology': 6, 'Consultation': 13, 'Laboratory': 3
            },
            'Radiology': {
                'Pharmacy': 7, 'Emergency': 10, 'Surgery': 4, 'Pediatrics': 12,
                'Cardiology': 14, 'ICU': 6, 'Radiology': 0, 'Consultation': 15, 'Laboratory': 3
            },
            'Consultation': {
                'Pharmacy': 9, 'Emergency': 4, 'Surgery': 11, 'Pediatrics': 3,
                'Cardiology': 2, 'ICU': 13, 'Radiology': 15, 'Consultation': 0, 'Laboratory': 15
            },
            'Laboratory': {
                'Pharmacy': 8, 'Emergency': 10, 'Surgery': 4, 'Pediatrics': 12,
                'Cardiology': 14, 'ICU': 3, 'Radiology': 3, 'Consultation': 15, 'Laboratory': 0
            }
        }
        
        return heuristiques.get(goal, {s: 0 for s in self.graph.services})
    
    
    def execute_mission(self, requested_services, algorithm='ucs'):
        print("\n" + "="*60)
        print("MISSION START")
        print("="*60)
        
        self.current_position = 'Pharmacy'
        self.total_distance = 0
        self.number_of_deliveries = 0
        self.medications_delivered = []
        
        self.perceive_requests(requested_services)
        
        for service in requested_services:
            print(f"\n--- Delivery to {service} ---")
            
            plan = self.plan_route(service, algorithm)
            
            if plan:
                path = plan['path']
                print(f"Path: {' -> '.join(path)}")
                print(f"Cost: {plan['cost']}, Nodes explored: {plan['nodes_explored']}")
                
                for i in range(len(path) - 1):
                    self.move(path[i + 1])
                
                self.deliver_medications(service)
            else:
                print(f"Cannot reach {service}")
        
        if self.current_position != 'Pharmacy':
            print(f"\n--- Returning to Pharmacy ---")
            return_plan = self.plan_route('Pharmacy', algorithm)
            if return_plan:
                path = return_plan['path']
                print(f"Return path: {' -> '.join(path)}")
                for i in range(len(path) - 1):
                    self.move(path[i + 1])
        
        self.display_report()
    
    
    def display_report(self):
        print("\n" + "="*60)
        print("REPORT")
        print("="*60)
        print(f"Deliveries: {self.number_of_deliveries}")
        print(f"Services: {', '.join(self.medications_delivered)}")
        print(f"Total distance: {self.total_distance} units")
        print(f"Final position: {self.current_position}")
        print("="*60)


if __name__ == "__main__":
    agent = DistributionAgent()
    agent.graph.display_graph()
    
    priority_services = ['Emergency', 'ICU', 'Laboratory']
    
    print("\n\nTEST WITH UCS")
    agent.execute_mission(priority_services, algorithm='ucs')
    
    input("\n\nPress Enter to continue...")
