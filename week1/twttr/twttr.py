str = input("Input: ")

vowels = "aeouiAIOUE"
result = ""

for char in str:
    if char not in vowels:
        result += char

print("Output: ", result)