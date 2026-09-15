#Create a program that will calculate the factorial 
number = int(input("enter a non-negative number : "))
factorial = 1
for i in range(1,number + 1):
    factorial = factorial * i
print("factorial is : ", factorial)