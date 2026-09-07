# Canonical Graduate SWE — DevSkiller Python Test Prep Guide

## 1. GitHub Repos to Re-Learn Python Syntax

**Primary — full syntax refresher (start here):**
[`Asabeneh/30-Days-Of-Python`](https://github.com/Asabeneh/30-Days-Of-Python)
A day-by-day guide covering variables, data types, strings, lists, tuples, sets,
dictionaries, conditionals, loops, functions, modules, list comprehensions, higher-order
functions, and OOP — with exercises at the end of every section. Given your timeline,
don't do all 30 days; jump to whichever topics feel rusty (see the topic list in
their README) and do the exercises for those.

**Secondary — algorithm reference for the coding-exercise part:**
[`TheAlgorithms/Python`](https://github.com/TheAlgorithms/Python)
Clean, tested implementations of sorting, searching, recursion, and basic data
structures. Don't memorize these — use them *after* you attempt a problem yourself,
to compare your approach against a clean reference implementation.

---

## 2. What Canonical's DevSkiller Python Test Actually Looks Like

Based on public reports from candidates (Glassdoor, Blind, personal blogs), the test
is roughly **2 hours** and has two distinct parts:

**Part A — Knowledge / "predict the output" questions**
Quick multiple-choice or short-answer questions like:
- "Which of these words is *not* a Python logging level: URGENT, CRITICAL, INFO, FATAL, TRACE?"
- "What does this code snippet print?" (a 5–10 line snippet you mentally trace or paste into a local interpreter)

These are fast if you know core Python semantics cold — see the gotchas list below.

**Part B — Coding exercises (2–3 tasks)**
DevSkiller's format is usually **"RealLifeTesting"**: you're given an existing small
project/codebase with some functions unimplemented and some unit tests already failing.
Your job is to make the given tests pass (and your code is often also scored on
hidden verification tests you can't see). This is closer to "complete this codebase to
spec" than blank-page LeetCode — read the provided tests as your spec before writing code.
Difficulty is generally **Easy–Medium** (arrays, strings, dicts, sorting, basic recursion,
simple class design) — not hard algorithmic puzzles.

You can work in DevSkiller's browser editor, or download/clone the project and work
locally, then push back.

---

## 3. Tutorial: Python Gotchas Likely to Show Up

These are the classic "what does this print?" traps — go through each one, predict the
output yourself, then verify in a REPL.

```python
# 1. Mutable default arguments
def add_item(item, bucket=[]):
    bucket.append(item)
    return bucket
print(add_item(1))   # [1]
print(add_item(2))   # [1, 2]  <- surprising! default list is shared across calls

# 2. Late-binding closures in loops
funcs = [lambda: i for i in range(3)]
print([f() for f in funcs])   # [2, 2, 2], not [0, 1, 2]

# 3. `is` vs `==`
a = [1, 2, 3]
b = [1, 2, 3]
print(a == b)   # True (same value)
print(a is b)   # False (different objects)

# 4. Small integer caching
x = 256; y = 256
print(x is y)   # True (cached)
x = 257; y = 257
print(x is y)   # False (not cached, implementation detail)

# 5. Shallow vs deep copy
import copy
original = [[1, 2], [3, 4]]
shallow = copy.copy(original)
shallow[0][0] = 99
print(original[0][0])   # 99 — inner lists are shared

# 6. String formatting / f-strings
name = "Fatih"
print(f"{name!r}")        # 'Fatih' (repr)
print(f"{3.14159:.2f}")   # 3.14

# 7. *args / **kwargs unpacking
def f(a, b, *args, **kwargs):
    print(a, b, args, kwargs)
f(1, 2, 3, 4, x=5)   # 1 2 (3, 4) {'x': 5}

# 8. Generators vs lists
def gen():
    yield 1
    yield 2
g = gen()
print(list(g))   # [1, 2]
print(list(g))   # [] — generator is exhausted after first use

# 9. Exception flow: try / except / else / finally
try:
    print("try")
except ValueError:
    print("except")
else:
    print("else")   # runs only if no exception
finally:
    print("finally")  # always runs
# Output: try / else / finally

# 10. Sorting with a key
words = ["banana", "kiwi", "apple"]
print(sorted(words, key=len))   # ['kiwi', 'apple', 'banana']

# 11. Truthiness of empty containers
print(bool([]), bool({}), bool(""), bool(0), bool(None))  # all False

# 12. enumerate / zip
names = ["a", "b"]
scores = [10, 20]
for i, (n, s) in enumerate(zip(names, scores)):
    print(i, n, s)
```

---

## 4. Practice Problems (Typical Style for This Test)

Try these on paper or in a plain text editor first (no autocomplete) to simulate
DevSkiller's environment, then run them to check.

1. **FizzBuzz variant** — print 1–100, but replace multiples of 3 with "Fizz", multiples
   of 5 with "Buzz", multiples of both with "FizzBuzz".
2. **Palindrome check** — write `is_palindrome(s)` that ignores case and spaces.
3. **Anagram check** — write `is_anagram(a, b)` using `collections.Counter`.
4. **Word frequency counter** — given a paragraph, return the top 3 most common words.
5. **Flatten a nested list** — `[1, [2, [3, 4], 5]]` → `[1, 2, 3, 4, 5]`, using recursion.
6. **Find duplicates** — return all duplicate values in a list, preserving first-seen order.
7. **Simple class design** — implement a `Stack` class with `push`, `pop`, `peek`,
   `is_empty`, and raise a custom exception on popping an empty stack.
8. **Parse and query JSON** — given a JSON string of user records, return names of
   users older than 18, sorted alphabetically.

**Worked example (to show the expected code style — readable, documented, tested):**

```python
from collections import Counter

def top_n_words(text: str, n: int = 3) -> list[tuple[str, int]]:
    """Return the n most common words in `text`, lowercased, punctuation ignored."""
    words = [w.strip(".,!?").lower() for w in text.split()]
    return Counter(words).most_common(n)

# Quick self-test
assert top_n_words("The cat sat. The cat ran.") == [("the", 2), ("cat", 2), ("sat", 1)]
print(top_n_words("The cat sat. The cat ran."))
```

---

## 5. Tips & Tricks for the Test Itself

- **Read the provided unit tests first, every time.** In DevSkiller's RealLifeTesting
  format, the given tests *are* the spec. Don't guess at requirements — the tests tell
  you exactly what's expected, including edge cases.
- **Time-box the knowledge section.** It's meant to be fast. If a trivia question stalls
  you for more than ~30 seconds, mark your best guess and move on — don't burn coding
  time on it.
- **Practice in a bare editor, not your usual IDE.** DevSkiller's browser editor has
  limited or no autocomplete. Try solving 2–3 of the practice problems above in a plain
  text editor or Notepad first, so the lack of IntelliSense doesn't throw you off during
  the real test.
- **Write clean, documented code even under time pressure.** Canonical's own prep
  guidance and candidate reports both note that code quality/readability is scored, and
  your test code may resurface in later live interviews. A short docstring and clear
  variable names cost you seconds and pay off.
- **Test edge cases before submitting:** empty input, `None`, negative numbers, duplicate
  values, single-element lists. A lot of hidden verification tests specifically probe these.
- **Know your standard library toolkit** — you'll write faster, cleaner code if these are
  fluent rather than looked-up: `collections.Counter` / `defaultdict`, `itertools`,
  `re`, `json`, `datetime`, list/dict comprehensions, `sorted(..., key=...)`.
- **Run everything locally before you submit**, even if it means copying your solution
  out of the browser editor into a terminal — a silly syntax typo shouldn't cost you the
  whole exercise.
- **Answer every question**, even ones you're unsure about — don't leave blanks if
  there's no penalty for wrong answers (check the instructions, but this is standard for
  DevSkiller-style tests).
- **Protect the 2-hour block**: stable internet, no interruptions, and treat it like a
  real exam — candidates report the timer is strict once started.

Good luck with it — feel free to paste any practice snippet here afterward if you want a second pair of eyes before the real thing.
