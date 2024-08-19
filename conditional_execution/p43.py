x = 3.1415926
s = str(x)
print(s,type(s))

x = 3.1415926
s = f"{x:0.6f}"
print(s,type(s))

x = 3.1415926*10000
s = f"{x:s,.3f}"
print(s,type(s))