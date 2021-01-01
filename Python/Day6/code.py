"""
--- Day 6: Custom Customs ---
As your flight approaches the regional airport where you'll switch to a
much larger plane, customs declaration forms are distributed to the
passengers.

The form asks a series of 26 yes-or-no questions marked a through z. All
you need to do is identify the questions for which anyone in your group
answers "yes". Since your group is just you, this doesn't take very long.

However, the person sitting next to you seems to be experiencing a language
barrier and asks if you can help. For each of the people in their group,
you write down the questions for which they answer "yes", one per line.
For example:

abcx
abcy
abcz

In this group, there are 6 questions to which anyone answered "yes": a, b,
c, x, y, and z. (Duplicate answers to the same question don't count extra;
each question counts at most once.)

Another group asks for your help, then another, and eventually you've
collected answers from every group on the plane (your puzzle input). Each
group's answers are separated by a blank line, and within each group, each
person's answers are on a single line. For example:

abc

a
b
c

ab
ac

a
a
a
a

b

This list represents answers from five groups:

- The first group contains one person who answered "yes" to 3 questions:
  a, b, and c.
- The second group contains three people; combined, they answered "yes"
  to 3 questions: a, b, and c.
- The third group contains two people; combined, they answered "yes" to
  3 questions: a, b, and c.
- The fourth group contains four people; combined, they answered "yes"
  to only 1 question, a.
- The last group contains one person who answered "yes" to only 1
  question, b.

In this example, the sum of these counts is 3 + 3 + 3 + 1 + 1 = 11.

For each group, count the number of questions to which anyone answered
"yes". What is the sum of those counts?
"""

from functools import reduce


def count_answer(group):
    flatten_group = reduce(lambda x, y: x + y, group)
    return len(set(flatten_group))


def part1(groups):
    result = 0
    for group in groups:
        result += count_answer(group)
    return result


def part2(groups):
    pass


with open("./input.txt", "r") as input_file, open("./output.txt", "w") as output_file:
    groups = [line.split() for line in input_file.read().split("\n\n")]

    output_file.write(f"part1 solution : {part1(groups)}\n")
    output_file.write(f"part2 solution : {part2(groups)}\n")
