n = int(input())
gene = input()

for i in range(len(gene), -1, -1):
    if gene[i] == gene[i-1]:
        pass
    elif gene[i-1]