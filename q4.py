def group(list,size):
    ans=[]
    for i in range(0,len(list),size):
        ans.append(list[i:i+size])
    return ans

list=[1,2,346,2412,121,468]
print(group(list,3))

