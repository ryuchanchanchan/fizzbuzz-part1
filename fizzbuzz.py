def fizzbuzz_convert(number):
    if number % 15 == 0:
        return "FizzBuzz"
    if number % 5 == 0:
        return "Buzz"
    if number % 3 == 0:
        return "Fizz"

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
