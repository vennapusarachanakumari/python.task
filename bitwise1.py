a = 5
b = 5
print(a ^ b)
#2. XOR Operation (Different Values)
a = 5
b = 3
print(a ^ b)
#3. AND Operation
a = 5
b = 3
print(a & b)
#4. Is 1 Even or Odd?
n = 1
if n % 2 == 0:
    print("Even")
else:
    print("Odd")
#Using Bitwise AND:
n = 1
if n & 1:
    print("Odd")
else:
    print("Even")    
#Practice All Bitwise Operators
a = 5   # 0101
b = 3   # 0011
print("AND :", a & b)
print("OR  :", a | b)
print("XOR :", a ^ b)
print("NOT a :", ~a)
print("Left Shift :", a << 1)
print("Right Shift:", a >> 1)    