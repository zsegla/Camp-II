# https://leetcode.com/problems/minimum-cost-for-tickets/



class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        PASSES = [1, 7, 30]         # days covered

        @lru_cache(None)
        def get_min_cost(i):        # min cost from days[i] onwards

            if i >= len(days):
                return 0

            min_cost = float("inf")
            j = i
            for length, cost in zip(PASSES, costs):
                while j < len(days) and days[j] < days[i] + length:     # find next uncovered travel day by this pass
                    j += 1
                min_cost = min(min_cost, cost + get_min_cost(j))

            return min_cost

        return get_min_cost(0)
