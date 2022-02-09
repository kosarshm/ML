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

result_list = list(zip(result_names, result_acceptable))

result_dict = {}

for i in result_names:
    a = result_list.count((i, 1))
    if a != 0:
        result_dict.update({i: a})
        
print(result_dict)
