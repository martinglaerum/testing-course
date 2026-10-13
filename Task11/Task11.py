#### TASK 11 ####
import random

## PALINDROME CHECKER ##

def palindrome_check(text):
    text = text.upper()
    text = ''.join(char for char in text if char.isalnum())
    reversed_text = text[::-1]
    if reversed_text == text:
        return True
    else:
        return False

## ANAGRAM ##

def anagram_check(text1, text2):
    text1 = sorted(text1.upper())
    text2 = sorted(text2.upper())
    return text1 == text2

## FIZZBUZZ ##
def fizzbuzz(n):
    if (n <= 0) or (not isinstance(n, int)):
        raise ValueError("Not valid btw!")
    my_list = []
    for i in range(1,n+1):
        if i % (3*5) == 0:
            my_list.append("FizzBuzz") 
        elif i % 3 == 0:
            my_list.append("Fizz")
        elif i % 5 == 0:
            my_list.append("Buzz")
        else:
            my_list.append(f"{i}")
    return my_list

## TEMP CONVERTER ##

def celsius_to_fahrenheit(temp):
    return (temp * 9/5) + 32

def fahrenheit_to_celsius(temp):
    return (temp - 32) * 5/9

## PASSWORD VALIDATOR ##

def password_check(password):
    if len(password) < 8:
        return False

    has_upper = False
    has_lower = False
    has_digit = False
    has_special = False

    for char in password:
        if char.isupper():
            has_upper = True
        elif char.islower():
            has_lower = True
        elif char.isdigit():
            has_digit = True
        else:
            has_special = True

    return has_upper and has_lower and has_digit and has_special


## BANK ACCOUNT ##

class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("You idiot")
        self.balance += amount
        return True

    def withdraw(self, amount):
        if amount <= 0 or amount > self.balance:
            raise ValueError("Your either poor or stupid")
        self.balance -= amount
        return True

    def get_balance(self):
        return self.balance


## COWS AND BULLS ##

class CowsAndBulls:
    number = ""
    def __init__(self, number = ""):
        if(number == ""):
            for i in range(4):
                self.number += str(random.randint(1,9))
        else:
            self.number = str(number)
        self.state = "ongoing"
        self.guess_count = 0

    def current_state(self):
        return self.state

    def guess(self, guess):
        if self.state == "finished":
            raise ValueError("The game is already finished")

        if(len(guess) != 4):
            if(guess == "-1"):
                print(f"Here is the secret: {self.number}")
                self.state = "finished"
                return self.state
            raise ValueError("Guess must be a 4-digit number")

        self.guess_count += 1

        cows = 0
        bulls = 0
        finds = ["-","-","-","-"]
        secret = self.number


        # find all green matches
        remaining_secret = list(secret)
        for i in range(4):
            if guess[i] == secret[i]:
                finds[i] = "C"
                cows += 1
                remaining_secret[i] = None

        # find yellow matches among unused digits
        for i in range(4):
            if finds[i] == "C":
                continue
            if guess[i] in remaining_secret:
                finds[i] = "B"
                bulls += 1
                remaining_secret[remaining_secret.index(guess[i])] = None

        
        if cows == 4:
            self.state = "finished"
            print(f"You won, the secret number was {self.number}")

        print(f"{cows} cows, {bulls} bulls")
        return f"{cows} - {bulls}"


#a = CowsAndBulls()
#while(a.current_state() != "finished"):
#    a.guess(input("Give a guess (0000-9999) (-1 to see answer and Quit): "))
    