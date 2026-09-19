# You have the four functions:

# printFizz that prints the word "fizz" to the console,
# printBuzz that prints the word "buzz" to the console,
# printFizzBuzz that prints the word "fizzbuzz" to the console, and
# printNumber that prints a given integer to the console.
# You are given an instance of the class FizzBuzz that has four functions: fizz, buzz, fizzbuzz and number. The same instance of FizzBuzz will be passed to four different threads:

# Thread A: calls fizz() that should output the word "fizz".
# Thread B: calls buzz() that should output the word "buzz".
# Thread C: calls fizzbuzz() that should output the word "fizzbuzz".
# Thread D: calls number() that should only output the integers.
# Modify the given class to output the series [1, 2, "fizz", 4, "buzz", ...] where the ith token (1-indexed) of the series is:

# "fizzbuzz" if i is divisible by 3 and 5,
# "fizz" if i is divisible by 3 and not 5,
# "buzz" if i is divisible by 5 and not 3, or
# i if i is not divisible by 3 or 5.
# Implement the FizzBuzz class:

# FizzBuzz(int n) Initializes the object with the number n that represents the length of the sequence that should be printed.
# void fizz(printFizz) Calls printFizz to output "fizz".
# void buzz(printBuzz) Calls printBuzz to output "buzz".
# void fizzbuzz(printFizzBuzz) Calls printFizzBuzz to output "fizzbuzz".
# void number(printNumber) Calls printnumber to output the numbers.
 

# Example 1:

# Input: n = 15
# Output: [1,2,"fizz",4,"buzz","fizz",7,8,"fizz","buzz",11,"fizz",13,14,"fizzbuzz"]
# Example 2:

# Input: n = 5
# Output: [1,2,"fizz",4,"buzz"]

import threading
from typing import Callable


class FizzBuzz:
    def __init__(self, n: int):
        self.n = n
        self.current = 1
        self.condition = threading.Condition()

    def _should_print(self, value: int, token: str) -> bool:
        if token == "fizz":
            return value % 3 == 0 and value % 5 != 0
        if token == "buzz":
            return value % 5 == 0 and value % 3 != 0
        if token == "fizzbuzz":
            return value % 15 == 0
        return value % 3 != 0 and value % 5 != 0

    # printFizz() outputs "fizz"
    def fizz(self, printFizz: 'Callable[[], None]') -> None:
        with self.condition:
            while self.current <= self.n:
                while self.current <= self.n and not self._should_print(self.current, "fizz"):
                    self.condition.wait()
                if self.current > self.n:
                    return
                printFizz()
                self.current += 1
                self.condition.notify_all()

    # printBuzz() outputs "buzz"
    def buzz(self, printBuzz: 'Callable[[], None]') -> None:
        with self.condition:
            while self.current <= self.n:
                while self.current <= self.n and not self._should_print(self.current, "buzz"):
                    self.condition.wait()
                if self.current > self.n:
                    return
                printBuzz()
                self.current += 1
                self.condition.notify_all()

    # printFizzBuzz() outputs "fizzbuzz"
    def fizzbuzz(self, printFizzBuzz: 'Callable[[], None]') -> None:
        with self.condition:
            while self.current <= self.n:
                while self.current <= self.n and not self._should_print(self.current, "fizzbuzz"):
                    self.condition.wait()
                if self.current > self.n:
                    return
                printFizzBuzz()
                self.current += 1
                self.condition.notify_all()

    # printNumber(x) outputs "x", where x is an integer.
    def number(self, printNumber: 'Callable[[int], None]') -> None:
        with self.condition:
            while self.current <= self.n:
                while self.current <= self.n and not self._should_print(self.current, "number"):
                    self.condition.wait()
                if self.current > self.n:
                    return
                printNumber(self.current)
                self.current += 1
                self.condition.notify_all()


if __name__ == "__main__":
    def run_example(n: int):
        result = []
        obj = FizzBuzz(n)

        def print_fizz():
            result.append("fizz")

        def print_buzz():
            result.append("buzz")

        def print_fizzbuzz():
            result.append("fizzbuzz")

        def print_number(x: int):
            result.append(x)

        threads = [
            threading.Thread(target=obj.fizz, args=(print_fizz,)),
            threading.Thread(target=obj.buzz, args=(print_buzz,)),
            threading.Thread(target=obj.fizzbuzz, args=(print_fizzbuzz,)),
            threading.Thread(target=obj.number, args=(print_number,)),
        ]

        for thread in threads:
            thread.start()
        for thread in threads:
            thread.join()

        print(result)

    run_example(15)