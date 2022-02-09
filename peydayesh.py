def find(num1, num2, num3):
    list_input = [num1, num2, num3]
    for i in range(1, 5):
        if i not in list_input:
            return i


num1, num2, num3 = map(int, input().split())
print(find(num1, num2, num3))
