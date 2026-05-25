def reverseString(s):
    if len(s) == 1:
        return s[0]
    return reverseString(s[1:]) + s[0]
s = "Ankit Jadli"
print(reverseString(s))