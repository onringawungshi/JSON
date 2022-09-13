import json
a={1:"onring",2:"manori",3:"lisa"}
with open("merki3.json","w") as fp:
    b=json.dumps(a,indent=1)
    print(b)