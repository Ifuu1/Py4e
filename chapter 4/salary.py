def computepay():
    hours = int(input('enter hours\n'))
    rate = float(input('enter rate\n'))
    pay = 40 * rate


    if hours > 40:
        overtime = hours - 40
        totalpay = pay + ((overtime * rate) * 1.5)

    else:
        totalpay = pay

    return totalpay

    # print('please pay',totalpay)

payment = computepay()
print('Pay', payment)

