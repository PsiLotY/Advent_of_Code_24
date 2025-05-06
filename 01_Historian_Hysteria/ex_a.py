"""Advent of Code 2024 - Day 1: Historian Hysteria
https://adventofcode.com/2024/day/1
"""

left_list = []
right_list = []
distance = 0

with open("01_Historian_Hysteria/input.txt", "r", encoding="utf-8") as f:
    for line in f:
        line = line.strip()
        splitted = line.split("   ")
        left_list.append(splitted[0])
        right_list.append(splitted[1])

left_list.sort()
right_list.sort()

for i in range(len(left_list)):
    left = left_list[i]
    right = right_list[i]
    distance += abs(int(left)-int(right))

print("Distance:", distance)