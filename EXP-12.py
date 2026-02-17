#file = open("s.txt","w")
#file.write("HELLO WORLD")
#file.close()
#file = open("s.txt","a")
#file.write("HELLO UNIVERSE")
#file.close()
file = open("s.txt","r")
content = file.read().split()
print(content)
n = int(input("ENTER THE WORD LENGTH : "))
for i in content:
   if len(i)==n:
       print(i)
file.close()