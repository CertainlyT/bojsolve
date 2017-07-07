num = int(input())

for i in range(num):
    a, b = map(str, input().split())

    if len(a) != len(b):
        print(a, "&", b, "are NOT anagrams.")
    else:
        c = list(a)
        d = list(b)
        c.sort()
        d.sort()
        if c == d:
            print(a, "&", b, "are anagrams.")
        else:
            print(a, "&", b, "are NOT anagrams.")