# https://adventofcode.com/2021/day/2

f = open('2021/day_2/input.txt', 'r')

commands = []
for line in f.readlines():
    commands.append(line.strip())

f.close()

depth = 0
horizontal_position = 0

for command in commands:
    action, amount = command.split(' ')
    amount = int(amount)

    if action == 'forward':
        horizontal_position += amount
    elif action == 'up':
        depth -= amount
    elif action == 'down':
        depth += amount

print(depth * horizontal_position)
