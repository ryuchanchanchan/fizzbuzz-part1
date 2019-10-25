number = int(input("1つの自然数を入れてね: "))

if number % 15 == 0:
    print("FizzBuzz")
elif number % 5 == 0:
    print("Buzz")
elif number % 3 == 0:
    print("Fizz")
else:
    print(str(number))

print(number)
