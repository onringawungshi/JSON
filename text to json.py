import json
fle_nme=open("Text.txt")
b=fle_nme.readlines()
emp_dict={}
for i in b:
    c=i.split()
    for j in c:
        emp_dict[j]=" ".join(c[1:])
        break
convert_jsn=json.dumps(emp_dict,indent=1)
jsn_file=open("Text to json.json","w")
w=jsn_file.write(convert_jsn)
jsn_file.close()