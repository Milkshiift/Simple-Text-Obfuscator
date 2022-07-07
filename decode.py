name = input("Name of file (with txt): ")
file1 = open(name, "r")

txt = file1.readline()
f = False
i = 0
pos = 0
while not f:
    i = i + 1
    if txt[len(txt) - i: len(txt) - i + 1] == "P":
        pos = len(txt) - i
        break
f = False
i = 0
pos1 = 0
while not f:
    i = i + 1
    if txt[pos - i: pos - i + 1] == "S":
        pos1 = pos - i
        break
code1 = txt[pos1 + 1: pos]
code2 = txt[pos + 1:len(txt)]
print("Output: " + txt[int(code1):int(code2)])
