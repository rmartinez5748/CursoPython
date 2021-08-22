numbers = [4, 8, 12, 16, 20, 4, 8]
sorted = []

for num in numbers:
    if num not in sorted:
        sorted.append(num)

print(sorted)
