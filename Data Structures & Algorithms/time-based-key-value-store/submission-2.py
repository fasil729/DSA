class TimeMap:

    def __init__(self):
        self.time_map = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.time_map[key].append((timestamp, value))
        

    def get(self, key: str, timestamp: int) -> str:
        arr = self.time_map[key]
        

        l, r = 0, len(arr) - 1

        while l <= r:
            mid = l + (r - l) // 2

            if arr[mid][0] <= timestamp:
                l = mid + 1
            else:
                r = mid - 1
        if l == 0:
            return ""
        return arr[l - 1][1]
        
