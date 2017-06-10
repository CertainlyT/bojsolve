n = int(input())
dna = list(input())
dna.reverse()

for i in range(n-1):
    if dna[i] == dna[i+1]:
        pass
    elif (dna[i] == "A" and dna[i + 1] == "G") or (dna[i] == "G" and dna[i + 1] == "A"):
        dna[i+1] = "C"
    elif (dna[i] == "C" and dna[i + 1] == "A") or (dna[i] == "A" and dna[i + 1] == "C"):
        dna[i + 1] = "A"
    elif (dna[i] == "A" and dna[i + 1] == "T") or (dna[i] == "T" and dna[i + 1] == "A"):
        dna[i + 1] = "G"
    elif (dna[i] == "C" and dna[i + 1] == "G") or (dna[i] == "G" and dna[i + 1] == "C"):
        dna[i + 1] = "T"
    elif (dna[i] == "G" and dna[i + 1] == "T") or (dna[i] == "T" and dna[i + 1] == "G"):
        dna[i + 1] = "A"
    else:
        dna[i + 1] = "G"

print(dna[n-1])