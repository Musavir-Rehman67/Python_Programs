import re
txt = "The rain in Spain"
# x = re.search("^The.*Spain$",txt)
# print(x.span()) #tuple with start and end match occurence
# print(x.string) # string passed into function
x = re.search(r"\bS\w+", txt)
print(x.group()) #part of string where there was a match
# x = re.findall("ai",txt)
# print(x)
# x = re.split("\s", txt) #retuurns a list 
# x = re.sub("\s", "9", txt) #replace all whitespace charachters with 9
# print(x)
# if x:
#     print("Yes")
# else:
#     print("No")