n = int(input("Enter a number: "))
pro = 1
def Factorial(n):
    pro = 1
    for i in range(1, n + 1):
        pro *= i
    return pro
fact = Factorial(n)
print(f"The factorial for {n} is:  ", end = "")
for j in range(n, 1, -1):
    print(j, " X ", end = "")
print("1 = ", fact)