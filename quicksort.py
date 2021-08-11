def quickSort(arr):
    if len(arr) < 2:
        return arr[:]
    else:
        pivot = arr[0]
        smaller, bigger = partition(arr[1:], pivot)
        smaller = quickSort(smaller)
        bigger = quickSort(bigger)
        return smaller + [pivot] + bigger


def partition(arr, pivot):
    smaller = []
    bigger = []
    for item in arr:
        print('*', end='')
        if item <= pivot:
            smaller.append(item)
        else:
            bigger.append(item)
    return smaller, bigger


print(quickSort([6, 1, 5, 4, 2]))
a = list(range(1, 100))
