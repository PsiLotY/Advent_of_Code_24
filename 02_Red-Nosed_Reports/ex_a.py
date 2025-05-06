"""Advent of Code 2024 - Day 2: Red-Nosed Reports
https://adventofcode.com/2024/day/2
"""

reports = []
correct_reports = 0

with open("02_Red-Nosed_Reports/input.txt", "r", encoding="utf-8") as f:
    reports = f.read().splitlines()

# either increae or decrease
# differ by at least 1 up to 3 
for report in reports:
    report = report.split(" ")
    increasing = True
    decreasing = True
    step_norm = True
    for i in range(len(report)-1):
        current_number = int(report[i])
        next_number = int(report[i+1])
        if current_number < next_number:
             decreasing = False
        if current_number > next_number:
            increasing = False
        difference = abs(current_number - next_number)
        if difference > 3 or difference <1:
            step_norm = False
    if (increasing and step_norm) or (decreasing and step_norm):
        correct_reports += 1
print("Correct reports:", correct_reports)
