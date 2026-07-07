'''
# print a continuous number triangle?
n = 6
num = 3

for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(num, end=" ")
        num += 1
    print()


# print a increasing number of triangle?
n = 5
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()    


# print a repeated number of triangle?
n = 5
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(i, end=" ")
    print()    
    

# print a reverse number triangle?
n = 5
for i in range(n, 0, - 1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()    


# print a revers repeated number pattern?
n = 5
for i in range(n, 0, -1):
    for j in range(i):
        print(i, end=" ")
    print()    
    
# print a revers counting pattern?
n = 5
for i in range(1, n + 1):
    for j in range(i, 0, -1):
        print(j, end=" ")
    print()  
    
# print a right aligned number triangle?
n = 5
for i in range(1, n + 1):
    print(" " * (n - i), end=" ")
    for j in range(1, i + 1):
        print(i, end=" ")
    print()   
    
# print a number pyramid pattern ?
n = 5
for i in range(1, n + 1):
    print(" " * (n - i), ends=" ")
    for j in range(1, i + 1):
        print(j, end=" ")
        
# print a decreasing number triangle?
n = 5
for i in range(1, n + 1):
    for j in range(n, n - i, -1):
        print(j, end=" ")
    print()         
    
# print a palindrom number pattern?
n = 5
for i in range(1, n + 1):
    for j in range(i, 0, -1):
        print(j, end=" ")
    for j in range(2, i + 1):
        print(j, end=" ")
    print()      
'''     

# print a  constant number sequence pattern?    
n = 5
for i in range(1, n + 1):
    for j in range(1, 0, -1):
        print(j, end=" ")
    for j in range(2, n + 1):
        print(j, end=" ")
    print()             
    
# print a row-wise constant repetition pattern?
n = 5
for i in range(1, n + 1):
    for j in range(1, 0, -1):
        print(i, end=" ")
    for j in range(2, n + 1):
        print(i, end=" ")
    print()    

# print a  a vertical number sequence pattern?
n = 5
for i in range(1, n + 1):
    for j in range(1, 0, -1):
        print(i, end=" ")
    print()    

# print a  simple number sequence pattern? 
n = 5
num = 1
for i in range(1, n + 1):
    print(num, end=" ")
    num += 1
print()    


# print pyramid style * structure?
n = 5
for i in range(1, n + 1):
    print(" " * (n - i), end="")
    print("* " * i)


# print butter fly pattern * structure?
n = 5

# Upper half
for i in range(1, n + 1):
    # Left wing
    for j in range(1, i + 1):
        print("*", end=" ")
    
    # Spaces between wings
    for j in range(2 * (n - i)):
        print(" ", end=" ")
    
    # Right wing
    for j in range(1, i + 1):
        print("*", end=" ")
    print()

# Lower half
for i in range(n, 0, -1):
    # Left wing
    for j in range(1, i + 1):
        print("*", end=" ")
    
    # Spaces between wings
    for j in range(2 * (n - i)):
        print(" ", end=" ")
    
    # Right wing
    for j in range(1, i + 1):
        print("*", end=" ")
    print()



