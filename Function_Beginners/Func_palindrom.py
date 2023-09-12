S = input("Enter a string: ")
def Palindrome(a):
    Temp = S[::-1]
    for i in range(0, len(S) - 1):
        if Temp[i] == S[i]:
            Ans = 'True'
        else:
            Ans = 'False'
    return Ans
print(Palindrome(S))