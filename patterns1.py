# Find length of number
num = int(input("Enter a number: "))
temp = num

length = len(str(num))
sum = 0

# Separate each digit and calculate digit^length
while temp > 0:
    digit = temp % 10      # Separate each digit
    sum = sum + (digit ** length)
    temp = temp // 10

# Check condition
if sum == num:
    print(num, "is an Armstrong Number")
else:
    print(num, "is Not an Armstrong Number")