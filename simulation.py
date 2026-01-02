# ============================================
# COMPLETE ALGORITHM SIMULATION
# ============================================
# Compares BFS, DFS, UCS and A*

from distribution_agent import DistributionAgent
import time


def full_comparison():
    """
    Complete comparison of all algorithms
    """
    print("\n" + "="*70)
    print("ALGORITHM COMPARISON")
    print("="*70)
    
    services = ['Surgery', 'Laboratory', 'Cardiology']
    
    algorithms = ['bfs', 'dfs', 'ucs', 'astar']
    algorithm_names = {
        'bfs': 'BFS (Breadth-First Search)',
        'dfs': 'DFS (Depth-First Search)',
        'ucs': 'UCS (Uniform Cost Search)',
        'astar': 'A* (A-Star)'
    }
    
    results = {}
    
    print(f"\nServices: {', '.join(services)}\n")
    
    for algo in algorithms:
        print(f"\n{'='*70}")
        print(f"Testing: {algorithm_names[algo]}")
        print(f"{'='*70}")
        
        agent = DistributionAgent()
        
        start = time.time()
        agent.execute_mission(services.copy(), algorithm=algo)
        end = time.time()
        
        results[algo] = {
            'distance': agent.total_distance,
            'deliveries': agent.number_of_deliveries,
            'time': round(end - start, 4)
        }
        
        print(f"\nExecution time: {results[algo]['time']} seconds")
        input("\nPress Enter to continue...")
    
    print("\n\n" + "="*70)
    print("RESULTS")
    print("="*70)
    print(f"{'Algorithm':<35} {'Distance':<15} {'Optimal?':<12}")
    print("-"*70)
    
    optimal_distance = min(results[algo]['distance'] for algo in ['ucs', 'astar'])
    
    for algo in algorithms:
        name = algorithm_names[algo]
        distance = results[algo]['distance']
        is_optimal = "YES" if distance == optimal_distance else "NO"
        print(f"{name:<35} {distance:<15} {is_optimal:<12}")
    
    print("="*70)


def simple_test():
    """
    Simple test with one algorithm
    """
    print("\n" + "="*70)
    print("SIMPLE TEST: PHARMACY -> LABORATORY")
    print("="*70)
    
    agent = DistributionAgent()
    result = agent.algorithms.ucs('Pharmacy', 'Laboratory')
    
    if result:
        print(f"\nPath found: {' -> '.join(result['path'])}")
        print(f"Distance: {result['cost']} units")
        print(f"Nodes explored: {result['nodes_explored']}")
    else:
        print("No path found")

def main_menu():
    """
    Interactive menu
    """
    while True:
        print("\n" + "="*70)
        print("MEDICATION DISTRIBUTION SYSTEM")
        print("="*70)
        print("\nChoose an option:")
        print("1. Simple test (Pharmacy -> Laboratory)")
        print("2. Complete mission with UCS")
        print("3. Compare all algorithms")
        print("4. Display hospital graph")
        print("5. Exit")
        print("="*70)
        
        choice = input("\nYour choice (1-5): ").strip()
        
        if choice == '1':
            simple_test()
        
        elif choice == '2':
            agent = DistributionAgent()
            services = input("\nEnter services (separated by commas): ").strip()
            services_list = [s.strip() for s in services.split(',')]
            agent.execute_mission(services_list, algorithm='ucs')
        
        elif choice == '3':
            full_comparison()
        
        elif choice == '4':
            from hospital_graph import HospitalGraph
            hospital = HospitalGraph()
            hospital.display_graph()
        
        elif choice == '5':
            print("\nGoodbye!")
            break
        
        else:
            print("\nInvalid choice. Try again.")
        
        input("\n\nPress Enter to return to menu...")


if __name__ == "__main__":
    main_menu()
