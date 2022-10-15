# https://adventofcode.com/2021/day/3

f = open('2021/day_3/input.txt', 'r')

bins = []
for line in f.readlines():
    bins.append(line.strip())

f.close()

# Calculate the oxygen generator rating
def oxygen_generator_rating(bins):
    candidates = bins
    length = len(bins[0])

    for i in range(length):
        # In the ith position, calculate the most common bit
        ones = 0
        zeros = 0
        for n in candidates:
            if n[i] == '1':
                ones += 1
            else:
                zeros += 1
        
        winner = '1' if ones >= zeros else '0'

        # Then, iterate through the candidates and only choose those who
        # has the winner in the ith position
        safe = []
        for n in candidates:
            if n[i] == winner:
                safe.append(n)
        
        candidates = safe

    return candidates[0]

# Calculate the co2 scrubber rating
def co2_scrubber_rating(bins):
    candidates = bins
    length = len(bins[0])

    for i in range(length):
        if len(candidates) == 1:
            return candidates[0]
        
        # In the ith position, calculate the least common bit
        ones = 0
        zeros = 0
        for n in candidates:
            if n[i] == '1':
                ones += 1
            else:
                zeros += 1
        
        winner = '0' if zeros <= ones else '1'

        # Then, iterate through the candidates and only choose those who
        # has the winner in the ith position
        safe = []
        for n in candidates:
            if n[i] == winner:
                safe.append(n)
        
        candidates = safe
    print(candidates)
    return


ogr = int(oxygen_generator_rating(bins), 2)
csr = int(co2_scrubber_rating(bins), 2)
print(ogr)
print(csr)

life_support = ogr * csr
print('answer:', life_support) # the answer
