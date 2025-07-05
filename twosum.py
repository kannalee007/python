s = input("Enter first word: ").replace(" ", "").lower()
t = input("Enter second word: ").replace(" ", "").lower()

dict_s = {}
for char in s:
    if char in dict_s:
        dict_s[char] += 1
    else:
        dict_s[char] = 1

dict_t = {}
for char in t:
    if char in dict_t:
        dict_t[char] += 1
    else:
        dict_t[char] = 1

if dict_s == dict_t:
    print("YES — They are anagrams!")
else:
    print("NO — They are not anagrams.")
