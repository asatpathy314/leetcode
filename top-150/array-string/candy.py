class Solution:
    def candy(self, ratings: List[int]) -> int:
        candy = [1] * len(ratings)
        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i - 1]:
                candy[i] = candy[i - 1] + 1

        for i in range(len(ratings) - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                if candy[i] <= candy[i + 1]:
                    candy[i] = candy[i + 1] + 1

        return sum(candy)


"""
The above is the two-pass greedy solution. The way to think about the problem is as follows.
Forget about whether the child has less candy if they have less rating. instead consider
that for every child if their rating is greater than their left neighbor they should have
more candy than them and the same for their right neighbor. If we can have this be true for
every single child, then we have solved the problem. We can do this by setting the correct
candy w.r.t. every left neighbor, and then doing the same for every right neighbor. 
"""
