class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        res=set()
        time=0
        mini=0
        cars=sorted(zip(position, speed), reverse=True)
        for pos, speed in cars:
            time=(target-pos)/speed
            print(time)
            if time>mini:
                mini=time
                res.add(time)
        return len(res)