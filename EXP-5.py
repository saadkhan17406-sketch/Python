print("UNI : 251A053, DATE : 03-02-2026")
l = []
name = []
age = []
section = []
name.extend((input("ENTER YOUR NAME : "), input("ENTER YOUR FRIENDS NAME : ")))

age.extend((input("ENTER YOUR AGE : "), input("ENTER YOUR FRIENDS AGE : ")))

section.extend((input("ENTER YOUR SECTION : "), input("ENTER YOUR FRIENDS SECTION : ")))

l.append((name[0], age[0], section[0], name[1], age[1], section[1]))
print(l)