class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = list(zip(position,speed))
        cars.sort(reverse=True)
        fleets = []
        for pos, v in cars:
            eta = (target - pos)/v
            if not fleets or fleets[-1] < eta:
                fleets.append(eta)

        return len(fleets)