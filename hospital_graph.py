# ============================================
# IMPROVED HOSPITAL GRAPH
# ============================================
# More realistic hospital layout with balanced distances
# Designed for optimal pathfinding

class HospitalGraph:
    """
    Improved Hospital Graph - 9 services
    
    Layout:
    - Pharmacy: Central distribution point
    - Emergency Wing: Emergency, Pediatrics (urgent care)
    - Surgical Wing: Surgery, ICU (critical care)
    - Diagnostic Wing: Laboratory, Radiology
    - Outpatient: Cardiology, Consultations
    """
    
    def __init__(self):
        # Symmetric, realistic hospital graph
        self.graph = {
            # PHARMACY - Central Hub
            'Pharmacy': {
                'Emergency': 3,      # Quick access to emergency
                'Surgery': 5,        # Direct to surgical wing
                'Consultations': 4   # Outpatient access
            },
            
            # EMERGENCY WING
            'Emergency': {
                'Pharmacy': 3,
                'Pediatrics': 2,     # Emergency → Pediatrics (adjacent)
                'Cardiology': 4      # Emergency → Cardiology
            },
            
            'Pediatrics': {
                'Emergency': 2,
                'Surgery': 3,        # Pediatrics → Surgery
                'Consultations': 5
            },
            
            # SURGICAL WING
            'Surgery': {
                'Pharmacy': 5,
                'Pediatrics': 3,
                'ICU': 1,            # Surgery → ICU (adjacent, critical)
                'Radiology': 4       # Surgery → Radiology (imaging)
            },
            
            'ICU': {
                'Surgery': 1,
                'Laboratory': 2,     # ICU → Lab (tests)
                'Radiology': 3       # ICU → Radiology
            },
            
            # DIAGNOSTIC WING
            'Laboratory': {
                'ICU': 2,
                'Radiology': 2,      # Lab ↔ Radiology (adjacent)
                'Consultations': 6
            },
            
            'Radiology': {
                'Surgery': 4,
                'ICU': 3,
                'Laboratory': 2
            },
            
            # OUTPATIENT SERVICES
            'Cardiology': {
                'Emergency': 4,
                'Consultations': 2   # Cardio ↔ Consultations (adjacent)
            },
            
            'Consultations': {
                'Pharmacy': 4,
                'Pediatrics': 5,
                'Cardiology': 2,
                'Laboratory': 6
            }
        }
        
        self.services = list(self.graph.keys())
        
        # Service descriptions for better understanding
        self.descriptions = {
            'Pharmacy': 'Central medication distribution point',
            'Emergency': 'Emergency room - high priority',
            'Surgery': 'Operating rooms',
            'ICU': 'Intensive Care Unit - critical patients',
            'Pediatrics': 'Children care unit',
            'Cardiology': 'Heart disease treatment',
            'Laboratory': 'Medical tests and analysis',
            'Radiology': 'X-ray and imaging',
            'Consultations': 'Outpatient consultations'
        }
    
    def get_neighbors(self, service):
        """Get neighboring services and distances"""
        return self.graph.get(service, {})
    
    def get_distance(self, service1, service2):
        """Get distance between two connected services"""
        if service2 in self.graph.get(service1, {}):
            return self.graph[service1][service2]
        return None
    
    def display_graph(self):
        """Display the complete graph structure"""
        print("\n" + "="*70)
        print("IMPROVED HOSPITAL GRAPH")
        print("="*70)
        
        for service, neighbors in self.graph.items():
            desc = self.descriptions.get(service, "")
            print(f"\n{service} ({desc}):")
            for neighbor, distance in sorted(neighbors.items(), key=lambda x: x[1]):
                print(f"  → {neighbor:<20} distance: {distance} units")
        
        print("\n" + "="*70)
        print(f"Total services: {len(self.services)}")
        print(f"Total connections: {sum(len(v) for v in self.graph.values()) // 2}")
        print("="*70)
    
    def get_statistics(self):
        """Get graph statistics"""
        distances = []
        for neighbors in self.graph.values():
            distances.extend(neighbors.values())
        
        return {
            'nodes': len(self.services),
            'edges': len(distances) // 2,  # Bidirectional
            'min_distance': min(distances),
            'max_distance': max(distances),
            'avg_distance': sum(distances) / len(distances)
        }


if __name__ == "__main__":
    hospital = HospitalGraph()
    hospital.display_graph()
    
    print("\n\nGRAPH STATISTICS:")
    stats = hospital.get_statistics()
    print(f"  Nodes: {stats['nodes']}")
    print(f"  Edges: {stats['edges']}")
    print(f"  Distance range: {stats['min_distance']} - {stats['max_distance']}")
    print(f"  Average distance: {stats['avg_distance']:.1f}")
