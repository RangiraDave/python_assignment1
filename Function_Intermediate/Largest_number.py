n = int(input("How many elements is in you list? "))
x = []
print("Enter those elements:")
for i in range(n):
    a = int(input(" --> "))
    x.append(a)
def find_largest(y):
    Temp = 0
    for i in range(0, len(y)):
        if y[i] > Temp:
            Temp = y[i]
    return Temp
print(find_largest(x))