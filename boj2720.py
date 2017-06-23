n = int(input())

for i in range(n):
    quarter_count = -1
    dime_count = -1
    nickel_count = -1
    penny_count = -1
    c = int(input())
    while c >= 0:
        c -= 25
        quarter_count += 1
    c += 25
    while c >= 0:
        c -= 10
        dime_count += 1
    c += 10
    while c >= 0:
        c -= 5
        nickel_count += 1
    c += 5
    while c >= 0:
        c -= 1
        penny_count += 1
    print(quarter_count, dime_count, nickel_count, penny_count)