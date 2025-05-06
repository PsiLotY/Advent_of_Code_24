"""Advent of Code 2024 - Day 1: Historian Hysteria
https://adventofcode.com/2024/day/1
"""

left_list = []
right_list = []
similarity = 0

with open("01_Historian_Hysteria/input.txt", "r", encoding="utf-8") as f:
    for line in f:
        line = line.strip()
        splitted = line.split("   ")
        left_list.append(splitted[0])
        right_list.append(splitted[1])

# go through left list and search the count of same number in right list

for i in range(len(left_list)):
    left = int(left_list[i])
    number_count = right_list.count(left)
    similarity += left * number_count

print("Similarity:", similarity)
