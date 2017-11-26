n = int(input())
str1 = input()
str2 = input()

if n % 2 == 1:
    for i in range(len(str1)):
        if str1[i] == str2[i]:
            print("Deletion failed")
            break
    else:
        print("Deletion succeeded")

else:
    for i in range(len(str1)):
        if str1[i] != str2[i]:
            print("Deletion failed")
            break
    else:
        print("Deletion succeeded")