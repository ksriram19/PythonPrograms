import heapq

def minimum_cost_to_resolve_conflicts(n, g1, m, g2):
    # Step 1: Identify initial conflicts
    conflicts = [i for i in range(min(n, m)) if g1[i] == g2[i]]
    
    # Step 2: Initialize total cost
    total_cost = 0
    
    while conflicts:
        min_cost = float('inf')
        best_swap = None
        
        # Find the best swap with the minimum cost
        for i in conflicts:
            for j in range(n):
                if i != j and g1[j] != g2[i]:
                    cost = i + j
                    if cost < min_cost:
                        min_cost = cost
                        best_swap = (i, j)
        
        if best_swap is None:
            return -1  # No valid swap found, return -1
        
        i, j = best_swap
        # Perform the swap
        g1[i], g1[j] = g1[j], g1[i]
        total_cost += min_cost
        conflicts.remove(i)
        
        # Update conflicts
        if g1[j] == g2[j] and j not in conflicts:
            conflicts.append(j)
    
    return total_cost

# Input handling
n = int(input("Enter the number of shares in group 1: "))
g1 = list(map(int, input("Enter the share positions of group 1: ").split()))
m = int(input("Enter the number of shares in group 2: "))
g2 = list(map(int, input("Enter the share positions of group 2: ").split()))

if n != m:
    print(-1)
else:
    result = minimum_cost_to_resolve_conflicts(n, g1, m, g2)
    print(result)
