def factorial(n):
    if n == 1:
        return n
    else:
        return n * factorial (n - 1)
    
print(factorial(4))

def countdown(n):
    if n =n= 0:
        print("0")
    else:
        print(n)
        countdown(n - 1)
    
countdown(6)