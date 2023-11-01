# https://leetcode.com/problems/path-with-maximum-probability/ 



class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
       
        graph = [[] for _ in range(n)]
        
        for i, (a, b) in enumerate(edges):
            p = succProb[i]
            graph[a].append((b, p))
            graph[b].append((a, p))
        
        max_probs = [0.0] * n
        max_probs[start_node] = 1.0
        
        pq = [(-1.0, start_node)]  # Use negative values for max heap
        visited = set()
        
        while pq:
            prob, node = heapq.heappop(pq)
            prob = -prob  # Get the positive probability
            
            if node in visited:
                continue
            
            visited.add(node)
            
            for neighbor, neighbor_prob in graph[node]:
                if max_probs[neighbor] < prob * neighbor_prob:
                    max_probs[neighbor] = prob * neighbor_prob
                    heapq.heappush(pq, (-max_probs[neighbor], neighbor))
        
        return max_probs[end_node]

        #using shortest path algorithms
