
def readnumbers():
    total = 0
    counter = 0
    average = 0
    while True:
        numbers = input('enter a number: \n')
        if numbers == 'done':
            break
        try:
            total += int(numbers)
            counter += 1
        except:
            print('invalid input')
    average = total/counter
    cache = total,counter,average
    return cache

print(readnumbers())


