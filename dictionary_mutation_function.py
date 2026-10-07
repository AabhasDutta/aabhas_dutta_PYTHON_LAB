def add_entry(d):
    d["age"] = 21

def reassign_dict(d):
    d = {"name": "Rahul", "age": 25}

my_dict = {"name": "Amit"}

add_entry(my_dict)
print("After add_entry:", my_dict)
reassign_dict(my_dict)
print("After reassign_dict:", my_dict)