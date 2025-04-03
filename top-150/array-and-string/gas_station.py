class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        s = 0
        t = 0
        g = 0
        l = len(gas)

        for i in range(l):
            t += gas[i] - cost[i]
            g += gas[i] - cost[i]

            if g < 0:
                s = i + 1
                g = 0

        return -1 if t < 0 else s


"""
How does this work?

The idea is that if total_gas > total_cost there must always exist some valid path through the gas stations.
Further, if we start as some index i, and then fail at some index i + n, all starting indexes from [i, i+n] are invalid.
We can use these two facts to continuously eliminate indexes and then eventually find the correct index if it exists.
Part of the reason this works is the following line: "If there exists a solution, it is guaranteed to be unique." 
"""
