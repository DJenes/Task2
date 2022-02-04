def range1(start, end):
    current = start
    while current < end:
        yield current
        current += 1

nums = range1(1,10)

for num in nums:
    print(num)