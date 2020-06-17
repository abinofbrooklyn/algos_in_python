class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        d = {}
        for task in tasks:
            if task in d:
                d[task] += 1
            else:
                d[task] = 1

        list = sorted(d.values(), reverse = True)
        max_num = list[0]

        i = 0
        counter = 0
        while i < len(list) and list[i] == max_num:
            counter += 1
            i += 1

        result = (max_num - 1) * (n + 1) + counter
        return max(result, len(tasks))
