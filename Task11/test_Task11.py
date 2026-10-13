from Task11 import *
import pytest

## PALINDROME CHECKER ##

def test_palindrome_check():
    assert(palindrome_check("apple")) == False
    assert(palindrome_check("radar")) == True
    assert(palindrome_check("a")) == True
    assert(palindrome_check("rAdAr")) == True

## ANAGRAM ##

def test_palindrome_check():
    assert(anagram_check("list","lists")) == False
    assert(anagram_check("silent","listen")) == True
    assert(anagram_check("","empty")) == False
    assert(anagram_check("a","b")) == False
    assert(anagram_check("A","a")) == True


## FIZZBUZZ ##

def test_fizzbuzz():
    assert fizzbuzz(3)[-1] == "Fizz"
    assert fizzbuzz(5)[-1] == "Buzz"
    assert fizzbuzz(15)[-1] == "FizzBuzz"
    assert fizzbuzz(7)[-1] == "7"
    with pytest.raises(ValueError):
        fizzbuzz(0)
    with pytest.raises(ValueError):
        fizzbuzz(-2)
    with pytest.raises(ValueError):
        fizzbuzz(3.2)
    assert fizzbuzz(6) == ["1","2","Fizz","4","Buzz","Fizz"]

## TEMP CONVERSION ##

def test_celsius_to_fahrenheit():
    assert celsius_to_fahrenheit(40) == 104
    assert celsius_to_fahrenheit(0) == 32
    assert celsius_to_fahrenheit(100) == 212
    assert celsius_to_fahrenheit(-40) == -40
    assert celsius_to_fahrenheit(37.5) == pytest.approx(99.5)
    
    
def test_fahrenheit_to_celsius():
    assert fahrenheit_to_celsius(32) == 0
    assert fahrenheit_to_celsius(212) == 100
    assert fahrenheit_to_celsius(-40) == -40
    assert fahrenheit_to_celsius(celsius_to_fahrenheit(13)) == 13

## PASSWORD VALIDATOR ##

def test_password_check():
    assert password_check("Password1!") == True       # Valid password
    assert password_check("Pass1!") == False          # Too short
    assert password_check("password1!") == False      # No uppercase
    assert password_check("PASSWORD1!") == False      # No lowercase
    assert password_check("Password!!") == False      # No digit
    assert password_check("Password12") == False      # No special


## BACNK ACCOUNT ##

def test_banking():
    account = BankAccount(100)
    assert account.get_balance() == 100

    account.deposit(50)
    assert account.get_balance() == 150

    account.withdraw(30)
    assert account.get_balance() == 120

    with pytest.raises(ValueError):
        account.deposit(0)

    with pytest.raises(ValueError):
        account.deposit(-10)

    with pytest.raises(ValueError):
        account.withdraw(-10)

    # Test withdrawing more than the balance
    with pytest.raises(ValueError):
        account.withdraw(200)

    assert account.get_balance() == 120

from Task11 import *
import pytest

## PALINDROME CHECKER ##

def test_palindrome_check():
    assert(palindrome_check("apple")) == False
    assert(palindrome_check("radar")) == True
    assert(palindrome_check("a")) == True
    assert(palindrome_check("rAdAr")) == True

## ANAGRAM ##

def test_palindrome_check():
    assert(anagram_check("list","lists")) == False
    assert(anagram_check("silent","listen")) == True
    assert(anagram_check("","empty")) == False
    assert(anagram_check("a","b")) == False
    assert(anagram_check("A","a")) == True


## FIZZBUZZ ##

def test_fizzbuzz():
    assert fizzbuzz(3)[-1] == "Fizz"
    assert fizzbuzz(5)[-1] == "Buzz"
    assert fizzbuzz(15)[-1] == "FizzBuzz"
    assert fizzbuzz(7)[-1] == "7"
    with pytest.raises(ValueError):
        fizzbuzz(0)
    with pytest.raises(ValueError):
        fizzbuzz(-2)
    with pytest.raises(ValueError):
        fizzbuzz(3.2)

## TEMP CONVERSION ##

def test_celsius_to_fahrenheit():
    assert celsius_to_fahrenheit(40) == 104
    assert celsius_to_fahrenheit(0) == 32
    assert celsius_to_fahrenheit(100) == 212
    assert celsius_to_fahrenheit(-40) == -40
    assert celsius_to_fahrenheit(37.5) == pytest.approx(99.5)
    
    
def test_fahrenheit_to_celsius():
    assert fahrenheit_to_celsius(32) == 0
    assert fahrenheit_to_celsius(212) == 100
    assert fahrenheit_to_celsius(-40) == -40
    assert fahrenheit_to_celsius(celsius_to_fahrenheit(13)) == 13

## PASSWORD VALIDATOR ##

def test_password_check():
    assert password_check("Password1!") == True       # Valid password
    assert password_check("Pass1!") == False          # Too short
    assert password_check("password1!") == False      # No uppercase
    assert password_check("PASSWORD1!") == False      # No lowercase
    assert password_check("Password!!") == False      # No digit
    assert password_check("Password12") == False      # No special


## BACNK ACCOUNT ##

def test_banking():
    account = BankAccount(100)
    assert account.get_balance() == 100

    account.deposit(50)
    assert account.get_balance() == 150

    account.withdraw(30)
    assert account.get_balance() == 120

    with pytest.raises(ValueError):
        account.deposit(0)

    with pytest.raises(ValueError):
        account.deposit(-10)

    with pytest.raises(ValueError):
        account.withdraw(-10)

    # Test withdrawing more than the balance
    with pytest.raises(ValueError):
        account.withdraw(200)

    assert account.get_balance() == 120


## COWS AND BULSS ##

def test_win_cows_and_bulls():
    game = CowsAndBulls("1234")
    assert game.current_state() == "ongoing"
    assert game.guess("4321") == "0 - 4"
    assert game.guess("1111") == "1 - 0"
    assert game.guess("1234") == "4 - 0"
    assert game.current_state() == "finished"

def test_guess_after_finished_cows_and_bulls():
    game = CowsAndBulls("1234")
    game.guess("1234")
    with pytest.raises(ValueError):
        game.guess("5678")

def test_invalid_guess_cows_and_bulls():
    game = CowsAndBulls("1234")
    with pytest.raises(ValueError):
        game.guess("12")
    with pytest.raises(ValueError):
        game.guess("12345")

def test_creation_cows_and_bulls():
    game = CowsAndBulls()
    assert len(game.number) == 4
    assert game.number.isdigit()
    assert game.current_state() == "ongoing"
    assert game.guess_count == 0
