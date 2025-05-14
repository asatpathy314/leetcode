class TimeMap:
    def __init__(self):
        self.store = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        l = 0
        m = len(self.store[key]) // 2
        r = len(self.store[key]) - 1
        if len(self.store[key]) == 0:
            return ""
        default_value = self.store[key][m]
        if default_value[0] > timestamp:
            default_value = (-1, "")
        timestamp, value = self._binary_search(key, l, r, timestamp, default_value)
        return value

    def _binary_search(self, key, l, r, timestamp, max_timestamp_pair):
        print("Args: ", key, l, r, timestamp, max_timestamp_pair)
        m = (l + r) // 2
        key_values = self.store[key]
        if l > r:
            return max_timestamp_pair
        if key_values[m][0] < timestamp:
            max_timestamp_pair = max(key_values[m], max_timestamp_pair)
            return self._binary_search(key, m + 1, r, timestamp, max_timestamp_pair)
        elif key_values[m][0] > timestamp:
            return self._binary_search(key, l, m - 1, timestamp, max_timestamp_pair)
        elif key_values[m][0] == timestamp:
            max_timestamp_pair = max(key_values[m], max_timestamp_pair)
            return max_timestamp_pair
