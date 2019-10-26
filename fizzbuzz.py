def fizzbuzz_convert(number):
    if number % 15 == 0:
        return "FizzBuzz"
    elif number % 5 == 0:
        return "Buzz"
    elif number % 3 == 0:
        return "Fizz"
    else:
        return str(number)


result = fizzbuzz_convert(1)
print(result)
result = fizzbuzz_convert(2)
print(result)

result = fizzbuzz_convert(5)
print(result)

result = fizzbuzz_convert(15)
print(result)

result = fizzbuzz_convert(100)
print(result)
