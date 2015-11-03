# TCSS 598 LIJUN XUE Soring Algos
# for calculate sortedness


def cal_inversion(target):
    # Use Merge Sort and calculate the Inversion number of the array
    # to measure the sortedness

    n = len(target)
    if n <= 1:
        return target, 0
    else:
        mid = n/2
        a1, left = cal_inversion(target[:mid])
        a2, right = cal_inversion(target[mid:])
        a, split = merge(a1, a2)
        # Divide original array into half size
        return a, (left + right + split)


def merge(a, b):
    # sort and merge 2 array
    c = []
    m1, m2 = 0, 0
    count = 0
    while m1<len(a) and m2<len(b):
        if a[m1] < b[m2]:
            c.append(a[m1])
            m1 += 1
        else:
            c.append(b[m2])
            m2 += 1
            count += (len(a) - m1)
    c += a[m1:]
    c += b[m2:]
    return c, count