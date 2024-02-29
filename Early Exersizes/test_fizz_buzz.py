from fizz_buzz import fizz_buzz
import pytest

def test_fizz_buzz_normal():
    """"Tests fizz_buzz function: normal result"""
    assert fizz_buzz(1) == 1
    assert fizz_buzz(2) == 2
    assert fizz_buzz(4) == 4


def test_fizz_buzz_multiples_3():
    """"Tests fizz_buzz function: multiples 3"""
    assert fizz_buzz(3) == "Fizz"
    assert fizz_buzz(2 * 3) == "Fizz"
    assert fizz_buzz(3 * 3) == "Fizz"
    assert fizz_buzz(4 * 3) == "Fizz"
    assert fizz_buzz(6 * 3) == "Fizz"


def test_fizz_buzz_multiples_5():
    """"Tests fizz_buzz function multiples 5"""
    assert fizz_buzz(5) == "Buzz"
    assert fizz_buzz(2 * 5) == "Buzz"
    assert fizz_buzz(4 * 5) == "Buzz"
    assert fizz_buzz(5 * 5) == "Buzz"
    assert fizz_buzz(7 * 5) == "Buzz"


def test_fizz_buzz_multiples_3_5():
    """"Tests fizz_buzz function multiples of both"""
    assert fizz_buzz(3 * 5) == "FizzBuzz"
    assert fizz_buzz(2 * 3 * 5) == "FizzBuzz"
    assert fizz_buzz(3 * 3 * 5) == "FizzBuzz"
    assert fizz_buzz(4 * 3 * 5) == "FizzBuzz"
    assert fizz_buzz(5 * 3 * 5) == "FizzBuzz"


def test_fizz_buzz_invalid():
    """"Tests fizz_buzz function: invalid"""
    with pytest.raises(ValueError):
        fizz_buzz(0)
        fizz_buzz(-1)
        fizz_buzz(-2)
        fizz_buzz(-3)
        fizz_buzz(-4)

