import operator

word = input()
word = word.upper()

word_dic = {}

for i in range(len(word)):
    if word[i] not in word_dic:
        word_dic[word[i]] = 1
    else:
        word_dic[word[i]] += 1

sorted_wordcount = sorted(word_dic.items(), key=operator.itemgetter(1), reverse=True)

count = []
for i in range(len(sorted_wordcount)):
    count.append(sorted_wordcount[i][1])

if count[0] == count[1]:
    print("?")
else:
    print(sorted_wordcount[0][0])

