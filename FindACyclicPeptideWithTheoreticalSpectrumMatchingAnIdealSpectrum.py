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
    peptides = [peptide, ""]
    n = len(peptide)
    for length in range(1, n):
        for counter in range(n - length):
            peptides.append(peptide[counter:counter + length])
    return sorted([Mass(peptide) for peptide in peptides])


def peptide_is_consistent(peptide, Spectrum):
    peptide_spectrum = LinearSpectrum(peptide)
    for elem in peptide_spectrum:
        if elem not in Spectrum:
            return False
    return True


def Cyclospectrum(peptide):
    peptides = [peptide, ""]
    n = len(peptide)
    peptide += peptide
    for length in range(1, n):
        for i in range(n):
            peptides.append(peptide[i: (i + length)])
    return sorted([Mass(peptide) for peptide in peptides])


def Mass(peptide):
    return sum(peptide)


def expand(peptides):
    expanded_peptides = []
    for peptide in peptides:
        for acid in masses:
            expanded_peptides.append(peptide + acid)
    return expanded_peptides


def CyclopeptideSequencing(Spectrum):
    new_peptides = [""]
    cyclopeptide = []
    ParentMass = max(Spectrum)
    while True:
        peptides = expand(new_peptides)
        new_peptides = []
        for peptide in peptides:
            if Mass(peptide) == ParentMass:
                if Cyclospectrum(peptide) == Spectrum:
                    cyclopeptide.append(peptide)
            if peptide_is_consistent(peptide, Spectrum):
                new_peptides.append(peptide)
        if not new_peptides:
            break
    return cyclopeptide

spectrum = list(map(int, input().split()))

cyclopeptide = CyclopeptideSequencing(sorted(spectrum))

result = set()
for peptide in cyclopeptide:
    formatted = "-".join(str(masses[i]) for i in peptide)
    result.add(formatted)

print(" ".join(list(result)))