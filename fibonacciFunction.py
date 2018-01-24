def fib(n):
    """ Print a Fibonocci series up to n."""
    a,b = 0,1
    while a < n:
            print(a, end=' ')
            a,b = b, a+b
    print()



#
# testing function
#
try:
    #calling function.
    fib(int(input("Please enter max number. ")))
    input()
except ValueError:
    print("This is not a valid number. Please try again.")
    input()
    
    
    


