import pprint
from itertools import permutations


def sort(a):
    n = len(a)
    cnt = 0
    for j in range(1, n):
        x = a[j]
        i = j - 1
        while (i >= 0) and (a[i] > x):
            cnt += 1
            a[i + 1] = a[i]
            i -= 1
            # print(cnt, a)
        a[i + 1] = x
    return cnt


# print (sort([5,1,2,3,4]))
def mixedSort(n):
    dict = {}
    l = list(permutations(range(1, n + 1)))
    res = [list(ele) for ele in l]
    m = 0
    for li in res:
        original = li.copy()
        t = sort(li)
        if t not in dict:
            dict[t] = [original]
        else:
            dict[t].append(original)
    return dict


pprint.pprint(mixedSort(5))
