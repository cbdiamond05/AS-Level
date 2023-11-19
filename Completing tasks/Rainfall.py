rainfall=[45,12,10,15,30,25,36,17,6,20,32,38]
totalrain=0
meanrain=0
months=0
for i in range(12):
    totalrain=totalrain+rainfall[i]
meanrain=totalrain/12  


aboveMean=[]
for i in range(12):
    months=months+1
    if rainfall[i]>meanrain:
        aboveMean.append(months)

print(totalrain)
print(meanrain)
print(aboveMean)  