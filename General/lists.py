mylist = ["apple","banana","Cherry"]
mylist[:] = ["mango",'orange','blackcurrant']
mylist.extend(mylist[:])
print(mylist)
print(mylist[0])
print(mylist[-1])
print(mylist[0:3])
print(mylist[-5:-2])
mylist[1] = "blackcurrant"
mylist[1:3] = ['blackcurrant',"watermelon"]
mylist[1:2] = ['blackcurrant',"watermelon"]
mylist[1:3] = ["watermelon"]
mylist.insert(  2,"watermelon")
mylist.append("orange")
mylist.remove("orange")
mylist.pop()
mylist.clear()
print(mylist)
# for x in mylist:
#     # print(x)
#     print(x[0])
# for i in range(len(mylist)):
#     print(mylist[i])

# i=0
# while i < len(mylist):
#     print(mylist[i])
#     i = i+1

# list comprehsension

# [print(x) for x in mylist]

# newlist = [x for x in mylist if x !='apple']
# print(newlist)

# for x in mylist:
#     newlist.append(x)
# print(newlist)

# Sort
#mylist.sort() #ascending order
# mylist.sort(key=str.lower) //case-insensitive sort function
# mylist.sort(reverse=True) //desending order
# mylist.reverse()
# print(mylist)


#copy a list
# thislist = mylist.copy()
# print(thislist)
# thislist = list(mylist)
# print(thislist)


# list = ["a","b","c"]
# list1 = [1,2,3,4]
# # list2 = list + list1
# for x in list1:
#     list.append(x)
# # print(list2)
# print(list)

print(mylist.count("banana"))