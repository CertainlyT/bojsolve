A = input()
B = input()

answer = ["", "", "", "", ""]

for i in range(len(A)):
    if A[i] == "1" and B[i] == "1":
        answer[0] += "1"
    else:
        answer[0] += "0"
    if A[i] == "1" or B[i] == "1":
        answer[1] += "1"
    else:
        answer[1] += "0"
    if A[i] == B[i]:
        answer[2] += "0"
    else:
        answer[2] += "1"
    if A[i] == "1":
        answer[3] += "0"
    else:
        answer[3] += "1"
    if B[i] == "1":
        answer[4] += "0"
    else:
        answer[4] += "1"

for i in range(5):
    print(answer[i])