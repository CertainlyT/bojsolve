chem = input().replace("(", "#").replace(")", "#").split("#")
chem_dic = {"H": 1, "C": 12, "O": 16}

result = []

for i in range(len(chem)):
    if len(chem[i]) != 0:
        if len(chem[i]) == 1:
            if 50 <= ord(chem[i]) <= 57:
                result[-1] *= int(chem[i])
            else:
                result.append(chem_dic[chem[i]])
        else:
            temp = []
            for j in range(len(chem[i])):
                if 65 <= ord(chem[i][j]) <= 90:
                    temp.append(chem_dic[chem[i][j]])
                else:
                    temp[-1] *= int(chem[i][j])
            result.append(sum(temp))

print(sum(result))
