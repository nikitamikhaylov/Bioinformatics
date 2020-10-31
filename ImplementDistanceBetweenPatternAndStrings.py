import math

def window(s, k):
    for i in range(len(s) - k + 1):
        yield s[i: i+k]

def Hamming(a, b):
    return sum([1 for i, j in zip(a, b) if i != j])

def DistanceBetweenPatternAndStrings(text, pattern):
    k = len(pattern)
    distance = 0
    for string in text:
        HammingDistance = math.inf
        for kmer in window(string, k):
            if HammingDistance > Hamming(pattern, kmer):
                HammingDistance = Hamming(pattern, kmer)
        distance += HammingDistance
    return distance

if __name__ == "__main__":
    pattern = input()
    text = input().split()
    print(DistanceBetweenPatternAndStrings(text, pattern))