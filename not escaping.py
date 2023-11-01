# https://codeforces.com/contest/1627/problem/E



import sys
from collections import defaultdict
import io
import os

input_data = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

inf = 5 * 10**16

for _ in range(int(input_data())):
    n, m, k = map(int, input_data().split())
    city_values = list(map(int, input_data().split()))
    city_connections = defaultdict(list)
    city_coords = set()
    city_coords.add((1, 1))
    city_coords.add((n, m))
    
    for i in range(k):
        start_x, start_y, end_x, end_y, distance = map(int, input_data().split())
        city_connections[start_x * m + start_y].append([end_x, end_y, distance])
        city_coords.add((start_x, start_y))
        city_coords.add((end_x, end_y))
        
    sorted_coords = sorted(list(city_coords))
    num_coords, coord_index = len(sorted_coords), {}
    dp, prefix, suffix = [-inf] * num_coords, [-inf] * num_coords, [-inf] * num_coords
    
    for i in range(num_coords):
        coord_index[sorted_coords[i]] = i
        
    coord_pairs, i = [], 0
    dp[0] = 0
    
    while i < num_coords:
        j = i
        while j + 1 < num_coords and sorted_coords[j + 1][0] == sorted_coords[j][0]:
            j += 1
            if sorted_coords[j][0] == 1:
                dp[j] = -city_values[0] * (sorted_coords[j][1] - 1)
        coord_pairs.append((i, j))
        i = j + 1
        
        
    for start, end in coord_pairs:
        left_val = right_val = -inf
        
        for i in range(start, end + 1):
            x, y = sorted_coords[i]
            left_val = max(left_val, prefix[i])
            dp[i] = max(dp[i], left_val - city_values[x - 1] * (y - 1))
            
        for i in range(end, start - 1, -1):
            x, y = sorted_coords[i]
            right_val = max(right_val, suffix[i])
            dp[i] = max(dp[i], right_val - city_values[x - 1] * (m - y))
            
        for i in range(start, end + 1):
            if dp[i] == -inf:
                continue
            
            x, y = sorted_coords[i]
            
            for end_x, end_y, distance in city_connections[x * m + y]:
                j = coord_index[(end_x, end_y)]
                dp[j] = max(dp[j], dp[i] + distance)
                prefix[j] = max(prefix[j], dp[j] + city_values[end_x - 1] * (end_y - 1))
                suffix[j] = max(suffix[j], dp[j] + city_values[end_x - 1] * (m - end_y))
                
                
    print(-dp[-1] if dp[-1] != -inf else "NO ESCAPE")
