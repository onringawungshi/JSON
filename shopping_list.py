# import json
# a={"shopping_list":{ "chaco":"15","Biscuits":"50","Diary_milk":"30","ice_cream":"20",}}
# a["shopping_list"]["lollipop"]=30
# b=json.dumps(a)
# c=json.loads(b)
# user=input("enter the item you want:")
# u=int(input("enter quantity of item:"))
# for i in c:
#     for j in c[i]:
#         if j==user:
#             v=c[i][user]
#             g=int(v)-u
#             c[i][user]=str(g)
# print(c)
# with open("shopping_list.json","w") as f:
#     store_in_jsn=json.dump(c,f)