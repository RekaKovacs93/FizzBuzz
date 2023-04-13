#values_to_return= {3 : "Fizz", 5 : "Buzz", 15 : "FizzBuzz"}
div_return_fizz = [3]
def fizz_buzz(number):
    if number % 5 == 0 and fizz_numbers_division():
        return "FizzBuzz"
    elif number % 3 == 0:
        return "Fizz"
    elif number % 5 == 0:
        return "Buzz"
    else:
        return str(number)

def fizz_numbers_division (number):
    for num in div_return_fizz:
        if number % num == 0:
            return True
def add_fizz_numbers(number):
    div_return_fizz.append(number)