def reverseNumber(num):
    if num < 10:
        return num
    return int(str(num % 10) + str(reverseNumber(num // 10)))
n = int(input("Enter number: "))
print("Reversed:", reverseNumber(n))