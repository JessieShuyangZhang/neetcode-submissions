class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        """
        s=v*t
        1+3t=4+2t
        t=3
        1+3*3=10
        """
        tup = [(position[i],speed[i]) for i in range(len(position))]
        sortedtup = sorted(tup,reverse=True) # (pos,speed)
        stack = []
        for currcar in sortedtup:
            if len(stack)!=0:
                frontcar = stack[-1]
                if (target-currcar[0])/currcar[1] > (target-frontcar[0])/frontcar[1]: # curr car creates new fleet
                    stack.append(currcar)
            else:
                stack.append(currcar)
        return len(stack)