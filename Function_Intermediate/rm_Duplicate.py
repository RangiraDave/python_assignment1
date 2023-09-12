s = []
n = int(input("How many elements do you have? "))

def remove_duplicate(L):
    for i in range(0, n):
        a = input("Enter the element: ")
        if a in L:
            pass
        else:
            L.append(a)
    return L
print(remove_duplicate(s))
