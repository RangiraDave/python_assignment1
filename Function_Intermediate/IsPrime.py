n = int(input("Enter a number: "))
a = ''
def is_prime(printl):
    if n < 1:
        printl = "Entered a Non-positive numbe."
    elif n == 1:
        printl = "Prime"
    elif n > 1:
        for i in range(2,n):
            if n % i == 0:
                printl = "Not Prime."
            else:
                printl = "It is Prime."
    return printl
print(is_prime(a))