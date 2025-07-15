for num in range(1,100+1):
    if num%5 == num%3 == 0:
        print('FIZZBUZZ')
    elif num%5 == 0:
        print('Buzz')
    elif num%3 == 0:
        print('Fizz')
    else:
        print(num)
