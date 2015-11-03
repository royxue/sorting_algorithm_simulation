# TCSS 598 LIJUN XUE Soring Algos
# for different algorithms comparasion

import generater
import time


def insertionsort(target):
    n = len(target)
    for i in range(1, n):
        temp = target[i]
        j = i - 1
        while j >= 0 and target[j] > temp:
            target[j+1] = target[j]
            j -= 1
        target[j+1] = temp

    return target


def selectionsort(target):
    n = len(target)
    for i in range(n-1):
        minid = i
        for j in range(i+1, n):
            if target[j] < target[minid]:
                minid = j
        temp = target[i]
        target[i] = target[minid]
        target[minid] = temp

    return target


def bubblesort(target):
    n = len(target)
    for i in range(n, 0, -1):
        for j in range(0, i-1):
            if target[j] > target[j+1]:
                temp = target[j]
                target[j] = target[j+1]
                target[j+1] = temp

    return target


def mergesort(target):
    n = len(target)
    if n <= 1:
        return target
    else:
        mid = n/2
        a1 = mergesort(target[:mid])
        a2 = mergesort(target[mid:])
        # Divide original array into half size
        return merge(a1, a2)


def merge(a, b):
    # sort and merge 2 array
    c = []
    m1, m2 = 0, 0
    while m1<len(a) and m2<len(b):
        if a[m1] < b[m2]:
            c.append(a[m1])
            m1 += 1
        else:
            c.append(b[m2])
            m2 += 1
    c += a[m1:]
    c += b[m2:]
    return c


def quicksort(target):
    n = len(target)
    if n <= 1:
        return target
    else:
        pivot = target[1]
        a1 = quicksort([x for x in target[1:] if x < pivot])
        a2 = quicksort([x for x in target[1:] if x >= pivot])
        return (a1+[pivot]+a2)


def calculate_time_size():
    data = generater.Datasets().list
    result = {}
    sort = [insertionsort, selectionsort, bubblesort, mergesort, quicksort]
    for dataset in data:
        name = str(len(dataset)) + str(type(dataset[0]))
        result[name] = {}
        for func in sort:
            times = []
            eachtime = []
            result[name][str(func)] = []
            for j in range(1, 5):
                x = (j*len(dataset))/4
                target = dataset[:x]
                for i in range(5):
                    start = time.time()
                    func(target)
                    end = time.time()
                    eachtime.append(end-start)
                times.append(numpy.mean(eachtime))
            result[name][str(func)].append(times)

    return result


if __name__ == "__main__":
    print calculate_time_size()

