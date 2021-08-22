largest = 0
numberList = [1, 25, 15, 25, 38, 100, 35]

for i in numberList:
    if i > largest:
        largest = i

print(f'The greatest number of the list is {largest}')
