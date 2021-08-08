#program to print positive numbers only from input list

n=int(input('Enter number of elements in a lis: '))
inputlist=[]

for i in range(n):
    k=int(input('Enter list element: '))
    inputlist.append(k)
    
print("Positive elements from list are:")

for i in inputlist:
    if i>=0:
        print(i)
                     
                     
