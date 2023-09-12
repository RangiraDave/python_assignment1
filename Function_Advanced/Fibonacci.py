n = int(input("Enter a number for Fibonacci Series: "))
a = 0
b = 1
if n < 0:
    print("Enter a positive number.")

else:
    for i in range(0,n):
        print(a)
        fibo = a + b
        a = b
        b = fibo
        