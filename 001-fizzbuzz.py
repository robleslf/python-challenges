### Exercise: FizzBuzz Challenge###

'''Develop a Python program that prints a series of numbers from 1 to 
100. However, for multiples of 3, the program should print "Fizz" 
instead of the number, and for multiples of 5, it will print "Buzz". 
For numbers that are multiples of both 3 and 5, the program will 
print "FizzBuzz".

Your task is to write a program that accomplishes this task in an 
elegant and efficient manner. Be sure to use control structures and 
programming logic to achieve it. Once your program is ready, you 
will have a creative solution to the classic programming challenge 
known as FizzBuzz.'''

def fizzbuzz():
    for number in range(1,101):
        if number % 3 == 0 and number % 5 == 0:
            print("FizzBuzz")
        elif number % 3 == 0:
            print("Fizz")
        elif number % 5 == 0:
            print("Buzz")
        else:
            print(number)

fizzbuzz()