def sum_of_intervals(intervals: list) -> int:
    result = set()
    for interval in intervals:
        start, stop = interval
        if start == stop:
            continue
        else:
            for num in range(start, stop):
                result.add(num)
    return len(result)


intervals = [
    [1, 2],
    [50, 100],
    [60, 70],
]
print(sum_of_intervals(intervals))
