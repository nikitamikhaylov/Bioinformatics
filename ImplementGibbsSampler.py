import operator
import math
import random
import itertools
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

def GibbsMostProbable(profile, text, k):
    probabilities = []
    for kmer in window(text, k):
        probabilities.append(ProfileProbability(profile, kmer))
    probability_sum = sum(probabilities)
    probabilities = [p / probability_sum for p in probabilities]
    accumulated_probs = list(itertools.accumulate(probabilities))
    toss = random.random()
    for i in range(len(accumulated_probs)):
        if toss < accumulated_probs[i]:
            return text[i:i + k]

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

def GibbsSampler(text, k, t, N):
    motifs = GetRandomMotifs(text, k)
    best_motifs = motifs
    best_score = math.inf
    for _ in range(N):
        removed_sequence = random.randrange(t)
        current_motifs = motifs[:removed_sequence] + motifs[removed_sequence + 1:]
        profile = ComputeProfile(current_motifs)
        computed_motif = GibbsMostProbable(profile, text[removed_sequence], k)
        motifs = motifs[:removed_sequence] + [computed_motif] + motifs[removed_sequence + 1:]
        if Score(motifs) < best_score:
            best_score = Score(motifs)
            best_motifs = motifs
    return best_motifs

def RunMultipleTimesGibbsSampler(dna_list, k, t, N):
    best_score = math.inf
    best_motifs = None
    for _ in tqdm(range(20)):
        motifs = GibbsSampler(dna_list, k, t, N)
        if Score(motifs) < best_score:
            best_motifs = motifs
            best_score = Score(motifs)
    return best_motifs

if __name__ == "__main__":
    k, t, N = map(int, input().split())
    text = [input() for _ in range(t)]
    for motif in RunMultipleTimesGibbsSampler(text, k, t, N):
        print(motif)