def hamming(a, b):
    return sum([1 for i, j in zip(a, b) if i != j])

def ApproximatePatternMatching(genome, pattern, d):
    count = 0
    output = open("output.txt", 'w')
    for i in range(len(genome) - len(pattern)):
        if hamming(genome[i: i + len(pattern)], pattern) <= d:
            count += 1
            print(i, end = ' ', file=output)
    return count

if __name__ == "__main__":
    pattern = input()
    genome = input()
    d = int(input())
    ApproximatePatternMatching(genome, pattern, d)
