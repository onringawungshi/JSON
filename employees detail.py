# import json
# a=[["neelam","programer","24","2400"],
# ["komal","trainer","24","20000"],
# ["anuradha","HR","25","40000"],
# ["Abhishek","manager","29","63000"]]
# b=["name","designation","age","salary"]
# s={}
# i=0
# while i<len(a):
#     t={}
#     emp_dict={}
#     j=0
#     while j<len(a[i]):
#         s[b[j]]=a[i][j]
#         j+=1
#     i+=1
#     # emp_dict={}
#     m="emp"+str(i)
#     t[m]=s
#     emp_dict.update(t)
#     print(emp_dict)
    
    # with open("employee detail.json","w") as f:
    #     fil=json.dumps(emp_dict)
    #     f.write(fil)
    
# import json   
# a=[["Neelam","Programer","24","2400"],
# ["Komal","Trainer","24","20000"],
# ["Anuradha","HR","25","40000"],
# ["Abhishek","Manager","29","63000"]]
# b=["Name","Designation","Age","Salary"]
# d={}
# i=0
# while i<len(a):
#     s={}
#     m="emp"+str(i+1)
#     j=0
#     while j<len(a[i]):
#         s[b[j]]=a[i][j]
#         j+=1
#     i+=1
#     d[m]=s
# with open("employee detail.json","w") as f:
#     jsn_file=json.dump(d,f,indent=1)


# word="onring"
# i=len(word)-1
# while i>=0:
#     print(word[i],end="")
#     i-=1