#python program for first n fibonacci numbers

def fib(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return (fib(n-1)+fib(n-2))


n=int(input('Enter any positive integer: '))
for x in range(n):
    print(fib(x))
      
    
