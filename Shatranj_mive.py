v = ({'name': 'apple', 'shape': 'sphere', 'mass': 350, 'volume': 120},
     {'name': 'mango', 'shape': 'square', 'mass': 150, 'volume': 120},
     {'name': 'lemon', 'shape': 'sphere', 'mass': 300, 'volume': 100},
     {'name': 'apple', 'shape': 'sphere', 'mass': 500, 'volume': 250})

result_names = []
result_acceptable = []

for i in v:

    if i['shape'] == "sphere" and 300 <= i['mass'] <= 600 and 100 <= i['volume'] <= 500:
        result_acceptable.append(1)
        result_names.append(i['name'])

#print(result_names)
#print(result_acceptable)

result_list = list(zip(result_names, result_acceptable))
#print(result_list)

count_map = {}
for i in result_list:
    count_map[i] = count_map.get(i, 0) + 1
print(count_map)

#dict2 = {k: v for k, v in count_map.items()}
#print(dict2)

#solution = {'apple': 2, 'lemon': 1}
