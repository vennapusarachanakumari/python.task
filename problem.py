# #1.Print numbers from 1 to N:

# n=int(input("Enter a number: "))
# for i in range(1,n):
#     print(i)
# #2.sum of first N numbers:

# n=int(input("Enter a number: "))
# sum=0
# for i in range(1,n+1):
#     sum+=i
#     print(sum)
# #3.check even or odd

# n=int(input("enter a number:"))
# if n%2==0:
#     print("Even")
# else:
#     print("Odd")

# #4.check positive,negitive or zero

# n=int(input("Enter a number: "))
# if n>0:
#     print("Positive")
# elif n<0:
#     print("Negative")
# else:
#     print("Zero")

# #5.Find largest of 3 numbers

# a=int(input("Enter first number: "))
# b=int(input("Enter 2nd number:"))
# c=int(input("Enter 3rd number:"))
# if a>b and a>c:
#     print("a is largest")
# elif b>a and b>c:
#     print("b is largest")
# else:
#     print("c is largest")

# #6.check leap year

# n=int(input("Enter a number:"))
# if n%4==0 and n%100!=0 or n%400==0:
#     print("Leap year")
# else:
#     print("Not a leap year")
# #7.Multiplication table

# n=int(input("Enter a number: "))
# for i in range(1,11):
#     print(n,"*",i,"=",n*i)
# #8.factorial

# n=int(input("enter a number:"))
# fact=1
# for i in range(1,n+1):
#     fact*=i
# print(fact)

# #9.count digits in a number

# n=int(input("enter a number:"))
# count=0
# while n!=0:
#     n//=10
#     count+=1
# print(count)

# #10.reverse a number

# n=int(input("Enter a number: "))
# reverse=0
# while n>0:
#     temp=n%10
#     reverse=reverse*10+temp
#     n//=10
# print(reverse)

# #11.sum of digits

# n=int(input("enter a number:"))
# sum=0
# while n>0:
#     temp=n%10
#     sum+=temp
#     n//=10
# print(sum)

#12.check palindrome number

# n=int(input("enter a number:"))
# rem,rev=0,0
# temp=n
# while n>0:
#     rem=n%10
#     rev=rev*10+rem
#     n//=10
# if rev==temp:
#     print("palindrome")
# else:
#     print("not palindrome")

# #13.factors of a number

# n=int(input("Enter a number: "))
# for i in range(1,n+1):
#     if n%i==0:
#         print(i)

#14.check prime number

# n=int(input("enter a number:"))
# if n>1:
#  for i in range(2,n):
#     if n%i==0:
#         print("not prime")
#         break
#     else:
#         print("prime")
# else:
#     print("not prime")


#15.check armstrong number

# n=int(input("Enter a number: "))
# temp=n
# sum=0
# while n>0:
#     rem=n%10
#     sum+=rem**3
#     n//=10
# if sum==temp:
#     print("Armstrong number")
# else:
#     print("Not an Armstrong number")

#16.find GCD(HCF) of two numbers

# a=int(input("Enter first number: "))
# b=int(input("Enter 2nd number:"))
# while b!=0:
#     a,b=b,a%b
# print("GCD is",a)

#find strong number 145 1.separate individual digit-1 4 5 2.find factorial #1!=1,4!=24,5!=120 3.sum of fact #1+24+120=145 4.condition check

# n=145
# m=n
# sum=0
# while n>0:
#     temp=n%10
#     fact=1
#     while(temp>0):
#         fact*=temp
#         temp-=1
#     sum+=fact
#     n//=10
# if(sum==m):
#     print(m,"strong number")
# else:
#     print(m,"not strong number")
# #145 strong number
# for n in range(100,100000):
#     m=n
#     sum=0
#     while n>0:
#        temp=n%10
#        fact=1
#     while(temp>0):
#        fact*=temp
#        temp-=1
#     sum+=fact
#     n//=10
# if(sum==m):
#     print(m,"strong number")
# #Neon number find the given number 9 power 2 --81 8+1=9

# n=9 
# power=9**2
# sum=0
# while power>0:
#     temp=power%10
#     sum+=temp
#     power//=10
# print(sum)

#153--armstrong number find length of number 3 separate each number 1,5,3 1 pow len of number--->1pow3+5pow3+3pow3 sum check condition
# n=153
# sum=0
# length=len(str(n))
# r=n
# while n>0:
#     temp=n%10
#     sum+=temp**length
#     n//=10
# if sum==r:
#     print(r,"Armstrong number")
# else:
#     print(r,"Not an Armstrong number")

# #automorphic number any value pow 2 n=25 25pow 2--->625 last number n

# t=(1,4,2,2,3,4,5,3)
# d={}
# for key in t:
#     d[key]=d.get(key,0)+1
# print(d)
# {1: 1, 4: 2, 2: 2, 3: 2, 5: 1}

#unique number of occurences like true or false
# arr=[1,4,2,2,3,4,5,3]
# d={}
# for key in arr:
#     d[key]=d.get(key,0)+1
# l=list(d.values())
# uniq=set(l)
# print(uniq)
# for i in uniq:
#     if l.count(i)>1:
#         print("False")
#         break
# else:
#     print("True")

# arr=[1,4,2,2,3]
# d={}
# for key in arr:
#     d[key]=d.get(key,0)+1
# l=list(d.values())
# for i in range(1,len(l)):
#     if(l.count(l[i])>1):
#         print(False)
# print(True)

# x="5"
# y=2
# print(x*y)



# n=153
# sum=0
# length=len(str(n))
# r=n
# while n>0:
#     temp=n%10
#     sum+=temp**length
#     n//=10
# if sum==r:
#     print("True")
# else:
#     print("False")



#single number

# l=[1,1,2,3,3]
# for i in range(len(l)):  #0<5
#     if (l.count(l[i])==1): #1->2==1,2->1==1
#         print(l[i]) #2




