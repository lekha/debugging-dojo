#!/usr/bin/env python3
"""
Prompt:
Loop through all numbers from 1 to 100. If the number is divisible by 3, print
out "Fizz" instead. If the number is divisible by 5, print out "Buzz" instead.
"""
from typing import Iterable
from typing import Union


def fizz_buzz(n: int) -> Iterable[Union[int, str]]:
    for i in range(n):
        if i%3 == 0: yield 'Fizz'
        elif i%5 == 0: yield 'Buzz'
        else: yield i


if __name__ == '__main__':
    print(list(fizz_buzz(17)))

