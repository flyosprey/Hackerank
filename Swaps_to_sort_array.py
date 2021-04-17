from time import time


def minimumSwap(arr):
    start = time()
    ref_arr = sorted(arr)
    index_dict = {v: i for i, v in enumerate(arr)}
    swaps = 0

    for i, v in enumerate(arr):
        correct_value = ref_arr[i]
        if v != correct_value:
            to_swap_ix = index_dict[correct_value]
            arr[to_swap_ix], arr[i] = arr[i], arr[to_swap_ix]
            index_dict[v] = to_swap_ix
            index_dict[correct_value] = i
            swaps += 1

    print("--- %s -- seconds" % (time() - start))
    print(swaps)


test_1 = [4, 3, 1, 2]  # swaps = 3
test_2 = [2, 3, 4, 1, 5]  # swaps = 3
test_3 = [1, 3, 5, 2, 4, 6, 7]  # swaps = 3
tests = [test_1, test_2, test_3]


for test in tests:
    minimumSwap(test)
