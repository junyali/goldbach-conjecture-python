
## // Imports \\ ##
import tkinter as tk
from tkinter import ttk
import timeit

# Sieve of eratosthenes is used to find every prime number up to and including n
def sieve_of_eratosthenes(n):
    potential_prime = [True for _ in range(n+1)]
    primes = []

    # Check all numbers if prime
    i = 2
    while i * i <= n:
        if potential_prime[i]:
            for j in range(i * i, n + 1, i):
                potential_prime[j] = False
        i += 1

    # Collects all prime numbers into a separate elist
    for i in range(2, n + 1):
        if potential_prime[i]:
            primes.append(i)

    return primes

def trim_prime_two(primes):
    primes.remove(2)
    return primes

def goldbach_strong_conjecture(n):
    # sum_x and sum_y are two prime numbers of which the sum is n
    sum_x, sum_y = 0, 0
    result = 0
    n = int(n)

    # n must be even
    if n % 2 == 0:
        primes = trim_prime_two(sieve_of_eratosthenes(n))

        while result != n:
            for prime_i in range(len(primes)):
                if result == n: break
                sum_x = primes[prime_i]
                for prime_j in range(len(primes)):
                    sum_y = primes[prime_j]
                    result = sum_x + sum_y
                    # Checks each combination of primes to see if the sum is equal to n
                    if result == n: break

    else:
        print("{number} is not an even natural number; Goldbach's Strong Conjecture cannot be verified with {number}".format(number=n))

    return sum_x, sum_y

if __name__ == '__main__':
    num = int(input("Please enter an even natural number greater than 2 >> "))
    timer_start = timeit.default_timer()
    x, y = goldbach_strong_conjecture(num)
    timer_end = timeit.default_timer()
    time_difference = timer_end - timer_start
    print("The prime sum of {x} and {y} make up the number {n}.".format(x=x, y=y, n=num))
    print("Calculation took {time} seconds.".format(time=round(time_difference, 2)))
