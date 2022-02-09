def game(number):
    number_1 = int(number[0])
    number_2 = int(number[1])
    if number_1 > number_2:
        return number_1 - number_2
    else:
        return number_2 - number_1


number = input()
print(game(number))
