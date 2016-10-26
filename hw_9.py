def positive_sum(arr):
    a = 0
    if len(arr) > 1:
        for i in range(len(arr)):
            if arr[i] >= 0:
                a = a + arr[i]
                i = i + 1
            elif arr[i] < 0:
                i = i + 1
        return a
    else:
        return 0