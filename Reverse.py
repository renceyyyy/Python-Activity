even = []
odd = []

for i in range(1, 21):
    if i % 2 == 0:
        even.append(i)
        if len(even) == 10:
            break
    else:
        odd.append(i)
        if len(odd) == 10:
            break
print("Reverse Even numbers")
for i in reversed(even):
    print(i)
print("Reverse Odd numbers")
for i in reversed(odd):
    print(i)
