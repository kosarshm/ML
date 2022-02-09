def minority_count(a):

    b = str(a)
    count_zeros = 0
    count_ones = 0
    for i in b:
        if i == "0":
            count_zeros += 1
        elif i == "1":
            count_ones += 1
    if count_ones != count_zeros:
        return min(count_ones, count_zeros)
    elif count_ones == count_zeros:
        return "0"


t = int(input())
result = []

for i in range(1, t+1):
    a = input()
    result.append(minority_count(a))

for i in range(1, t+1):
    print(result[i-1])
