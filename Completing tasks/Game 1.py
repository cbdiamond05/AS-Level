import random
mylist=["Rock","Paper","Scissors"]
a=random.sample(mylist,1)

no1=input("Enter Rock, Paper or Scissors: ")
if a==no1:
    print("I had ",a," you won")
else:
    print("I had ",a," you lost")