num = 153
temp = num

# Find length of the number
count = 0
while temp > 0:
    count = count + 1
    temp = temp // 10

temp = num
sum = 0

# Separate digits and find power
while temp > 0:
    digit = temp % 10
    sum = sum + (digit ** count)
    temp = temp // 10

# Check Armstrong
if sum == num:
    print(num, "is an Armstrong Number")
else:
    print(num, "is Not an Armstrong Number")