n = int(input("Enter a number to check wheter it's Prime or not: "))
for i in range(2, n):
    if n % i == 0:
        print("Not Prime number")
        break
    else:
        print("It is Prime")
        break