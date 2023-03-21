import json

data = '{"name":"Musavir","hobbies":["cooking","running"]}'

d = json.loads(data)
print(d)
print(d["name"])

f = open('sample.json')
data1 = json.load(f)
print(data1)
f.close()

dictionary = {
    "id": 1,
    "name":"musa",
    "rollno":33,
    "sgpa":8.31,
    "email":"musa@gmail.com",
    "courses": ["python","html","c++"]
}
print(json.dumps(dictionary,indent=3))

with open("sample.json","w") as outfile:
    json.dump(dictionary,outfile)