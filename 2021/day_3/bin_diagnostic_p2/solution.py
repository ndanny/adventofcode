# https://adventofcode.com/2021/day/3

f = open('2021/day_3/input.txt', 'r')

bins = []
for line in f.readlines():
    bins.append(line.strip())

f.close()


# Calculate the most common bit in each column for the resulting
# number.
def calculate(t, bins):
    res = []
    size = bins[0]
    for i in range(len(size)):
        ones = 0
        zeros = 0
        for j in range(len(bins)):
            if bins[j][i] == '1':
                ones += 1
            elif bins[j][i] == '0':
                zeros += 1
        

        if ones > zeros:
            if t == 'gamma':
                res.append('1')
            elif t == 'epsilon':
                res.append('0')
        else:
            if t == 'gamma':
                res.append('0')
            elif t == 'epsilon':
                res.append('1')

    return ''.join(res)

gam = calculate('gamma', bins)
ep = calculate('epsilon', bins)

n1 = int(gam, 2)
n2 = int(ep, 2)

print(n1)
print(n2)

# Result
print(n1 * n2)
