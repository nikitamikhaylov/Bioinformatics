import operator
import numpy as np
import math
import random
from tqdm import tqdm

symbolToNumber = {'A': 0, 'T': 1, 'C': 2, 'G': 3}
numberToSymbol = {0: 'A', 1: 'T', 2: 'C', 3: 'G'}

def window(s, k):
    for i in range(len(s) - k + 1):
        yield s[i: i+k]

def Hamming(a, b):
    return sum([1 for i, j in zip(a, b) if i != j])

def ComputeProfile(motifs):
    len_motif = len(motifs[0])
    profile = {s : [0] * len_motif for s in 'ACTG'}
    profile['len'] = len(motifs)
    for i in range(len_motif):
        current = {'A': 0, 'T': 0, 'C': 0, 'G': 0}
        for motif in motifs:
            current[motif[i]] += 1
        for s in 'ACTG':
            profile[s][i] = current[s] + 1 / (len(motifs))
    return profile

def ConsensusString(motifs):
    len_motif = len(motifs[0])
    answer = ''
    for i in range(len_motif):
        current = {'A': 0, 'T': 0, 'C': 0, 'G': 0}
        for motif in motifs:
            current[motif[i]] += 1
        answer += max(current.items(), key=operator.itemgetter(1))[0]
    return answer

def ProfileProbability(profile, str):
    probability = 1
    for i, s in enumerate(str):
        probability *= profile[s][i]
    return probability

def ProfileMostProbable(profile, text, k):
    probabilities = []
    for kmer in window(text, k):
        probabilities.append(ProfileProbability(profile, kmer))
    answer = np.argmax(probabilities)
    return text[answer: answer + k]

def Score(motifs):
    score = 0
    consensus = ConsensusString(motifs)
    for motif in motifs:
        score += Hamming(motif, consensus)
    return score

def GetRandomMotifs(text, k):
    motifs = []
    for string in text:
        ind = random.randint(0, len(string) - k)
        motifs.append(string[ind : ind + k])
    return motifs

def GetMotifsFromProfile(text, profile, k):
    motifs = []
    for string in text:
        motifs.append(ProfileMostProbable(profile, string, k))
    return motifs

def RandomizedMotifSearch(text, k, t):
    motifs = GetRandomMotifs(text, k)
    best_motifs = motifs
    best_score = math.inf
    while True:
        profile = ComputeProfile(motifs)
        motifs = GetMotifsFromProfile(text, profile, k)
        if Score(motifs) < best_score:
            best_score = Score(motifs)
            best_motifs = motifs
        else:
            break
    return best_motifs

def RunMultipleTimes(dna_list, k, t):
    best_score = math.inf
    best_motifs = None
    for i in tqdm(range(1000)):
        motifs = RandomizedMotifSearch(dna_list, k, t)
        if Score(motifs) < best_score:
            best_motifs = motifs
            best_score = Score(motifs)
    return best_motifs

if __name__ == "__main__":
    k, t = map(int, input().split())
    text = []
    for _ in range(t):
        text.append(input())
    for motif in RunMultipleTimes(text, k, t):
        print(motif)