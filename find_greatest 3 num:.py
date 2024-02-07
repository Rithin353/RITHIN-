def find_greatest(num1, num2, num3):
    return max(num1, num2, num3)

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))

greatest = find_greatest(num1, num2, num3)
print("The greatest of the three numbers is:", greatest)