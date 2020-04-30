m_file = open('text_6.txt', 'r', encoding='utf-8')
readfile = m_file.readlines()

mydict = {}
for n in readfile:
    a = n.split()
    mydict[a[0]] = (a[1:4])

print(mydict)