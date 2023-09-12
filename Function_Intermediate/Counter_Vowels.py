s = input("Enter  the string: ")
b = 0
def count_vowels(a):
    a = 0
    for i in range(0, len(s)):
        if s[i] == 'i' or s[i] == 'u' or s[i] == 'o' or s[i] == 'a' or s[i] == 'e':
            a += 1
    return a
print(count_vowels(b))