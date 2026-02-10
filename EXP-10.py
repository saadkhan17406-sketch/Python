#https://github.com/saadkhan17406-sketch/Python
#FACTORIAL GENERATOR
print("UIN : 251A053  DATE : 10-02-2026")
n = int(input("ENTER NUMBER : "))
for i in range(2, n):
  if n%i == 0:
    print(f"{i} IS NOT PRIME ")
  else:
    print(f"{i} IS PRIME ")
