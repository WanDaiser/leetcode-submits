class Solution(object):
    def winningPlayer(self, x, y):
        moves=min(x,y//4)
        return "Alice" if moves %2==1 else "Bob"
        