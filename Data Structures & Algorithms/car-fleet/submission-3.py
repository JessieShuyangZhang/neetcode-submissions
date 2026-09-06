class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        """
        s=v*t
        1+3t=4+2t
        t=3
        1+3*3=10
        """
        tup = [(position[i],speed[i]) for i in range(len(position))]
        tup.sort(reverse=True) # (pos,speed)
        stack = []
        for currcar in tup:
            t = (target-currcar[0])/currcar[1]

            if len(stack)!=0:
                frontcar = stack[-1]
                if t > frontcar: # curr car creates new fleet
                    stack.append(t)
            else:
                stack.append(t)
        return len(stack)