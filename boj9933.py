n = int(input())
word_list = []

for i in range(n):
    word = input()
    word_list.append(word)

for i in range(n):
    if word_list[i][::-1] in word_list:
        print(len(word_list[i]), word_list[i][(len(word_list[i])//2)])
        break
