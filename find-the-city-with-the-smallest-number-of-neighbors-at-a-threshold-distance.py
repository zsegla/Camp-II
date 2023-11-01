# https://leetcode.com/problems/find-the-city-with-the-smallest-number-of-neighbors-at-a-threshold-distance/



class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:

        
        dist = [[float('inf') if i != j else 0 for j in range(n)] for i in range(n)]
        for u, v, d in edges:
            dist[u][v] = d
            dist[v][u] = d
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
        city_neighbors = {}
        for i in range(n):
            count = 0
            for j in range(n):
                if dist[i][j] <= distanceThreshold and i != j:
                    count += 1
            city_neighbors[i] = count
        min_neighbors = min(city_neighbors.values())
        result_city = 0
        for city, neighbors in city_neighbors.items():
            if min_neighbors == neighbors:
                result_city = max(result_city, city)
        return result_city


