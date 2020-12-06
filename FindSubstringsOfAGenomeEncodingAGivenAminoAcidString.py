protein_encoding = {
    'AAA' : 'K',
    'AAC' : 'N',
    'AAG' : 'K',
    'AAU' : 'N',
    'ACA' : 'T',
    'ACC' : 'T',
    'ACG' : 'T',
    'ACU' : 'T',
    'AGA' : 'R',
    'AGC' : 'S',
    'AGG' : 'R',
    'AGU' : 'S',
    'AUA' : 'I',
    'AUC' : 'I',
    'AUG' : 'M',
    'AUU' : 'I',
    'CAA' : 'Q',
    'CAC' : 'H',
    'CAG' : 'Q',
    'CAU' : 'H',
    'CCA' : 'P',
    'CCC' : 'P',
    'CCG' : 'P',
    'CCU' : 'P',
    'CGA' : 'R',
    'CGC' : 'R',
    'CGG' : 'R',
    'CGU' : 'R',
    'CUA' : 'L',
    'CUC' : 'L',
    'CUG' : 'L',
    'CUU' : 'L',
    'GAA' : 'E',
    'GAC' : 'D',
    'GAG' : 'E',
    'GAU' : 'D',
    'GCA' : 'A',
    'GCC' : 'A',
    'GCG' : 'A',
    'GCU' : 'A',
    'GGA' : 'G',
    'GGC' : 'G',
    'GGG' : 'G',
    'GGU' : 'G',
    'GUA' : 'V',
    'GUC' : 'V',
    'GUG' : 'V',
    'GUU' : 'V',
    'UAA' : '$',
    'UAC' : 'Y',
    'UAG' : '$',
    'UAU' : 'Y',
    'UCA' : 'S',
    'UCC' : 'S',
    'UCG' : 'S',
    'UCU' : 'S',
    'UGA' : '$',
    'UGC' : 'C',
    'UGG' : 'W',
    'UGU' : 'C',
    'UUA' : 'L',
    'UUC' : 'F',
    'UUG' : 'L',
    'UUU' : 'F'}

def Translate(dna):
    rna = dna.replace('T', 'U')
    answer = ""
    for i in range(0, len(rna), 3):
        translation = protein_encoding[rna[i:i + 3]]
        if translation == '$':
            return answer
        answer += translation
    return answer


def ReverseComplement(str):
    complements = {'A': 'T', 'T': 'A', 'G': 'C', 'C': 'G'}
    return ''.join(complements[i] for i in reversed(str))

text = input()
amino = input()

n = len(amino)
for i in range(len(text) - 3*n + 1):
    if Translate(text[i:i + n*3]) == amino:
        print(text[i:i + n*3])
        continue
    if Translate(ReverseComplement(text[i:i + n*3])) == amino:
        print(text[i:i + n*3])
        continue
