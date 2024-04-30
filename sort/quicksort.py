def quick(arr):
    pivot_idx = 0
    pivot = arr[pivot_idx]
    s = 0
    e = len(arr) - 1

    while s <= e:
        while s <= e:
            if arr[s] <= pivot:
                s += 1
            else:
                break
        while s <= e:
            if arr[e] >= pivot:
                e -= 1
            else:
                break
        if s <= e:
            arr[s], arr[e] = arr[e], arr[s]
            s += 1
            e -= 1

    if pivot_idx >= s:
        pivot_idx, arr[0], arr[s-1] = s-1, arr[s-1], pivot
    if pivot_idx <= e:
        pivot_idx, arr[0], arr[e] = e, arr[e], pivot
    
    if len(arr[0:pivot_idx]) > 1:
        arr[0:pivot_idx] = quick(arr[0:pivot_idx])
    if len(arr[pivot_idx+1:]) > 1:
        arr[pivot_idx+1:] = quick(arr[pivot_idx+1:])

    return arr
