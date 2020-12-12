"""
--- Day 1: Report Repair ---
After saving Christmas five years in a row, you've decided to take a
vacationat a nice resort on a tropical island.Surely, Christmas will go
on without you.

The tropical island has its own currency and is entirely cash-only. The
gold coins used there have a little picture of a starfish; the locals just
call them stars. None of the currency exchanges seem to have heard of them,
but somehow, you'll need to find fifty of these coins by the time you
arrive so you can pay the deposit on your room.

To save your vacation, you need to get all fifty stars by December 25th.

Collect stars by solving puzzles. Two puzzles will be made available on
each day in the Advent calendar; the second puzzle is unlocked when you
complete the first. Each puzzle grants one star. Good luck!

Before you leave, the Elves in accounting just need you to fix your expense
report (your puzzle input); apparently, something isn't quite adding up.

Specifically, they need you to find the two entries that sum to 2020
and then multiply those two numbers together.

For example, suppose your expense report contained the following:

1721
979
366
299
675
1456

In this list, the two entries that sum to 2020 are 1721 and 299.
Multiplying them together produces 1721 * 299 = 514579, so the correct answer is 514579.

--- Part Two ---
The Elves in accounting are thankful for your help; one of them even offers
you a starfish coin they had left over from a past vacation. They offer you
a second one if you can find three numbers in your expense report that meet
the same criteria.

Using the above example again, the three entries that sum to 2020 are 979,
366, and 675. Multiplying them together produces the answer, 241861950.

In your expense report, what is the product of the three entries that sum
to 2020?
"""

from functools import reduce
from itertools import combinations


def part1(numbers):
    return reduce(
        lambda x, y: x * y,
        list(*filter(lambda comb: sum(comb) == 2020, combinations(numbers, 2))),
    )


def part2(numbers):
    return reduce(
        lambda x, y: x * y,
        list(*filter(lambda comb: sum(comb) == 2020, combinations(numbers, 3))),
    )


numbers = None

with open("./input.txt", "r") as f:
    numbers = list(map(lambda line: int(line.rstrip("\n")), f.readlines()))

with open("./output.txt", "w") as f:
    f.write(f"part1 solution : {part1(numbers)}\n")
    f.write(f"part2 solution : {part2(numbers)}\n")

PART_ONE_TEST_CASE = {
    "numbers": [1721, 979, 366, 299, 675, 1456],
    "result": 514579,
}

PART_TWO_TEST_CASE = {
    "numbers": [1721, 979, 366, 299, 675, 1456],
    "result": 241861950,
}

print(f'part1 test result : {part1(PART_ONE_TEST_CASE["numbers"]) == PART_ONE_TEST_CASE["result"]}')
print(f'part2 test result : {part2(PART_TWO_TEST_CASE["numbers"]) == PART_TWO_TEST_CASE["result"]}')

