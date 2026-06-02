class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        euclidean = lambda x: (x[0]**2+x[1]**2)**0.5 
        def pivot(l,r):
            # r is pivot
            distP = euclidean(points[r])
            i = l
            for j in range(l,r):
                if euclidean(points[j]) <= distP:
                    points[i], points[j] = points[j], points[i]  
                    i += 1
            # i is where r should go
            points[i], points[r] = points[r], points[i]
            return i 

        l, r = 0, len(points)-1
        p = len(points)
        while p != k-1:
            p = pivot(l,r)
            if p<k-1:
                l = p+1
            elif p>k-1:
                r = p-1            
        return points[0:k]
        