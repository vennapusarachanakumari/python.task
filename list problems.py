#sum of list

l=[10,20,60,30,40]
sum=0
for val in l:
    sum+=val
print(sum)

#product of list

l=[10,20,60,30,40]
prod=1
for val in l:
    prod=prod*val
print(prod)

#maximum list
l=[10,20,60,30,40]
max=0
for val in l:
    if max<val:
      max=val
print(max)

#minimum list

l=[10,20,60,30,40]
min=l[0]
for val in l:
    if min>val:
      min=val
print(min)

#length of list

l = [10, 20, 60, 30, 40]
print(len(l))