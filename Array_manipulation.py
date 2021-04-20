"""
    Starting with a 1-indexed array of zeros and a list of operations,
    for each operation add a value to each the array element between two given indices, inclusive.
    Once all operations have been performed, return the maximum value in the array.
"""


def array_manipulation(n, queries):
    arr = [0] * (n + 1)

    for quary in queries:
        start = quary[0] - 1
        end = quary[1]
        val = quary[2]

        arr[start] += val
        arr[end] -= val

    max_val = 0
    cur_val = 0
    for v in arr:
        cur_val += v
        if cur_val > max_val:
            max_val = cur_val

    print(max_val)


test_1 = [[1, 2, 100], [2, 5, 100], [3, 4, 100]]  # n = 5
test_2 = [[1, 5, 3], [4, 8, 7], [6, 9, 1]]  # n = 10
test_3 = [[2, 6, 8], [3, 5, 7], [1, 8, 1], [5, 9, 15]]  # n = 10
tests = [test_1, test_2, test_3]
n_1 = 5

for test in tests:
    array_manipulation(n_1, test)
