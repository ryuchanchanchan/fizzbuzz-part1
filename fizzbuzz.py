def fizzbuzz_convert(number):
    if number % 15 == 0:
        print("FizzBuzz")
    elif number % 5 == 0:
        print("Buzz")
    elif number % 3 == 0:
        print("Fizz")
    else:
        print(str(number))


fizzbuzz_convert(1)
fizzbuzz_convert(2)
fizzbuzz_convert(5)
fizzbuzz_convert(15)
fizzbuzz_convert(100)
