def find_max(numberList):
    largest = 0
    for i in numberList:
        if i > largest:
            largest = i

    return largest
