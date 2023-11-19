#Linear search
mylist=[2,56,3,45,43,5]
searchItem=int(input("Enter the number you would like to find: "))

found=False
end=len(mylist)-1

for i in range(0,end): #goes through the list and compares each number to the searchItem to find the number wanted
    if mylist[i]==searchItem:
        print("Your item was found in position ",i)
        found=True
if mylist==False:#if the searchItem is not in the list it will then print number not found
    print("Your number has not been found")


#Binary search
mylist=[2,3,5,43,45,56]
searchItem=int(input("Enter the number you would like to find: "))

found =False
start=0
end=len(mylist)-1

while start<=end and found==False:  # checks if the list has been fully checked and if the searchItem has been found
    midpoint = (start+end) //2  #splits the list in half
    if mylist[midpoint] == searchItem:  #checks if the number at the midpoint is equal to the searchItem
        found=True
    else:
        if mylist[midpoint]<searchItem:  #checks if the searchItem is greater than the midpoint
            start=midpoint+1  #if so it disregards the earlier half of the list 
        else:
            end=midpoint-1  #if not it disregards the later half of the list
if found==True:
    midpoint=midpoint+1
    print("Your number has been found at position",midpoint)
else:
    print("Your number has not been found")

