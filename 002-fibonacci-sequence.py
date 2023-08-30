### Exercise: Fibonacci Sequence Generator ###

'''
es: Descripción:
La secuencia de Fibonacci es una serie matemática en la cual cada número es la suma 
de los dos números anteriores. Comienza generalmente con los números 0 y 1. En este 
ejercicio, vamos a escribir un programa en Python para generar y mostrar los primeros 
100 números de la secuencia de Fibonacci.

en:The Fibonacci sequence is a mathematical series in which each number is the sum 
of the two preceding ones. It usually starts with the numbers 0 and 1. In this 
exercise, we are going to write a Python program to generate and display the first 
100 numbers of the Fibonacci sequence.
'''

def fibonacci_sequence():
    
    prev = 0
    next = 1

    for ind, num in enumerate(range(0, 30)):
        print(f"{ind + 1}: {prev}")

        fib = prev + next
        prev = next
        next = fib

fibonacci_sequence()