import sys

input = sys.stdin.readline


inputx = str(input())

listbox = []
a =""
for i in inputx:
    if i != "+" and i != "-":
        a+=i
        print("a", a)
    
    elif i == "+" or i == "-":
        listbox.append(a)
        listbox.append(i)
        a = ""
    
    else :
        print("hdsfs")
        listbox.append(a)

print("listbox", listbox)
        
