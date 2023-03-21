mydict = {
    'name':"Musavir",
    'age':23,
}
# print(mydict.keys())
mydict['skills'] = "DJANGO"
# print(mydict['age'])
# print(mydict.get("skills"))
# print(mydict.keys())
# print(mydict.values())
mydict['age'] = 24
# print(mydict.items())

# if 'name' in mydict:
#     print("present")

mydict.update({'age':23})
mydict.update({'intrested':'cooking'})

# mydict.pop("intrested")
# del mydict['intrested']
# print(mydict)

# for x in mydict.values():
#     print(x)
    # print(x)
    # print(mydict[x])
# for x,y in mydict.items():
#     print(x,y)

# dict1 = mydict.copy()
# print(dict1)

dict2 = mydict.setdefault("name","musa")
print(dict2)


myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}
print(myfamily['child2']['name'])
