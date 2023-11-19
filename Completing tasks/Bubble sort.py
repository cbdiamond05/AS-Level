mylist=[1,12,32,4,23,19,78,6]

n=len(mylist)
swapped=True

while n>0 and swapped==True:
    swapped=False
    n=n-1
    for i in range(0,n):
        if mylist[i]>mylist[i+1]:
            store=mylist[i]
            mylist[i]=mylist[i+1]
            mylist[i+1]=store
            swapped=True
print(mylist)