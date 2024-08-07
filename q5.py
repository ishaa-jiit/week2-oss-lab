def lensort(arr):
    for i in range(0,len(arr)-1,1):
        for j in range(0,len(arr)-i-1):
            if len(arr[j])>len(arr[j+1]):
                arr[j],arr[j+1]=arr[j+1],arr[j]
    return arr

arr=["mszhb","agnia","te"]
print(lensort(arr))