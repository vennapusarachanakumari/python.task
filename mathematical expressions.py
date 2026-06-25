#1.Write a program to find the area of a Rectangle
# l=20
# b=12
# area=l*b
# print(area)
# #2.Write a program to find the area of a square
# side=12
# area=side*side
# print(area)/
#3.Write a program to find the area of a traingle
# b=34
# h=45
# a=1/2*b*h
# print(a)
# #4.Write a program to find the area of a circle
# r=23
# pi=3.14
# a=pi*r**r
# print(a)
# #5.Write a program to find the area of a parallelogram
# b=23
# h=12
# a=b*h
# print(a)
# #6.Write a program to find the area of a rhombus
# d1=12
# d2=23
# a=1/2*d1*d2
# print(a)
#7.Write a program to find the area of a trapezium
# a=12
# b=23
# h=21
# a=1/2*(a+b)*h
# print(a)
# 8.Write a program to find the area of an equilateral triangle
# import math
# a=10
# area=(math.sqrt(3)/4*a**2)
# print(area)
# 9.Write a program to find the area of a sector of a circle
# pi=3.14
# r=3
# theta=60
# a=(theta/360)*pi*r**r
# print(a)
# 10.Write a program to find the area of a semicircle
# pi=3.14
# r=3
# a=1/2*pi*r**r
# print(a)
# Parimeter Problems
# 1.Write a program to find the perimeter of a rectangle
# l=7
# b=2
# per=2*(l+b)
# print(per)
# 2.Write a program to find the perimeter of a square
# side=7
# per=4*side
# print(per)
# 3.Write a program to find the perimeter of a triangle
# a=6
# b=8
# c=4
# perimeter=a+b+c
# print(perimeter)
#4.Write a program to find the circumference of a circle
# pi=3.14
# # r=12
# per=2*pi*r
# print(per)
# 5.Write a program to find the perimeter of a parallelogram
# a=6
# b=7
# per=2*(a+b)
# print(per)
# 6.Write a program to find the perimeter of a rhombus
# a=8
# per=4*a
# print(per)
# #7.Write a program to find the perimeter of a regular pentagon
# a=34
# per=5*a
# print(per)
# #8.Write a program to find the perimeter of a regular hexagon
# a=8
# per=6*a
# print(per)
# #9.Write a program to find the perimeter of a trapezium
# a=11
# b=6
# c=2
# d=8
# per=a+b+c+d
# print(per)
# #10.Write a program to find the perimeter of an equilateral triangle
# a=7
# per=3*a
# print(per)
# #Cube Problems
# #1.write a program to find the volume of a cube
# a=2
# vol=a**3
# print(vol)
# #2.write a program to find the surface area of a cube
# a=3
# sur=6*a**2
#print(sur)
#3.write a program to find the lateral surface area of a cub
# a=5
# lsa=4*a**2
# print(lsa)
# 100
# #4.write a program to find the cube of a given number
# a=6
# cube=a**3
# print(cube)
# #5.write a program to check whether a number ia a perfect cube
# n=34
# cube=n**(1/3)
# print(cube)
# 3.239611801277483
# #6.write a program to find the sum of cubes of two numbers
# a=3
# b=4
# cubes=a**3+b**3
# print(cubes)
# 7.write a program to find the difference of cubes of two numbers
#3.write a program to find the lateral surface area of a cube
# a=5
# lsa=4*a**2
# print(lsa)
#4.write a program to find the cube of a given number
# a=6
# cube=a**3
# print(cube)
# #5.write a program to check whether a number ia a perfect cube
# n=34
# cube=n**(1/3)
# print(cube)
#6.write a program to find the sum of cubes of two numbers
# a=3
# b=4
# cubes=a**3+b**3
# print(cubes)
#7.write a program to find the difference of cubes of two numbers
a = 3
b = 4
cubes = a**3 - b**3
print(cubes)
#8.write a program to print cubes from 1 to N
n=int(input("Enter a number: "))
for i in range(1,n):
    print(i**3)
#9.write a program to find the cube root of a number
n = float(input("Enter a number: "))
cube_root = n ** (1/3)
print(cube_root)
#10.write a program to find the largest cube less than or equal to N
N = int(input("Enter a number: "))
i = 1
while i**3 <= N:
    i += 1
print((i-1)**3)

