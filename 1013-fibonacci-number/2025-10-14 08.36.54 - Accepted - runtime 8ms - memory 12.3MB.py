class Solution(object):
    def fib(self, n):
        curr_term=1
        previous_term=0
        for i in range(n):
            previous_term,curr_term = curr_term,curr_term+previous_term
        return previous_term