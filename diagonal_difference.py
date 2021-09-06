"""Given a square matrix, calculate the absolute difference between the sums of its diagonals"""


def diagonal_difference(arr):
    left = 0
    right = 0
    for i in range(len(arr)):
        left += arr[i][i]
        right += arr[i][len(arr) - 1 - i]

    return abs(left - right)


arr = [[11, 2, 4], [4, 5, 6], [10, 8, -12]]  # 15

diagonal_difference(arr)
