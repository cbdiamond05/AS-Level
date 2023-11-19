mylist=[]
mean=0
count=0
analysed=int(input("Enter the number of readings to be analysed: "))
for i in range(analysed):
    reading=int(input("Enter the number: "))
    mean=mean+reading
    mylist.append(reading)
meanTotal=mean//analysed

for i in range(analysed):
    if reading>meanTotal:
        count=count+1

print(mylist)
print(meanTotal)
print(count)
print(max(mylist))

no1=int(input("Enter number 1: "))
no2=int(input("Enter number 2: "))
no3=int(input("Enter number 3: "))
totalNo=no1+no2+no3
if totalNo//3 and =! MOD and totalNo#