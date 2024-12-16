# Prime Game

## Description

This module defines a function `isWinner` to determine the winner of a prime number game played by Maria and Ben.

## Game Rules

1. Given a set of consecutive integers from 1 to `n`, players alternately pick a prime number.
2. When a prime is chosen, it and all its multiples are removed from the set.
3. The player unable to make a move loses.

Maria always goes first, and both players play optimally.

## Prototype

```python
def isWinner(x, nums)

