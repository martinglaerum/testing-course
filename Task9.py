## EVEN OR ODD ##

def even_or_odd(number):
    if(number % 2 == 0):
        return "Even"
    else:
        return "Odd"

print(even_or_odd(17),even_or_odd(248),even_or_odd(9781))


## BASIC OPERATIONS ##
def basic_operations(operation,number1,number2):
    if(operation == "Plus"):
        return number1 + number2
    elif(operation == "Minus"):
        return number1 - number2
    elif(operation == "Division"):
            return number1 / number2
    elif(operation == "Multiplication"):
        return number1 * number2
    else:
        return 0

print(basic_operations("plus",3,9),basic_operations("Division",5468,42),basic_operations("Multiplication",71,29))


## TOTAL POINTS ##

def total_points(match):
    parts = match.split(":")
    home = int(parts[0])
    away = int(parts[1])
    score = 0
    if(home > away):
        score = 3
    elif(home == away):
        score = 1
    print(f"From this match your team got {score} points")

total_points("4:2")
total_points("17:21")
total_points("321:321")
total_points("7:10")

## THE LARGEST NUMBER ##

def largest_number(a,b,c):
    total1 = a + b + c
    total2 = a * b * c
    if(total1 > total2):
        return total1
    return total2

print(largest_number(1,2,3), largest_number(7,-2,3),largest_number(8,2,4))


## THE POWER OF N-TH ##

def index(my_numbers, nth):
    if nth < 0 or nth >= len(my_numbers):
        return -1

    return my_numbers[nth-1] ** nth

print(index([1, 2, 3, 4], 3))


## QUARTER OF THE YEAR ##

def quarter_of_the_year(month):
    if (month < 0 or month > 12) :
        return "idiot"
    if month < 4:
        return "First quarter"
    if month < 7:
        return "Second quarter"
    if month < 10:
        return "Third quarter"
    else:
        return "Fourth quarter"

print(quarter_of_the_year(1),quarter_of_the_year(7),quarter_of_the_year(12))

## CENTURY OF THE YEAR ##

def century(year):
    cent = year // 100
    edge_case =  year % 100
    if(edge_case == 0):
        return cent
    else:
        return cent+1

print(century(1312),century(800),century(2121),century(75))

## FORM THE MINIMUM ##

def form_the_minimum(*args):
    numbers = set()
    for num in args:
        numbers.add(num)
    numbers = sorted(numbers)
    total = ""
    for i in range(len(numbers)):
        total = total + str(numbers[i])
    return int(total)

print(form_the_minimum(1,2,4,6,2,1),form_the_minimum(9,2,4,6,2),form_the_minimum(1,3,1,3,1),form_the_minimum(5,7,3,9,2,9,8))


#### THE PIZZA MADNESS ####

## STRING REPEAT ##

def string_repeat(my_text,my_number):
    for i in range(my_number):
        print(my_text)

string_repeat("Hey",3)
string_repeat("Yo, you serious",2)
string_repeat("What a save!",5)

## NO WHITESPACES ##

def no_space(my_text):
    print(my_text.replace(" ", ""))

no_space("Last christmas, I gave you my heart")
no_space("See you again, aaaaaah")

## NUMBER TO STRING ##

def number_to_string(my_number):
    return str(my_number)

print(number_to_string(1),number_to_string(23),number_to_string(2198612))

## BOLEAAN TO STRING ##
def bolaan_to_string(my_bool):
    return str(my_bool)

print(bolaan_to_string(True),bolaan_to_string(False))

## ABBREVIATE A PIZZA NAME ##
def abbrev_name(my_string):
    parts = my_string.split(" ")
    return parts[0][0] + "." + parts[1][0]

print(abbrev_name("Martin Glaerum"), abbrev_name("Bruno Fernandes"))


## PIZZA LENGTH ##
def name_length(my_string):
    parts = my_string.split(" ")
    return [parts[0], len(parts[0]), parts[1], len(parts[1])]

print(name_length("Mikkel Rev"))

## REMOVE THE FIRST AND LAST ELEMENT ##

def remove_orders(my_string):
    numbers = my_string.split(",")
    if len(numbers) < 3:
        return ""
    del numbers[0]
    del numbers[-1]
    my_string2 = ""
    for i in range(len(numbers)):
        my_string2 = my_string2 + numbers[i]
        if (i < ((len(numbers))-1)):
            my_string2 = my_string2 + ","
    return my_string2

print(remove_orders("3,4,3,5,6,2,4"), remove_orders("2,3,4,2"), remove_orders("1,2,3"))

## THE MENU ##

def food_menu(foods):
    foods2 = []
    i = 1
    for food in foods:
        foods2.append(f"{i}.{food}")
        i += 1
    return foods2

print(food_menu(["Pizza","Onion","Lasagne","Egg", "Tikki Masala"]))