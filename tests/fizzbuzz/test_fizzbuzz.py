from src.fizzbuzz.fizzbuzz import Fizzbuzz


def test_should_return_fizz_if_number_is_divisible_by_3():
    assert Fizzbuzz.run_fizzbuzz(3) == "fizz"
    assert Fizzbuzz.run_fizzbuzz(6) == "fizz"


def test_should_return_the_same_number_if_it_does_not_meet_the_conditions():
    assert Fizzbuzz.run_fizzbuzz(2) == "2"
    assert Fizzbuzz.run_fizzbuzz(4) == "4";


def test_should_return_buzz_if_number_is_divisible_by_5():
    assert Fizzbuzz.run_fizzbuzz(5) == "buzz"
    assert Fizzbuzz.run_fizzbuzz(10) == "buzz"


def test_should_return_fizzbuzz_if_number_is_divisible_by_15():
    assert Fizzbuzz.run_fizzbuzz(15) == "fizzbuzz"
    assert Fizzbuzz.run_fizzbuzz(45) == "fizzbuzz"
