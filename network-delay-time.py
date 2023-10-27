# https://leetcode.com/problems/network-delay-time/



class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        best_times = [float("inf") for _ in range(n + 1)]
        best_times[k] = 0

        network = [[] for _ in range(n + 1)]
        for u, v, w in times:
            network[u].append((v, w))

        nodes = {no for no in range(1, n + 1)}

        while nodes:
            best_time = float("inf")
            for node in nodes:
                if best_times[node] < best_time:
                    best_time = best_times[node]
                    next_node = node

            if best_time == float("inf"):
                return -1
            nodes.remove(next_node)

            for nbor, time in network[next_node]:
                best_times[nbor] = min(best_times[nbor], best_time + time)

        return max(best_times[1:])
