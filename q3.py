def findDup(list):
    rep={}
    ans=[]
    for i in range(0,len(list),1):
        if(list[i] in rep):
            rep[list[i]] +=1
        else:
            rep[list[i]]=1
    for a in rep:
        if(rep[a]>1):
            ans.append(a)
    return ans

        
list=[10,20,30,10]
print(findDup(list))