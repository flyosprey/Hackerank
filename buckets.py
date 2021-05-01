"""Check if the example in the combination of brackets is correct"""

s1 = "(32 + (3*5) + ((223 - 55) * 125))"
s2 = "(32 + (3*5))"
s3 = "()())(())("
s4 = ')('
s5 = '()[['


def right_buckets(s):
    t1, t2 = '(', ')'
    k1, k2 = '[', ']'
    j1, j2 = '{', '}'

    count_t2, count_t1 = 0, 0
    count_k2, count_k1 = 0, 0
    count_j2, count_j1 = 0, 0

    for i in s:
        if t2 == i:
            count_t2 += 1
            if count_t2 == count_t1 + 1:
                break

        elif k2 == i:
            count_k2 += 1
            if count_k2 == count_k1 + 1:
                break

        elif j2 == i:
            count_j2 += 1
            if count_j2 == count_j1 + 1:
                break

        if t1 == i:
            count_t1 += 1

        elif k1 == i:
            count_k1 += 1

        elif j1 == i:
            count_j1 += 1

    if count_t2 == count_t1 and count_k2 == count_k1 and count_j2 == count_j1:
        print('Yes')

    elif count_t2 != count_t1 or count_k2 != count_k1 or count_j2 != count_j1:
        print('No')


# right_buckets(s1)
# right_buckets(s2)
# right_buckets(s3)
# right_buckets(s4)
right_buckets(s3)
