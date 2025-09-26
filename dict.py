data = {"a": 1, "b": 2, "c": 3}
new_data = {key: value * 2 for key, value in data.items() if value % 2 != 0}
print(new_data)