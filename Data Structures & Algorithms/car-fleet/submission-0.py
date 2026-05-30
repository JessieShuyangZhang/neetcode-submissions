class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        mp = dict(zip(position, speed))
        psorted = dict(sorted(mp.items(), reverse=True))
        fleets = []
        for pos, v in psorted.items():
            eta = (target-pos)/v
            if not fleets: 
                fleets.append(eta)
            if len(fleets) > 0:
                cur = fleets[-1]
                if eta > cur: # slower, will form another fleet
                    fleets.append(eta)

        return len(fleets) 