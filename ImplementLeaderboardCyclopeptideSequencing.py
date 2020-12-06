masses = {
    'G': 57,
    'A': 71,
    'S': 87,
    'P': 97,
    'V': 99,
    'T': 101,
    'C': 103,
    'I': 113,
    'N': 114,
    'D': 115,
    'K': 128,
    'E': 129,
    'M': 131,
    'H': 137,
    'F': 147,
    'R': 156,
    'Y': 163,
    'W': 186}

def LinearSpectrum(peptide):
    peptides = [peptide]
    n = len(peptide)
    for l in range(1, n):
        for i in range(n - l):
            peptides.append(peptide[i: i + l])
    return sorted([Mass(peptide) for peptide in peptides])


def Cyclospectrum(peptide):
    peptides = [peptide]
    n = len(peptide)
    peptide += peptide
    for l in range(1, n):
        for i in range(n):
            peptides.append(peptide[i: (i + l)])
    return sorted([Mass(peptide) for peptide in peptides])


def Mass(peptide):
    return sum(peptide)

def Expand(leaderboard):
    expanded = []
    for pep in leaderboard:
        for w in masses.values():
            expanded.append(pep + (w,))
    return expanded


def CyclicScore(peptide, spectrum):
    score = 0
    for weight in Cyclospectrum(peptide):
        if weight in spectrum:
            score += 1
    return score


def Score(peptide, spectrum):
    score = 0
    for elem in LinearSpectrum(peptide):
        if elem in spectrum:
            score += 1
    return score


def Cut(board, spectrum, n):
    board.sort(reverse=True, key=lambda x: Score(x, spectrum))
    if len(board) <= n:
        return board
    cutted = board[:n]
    for i in range(n, len(board)):
        prev = Score(board[i - 1], spectrum)
        curr = Score(board[i], spectrum)
        if prev != curr:
            break
        cutted.append(board[i])
    return cutted


def SequenceLeaderboardCyclopeptide(Spectrum, N):
    new_leaderboard = [tuple()]
    leader_peptide = tuple()
    parentMass = max(Spectrum)
    while True:
        leaderboard = Expand(new_leaderboard)
        new_leaderboard = []
        for peptide in leaderboard:
            mass = Mass(peptide)
            if mass == parentMass:
                if CyclicScore(peptide, Spectrum) > CyclicScore(leader_peptide, Spectrum):
                    leader_peptide = peptide
            elif mass < parentMass:
                new_leaderboard.append(peptide)

        new_leaderboard = Cut(new_leaderboard, Spectrum, N)
        if not new_leaderboard:
            break
    return leader_peptide


n = int(input())
spectrum = [int(elem) for elem in input().split()]

cyclopeptide = SequenceLeaderboardCyclopeptide(spectrum, n)
print("-".join(str(weight) for weight in cyclopeptide))