seq = ['a', 'b', 'c', 'd', 'e']

# creating dict with default values as None
res_dict = list(dict.fromkeys(seq))

print("The newly created dict with None values : " , res_dict)

cases = [{"id": 2, "age": 30}, {"id": 1, "age": 25}]
print(sorted(cases, key = lambda c: c["age"], reverse=False))