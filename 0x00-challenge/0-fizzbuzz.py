#!/usr/bin/python3
""" FizzBuzz
    Changes of logic if (j % 3) == 0 and (j % 5) == 0:
"""
import sys


def fizzbuzz(m):
    """
    This fizzBuzz function prints numbers from 1 to n separated by a space
    
    - This multiples of three print "Fizz" instead of the number and for
      multiples of five print "Buzz"
    - These are numbers which are multiples of both
      three and five print "FizzBuzz"
    """
    if m < 1:
        return

    tmp_result = []
    for j in range(1, n + 1):
        if (j % 3) == 0 and (j % 5) == 0:
            tmp_result.append("FizzBuzz")
        elif (j % 3) == 0:
            tmp_result.append("Fizz")
        elif (j % 5) == 0:
            tmp_result.append("Buzz")
        else:
            tmp_result.append(str(j))
    print(" ".join(tmp_result))


if __name__ == '__main__':
    if len(sys.argv) <= 1:
        print("Missing number")
        print("Usage: ./0-fizzbuzz.py <number>")
        print("Example: ./0-fizzbuzz.py 89")
        sys.exit(1)

    number = int(sys.argv[1])
    fizzbuzz(number)
