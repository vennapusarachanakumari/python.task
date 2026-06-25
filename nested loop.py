 #1 Sum of Digits
num = 1234
sum_digits = sum(int(digit) for digit in str(num))
print("Sum of digits:", sum_digits)
# 2. Reverse a Number
num = 1234
reverse_num = int(str(num)[::-1])
print("Reversed number:", reverse_num)
# 3. Count Digits in a Number
num = 12345
count = len(str(num))
print("Number of digits:", count)
# 4. Check Even or Odd
num = 17

if num % 2 == 0:
    print("Even")
else:
    print("Odd")
# 5. Check Prime Number
num = 13
if num > 1:
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            print("Not Prime")
            break
    else:
        print("Prime")
else:
    print("Not Prime")
# 6. Find Factorial of a Number
num = 5
factorial = 1

for i in range(1, num + 1):
    factorial *= i

print("Factorial:", factorial)
# 7. Find Factors of a Number
num = 12

print("Factors:")
for i in range(1, num + 1):
    if num % i == 0:
        print(i, end=" ")
# 8. Check Palindrome Number
num = 121

if str(num) == str(num)[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")
# 9. Check Armstrong Number
num = 153
power = len(str(num))

armstrong_sum = sum(int(digit) ** power for digit in str(num))

if armstrong_sum == num:
    print("Armstrong")
else:
    print("Not Armstrong")
# 10. Find GCD (HCF) of Two Numbers
a = 12
b = 18
while b:
    a, b = b, a % b

print("GCD:", a)
