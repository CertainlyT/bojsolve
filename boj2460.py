human_count = 0
count_list = []

for i in range(10):
    a, b = map(int, input().split())
    human_count += b
    human_count -= a
    count_list.append(human_count)

print(max(count_list))