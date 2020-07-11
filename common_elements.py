def common_elements(a,b):
    p1 = 0
    p2 = 0
    result = []

    while p1 < len(a) and p2 < len(b):
        if a[p1] == b[p2]:
            result.append(a[p1])
            p1 += 1
            p2 += 2
        elif a[p1] < b[p2]:
            p2 += 1
        else:
            p1 += 1
    return result

print(common_elements([1,24,53,2,3,5,7,], [1,23,45,2,7,8]))
