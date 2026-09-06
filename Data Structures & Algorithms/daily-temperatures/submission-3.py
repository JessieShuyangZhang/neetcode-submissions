class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        """
        stsack: (40,5), (28,6) 

        [1, _, 1,]

        (30,0)
        38, i=1
        """

        stack=[] #(temp,index)
        res = [0]*len(temperatures)
        for i,temp in enumerate(temperatures): 
            while len(stack) !=0 and stack[-1][0] < temp:
                t,ind = stack.pop()
                res[ind] = i-ind
            stack.append((temp,i))
        
        return res