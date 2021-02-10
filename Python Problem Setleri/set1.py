a = range(0, 100)
for sayi in a:
    if sayi % 3 == 0:
        if sayi % 5 == 0:
            print("FizzBuzz", end=",")
        else:
            print("Fizz", end=",")
    elif sayi % 5 == 0:
        print("Buzz", end=",")
    else:
        print(sayi, end=",")
