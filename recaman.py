




def recaman(n):
 
    arr = [0] * n
 
    arr[0] = 0

    check = [0] * n
 
    for i in range(1, n):
     
        curr = arr[i-1] - i
        for j in range(0, i):
            if ((arr[j] == curr) or curr < 0):
                curr = arr[i-1] + i
                break
             
        arr[i] = curr

    for i in range(1,len(arr)):
        try:
            temp = arr[i-1]
            if temp > arr[i]:
                check[i] = 1
        except IndexError:
            pass

    return arr, check


print(recaman(12))
