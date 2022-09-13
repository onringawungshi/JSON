import json
# a={'4': 5, 
#     '6': 7, 
#     '1': 3, 
#     '2': 4}
a={"id" : 1, "name" : "value2", "age" : 29}
s=dict(sorted(a.items()))
b=json.dumps(s)
print(b)




