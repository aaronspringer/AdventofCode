import re

def part1():
    total_points = 0

    with open("input.txt", 'r') as file:
        for line in file:
            parts = line.strip().split('|')
            winners = set(int(num) for num in re.findall(r'\d+', parts[0]))
            others = set(int(num) for num in re.findall(r'\d+', parts[1]))
            matches = len(winners.intersection(others))
            if matches > 0:
                card_points = 2 ** (matches - 1)
            else:
                card_points = 0

            total_points += card_points

    return total_points


def part2():
    with open("input.txt", 'r') as file:
        lines = file.readlines()

    cardmatches = []
    for line in lines:
        parts = line.strip().split('|')
        winners = set(int(num) for num in re.findall(r'\d+', parts[0]))
        others = set(int(num) for num in re.findall(r'\d+', parts[1]))
        matches = len(winners.intersection(others))
        cardmatches.append(matches)

    cardaddition = [1 for _ in cardmatches]

    for i in range(len(cardmatches)):
        for j in range(1, cardmatches[i] + 1):
            if i + j < len(cardaddition):
                cardaddition[i + j] += cardaddition[i]

    total = sum(cardaddition)
    return total

print(part1())
print(part2())

