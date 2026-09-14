class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        afound, bfound, cfound = False, False, False
        for i in range(len(triplets)):
            if (triplets[i][0] > target[0] or triplets[i][1] > target[1] or triplets[i][2] > target[2]):
                continue
            if triplets[i][0] == target[0]:
                afound = True
            if triplets[i][1] == target[1]:
                bfound = True
            if triplets[i][2] == target[2]:
                cfound = True
            if afound and bfound and cfound: 
                return True
        return False