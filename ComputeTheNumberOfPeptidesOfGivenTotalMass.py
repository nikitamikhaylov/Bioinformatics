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

memory = {}

def solve(mass):
    global memory
    answer = 0
    for key, value in masses.items():
        if memory.get(mass - value):
            answer += memory[mass - value]
        elif mass > value:
            answer += solve(mass - value)
        elif mass < value:
            break
        elif mass == value:
            return answer + 1
    memory[mass] = answer
    return answer

print(solve(int(input())))
