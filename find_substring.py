def find_substring(s, k):
    vowels = ('a', 'e', 'i', 'o', 'u')

    old_counter = 0
    new_counter = 0
    view = ''
    for i in range(0, len(s)-k):
        new = s[i:k]
        for j in range(len(new)):
            if new[j] in vowels:
                old_counter += 1

        if new_counter < old_counter:
            new_counter = old_counter
        old_counter = 0
        k += 1
    if view:
        print('Full')


find_substring('find_substring', 5)
