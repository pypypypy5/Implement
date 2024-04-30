def selectionsort(li):
    for index_now in range(1,len(li)):
        for i in range(index_now,0,-1):
            if li[i] < li[i-1]:
                li[i], li[i-1] = li[i-1], li[i]
            else:
                break
