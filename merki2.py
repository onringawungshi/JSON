import json
d={"name": "David", "class": "I", "age": 6}
with open("merki2.json","w") as fp:
    json.dump(d,fp,indent=1)
    
    
