n = input()
y = n.lower()
str1 = y.split()
print(str1)

reverse = lambda i : i[::-1]

res = list(map(reverse, str1))

capitalized_res = [word.capitalize() for word in res]

final_str = ' '.join(capitalized_res)

print(final_str)