values_to_return= { 15 : "FizzBuzz", 7 : "Ruzz", 3 : "Fizz", 5 : "Buzz"}

# def fizz_buzz(number):
#     if number % 5 == 0 and fizz_numbers_division():
#         return "FizzBuzz"
#     elif number % 3 == 0:
#         return "Fizz"
#     elif number % 5 == 0:
#         return "Buzz"
#     else:
#         return str(number)



def fizzbuzz (number):
    for key in values_to_return:
        if number % key == 0:
            return values_to_return[key]
    return str(number)
        
