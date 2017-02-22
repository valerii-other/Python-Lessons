fig = input("PLease input yoyr number: ")
s = str(fig)
s2=""

if fig < 0:
    s2+=s[0]
    for i in range(len(s)-1,0, -1):
        s2 += s[i]
elif fig > 0:
    for i in range(len(s)-1,-1,-1):
        s2+=s[i]

print(s2)
