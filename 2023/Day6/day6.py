from math import prod

def calculate(times, distances):
    winners = []

    for i in range(len(times)):
        time = times[i]
        distance = distances[i]
        validholds = 0

        for holdtime in range(time):
            speed = holdtime
            traveltime = time - holdtime
            totaldistance = speed * traveltime
            if totaldistance > distance:
                validholds += 1

        winners.append(validholds)

    return winners, prod(winners)


time = [41968894]
distance = [214178911271055]

win, total = calculate(time, distance)
print(win,total)

