#1Square Pattern
# n=4
# m=4
# for i in range(n):
#     for j in range(m):
#         print("*",end=" ")
#     print()
# #Right Triangle
# n=5
# for i in range(n):
#     for j in range(i+1):
#         print("*",end=" ")
#     print() 
# Number Triangle 1 1 2 1 2 3 1 2 3 4 1 2 3 4 5
# n=5
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(j,end=" ")
#     print() 
#Repeated Number Triangle 1 2 2 3 3 3 4 4 4 4 5 5 5 5 5
# n=5
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(i,end=" ")
#     print()
# #Alphabet Triangle A A B A B C A B C D A B C D E
# n=6
# for i in range(n):
#     val=65
#     for j in range(1,i+1):
#         print(chr(val),end=" ")
#         val+=1
#     print()
 
#Inverted Number Triangle 1 2 3 4 5 1 2 3 4 1 2 3 1 2 1
# n=5
# for i in range(n,0,-1):
#     for j in range(1,i+1):
#         print(j,end=" ")
#     print()
 
#Continuous Number Pattern 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15
# n=5
# val=1
# for i in range(1,n+1):
#     for j in range(i):
#         print(val,end=" ")
#         val+=1
#     print()
#Right-Aligned Star Triangle
#n = 5
# for i in range(1, n + 1):
#     for j in range(n - i):
#         print(" ", end=" ")
#     for k in range(i):
#         print("*", end=" ")
#     print()
#Pyramid Pattern
# n = 5
# for i in range(1, n + 1):
#     for j in range(n - i):
#         print(" ", end="")
#     for k in range(i):
#         print("*", end=" ")
#     print()
# n=4
# m=8
# for i in range(n):
#     for j in range(m):
#         print("*",end=" ")
#     print()

# n=8
# m=4
# for i in range(n):
#     for j in range(m):
#         print("*",end=" ")
#     print() 

# n=3
# for i in range(n):
#     for j in range(n):
#         print(i,j,end="  ")
#     print()

# n=3
# for i in range(n):
#     for j in range(n):
#         print(i,j,end="  ")
#     print()
  
# n=3
# for i in range(n):
#     for j in range(n):
#         print(i,end=" ")
#     print()

# n=3
# for i in range(n):
#     for j in range(n):
#         print(j,end=" ")
#     print()

# for ch in range(26):
#     print(chr(ch+65))

# for ch in range(26):
#     print(chr(ch+97)