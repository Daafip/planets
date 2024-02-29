# The function `fizz_buzz()` takes an integer argument and returns it, BUT:
#
# - It fails on zero or negative numbers
# - It returns "Fizz" on multiples of 3
# - It returns "Buzz" on multiples of 5
# - It instead returns "FizzBuzz" on multiples of 3 and 5


def fizz_buzz(val):
    if valid_number(val):
        if val % 3 == 0:
            return "Fizz"
        elif val % 5 == 0:
            return "Buzz"
        else: return val




def valid_number(val):
    if val > 0:
        return True
    else:
        return False