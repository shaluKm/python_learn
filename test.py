print("Hello world")

sum = 0

def normalSum():
    global sum
    for x in range(10):
        sum += x
    return sum



print(normalSum())